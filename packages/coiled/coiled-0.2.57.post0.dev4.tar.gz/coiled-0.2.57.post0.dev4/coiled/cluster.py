from __future__ import annotations

import asyncio
import datetime
import enum
import logging
import sys
import time
import warnings
import weakref
from asyncio import wait_for
from contextlib import suppress
from typing import (
    Awaitable,
    Callable,
    Dict,
    Generic,
    Optional,
    Set,
    TypeVar,
    Union,
    cast,
    overload,
)

import botocore
import dask
import dask.distributed
import distributed.deploy
import tlz as toolz
from dateutil import tz
from distributed.core import Status
from distributed.deploy.adaptive import Adaptive
from typing_extensions import Literal

from coiled.context import track_context

from .compatibility import DISTRIBUTED_VERSION
from .core import Async, AWSSessionCredentials, Cloud, IsAsynchronous, Sync
from .utils import (
    COILED_LOGGER_NAME,
    name_exists_in_dict,
    parse_identifier,
    parse_wait_for_workers,
    scheduler_ports,
    validate_account,
)

logger = logging.getLogger(COILED_LOGGER_NAME)


@enum.unique
class CredentialsPreferred(enum.Enum):
    LOCAL = "local"
    # USER = 'user'
    ACCOUNT = "account"  # doesn't work, should be fixed or deprecated/removed someday
    NONE = None


_T = TypeVar("_T")


class CoiledAdaptive(Adaptive):
    async def scale_up(self, n):
        logger.info(f"Adaptive scaling up to {n} workers.")
        await self.cluster.scale_up(n)

    async def scale_down(self, workers):
        if not workers:
            return
        logger.info(f"Adaptive is removing {len(workers)} workers: {workers}.")
        await self.cluster.scale_down(workers)


class Cluster(distributed.deploy.Cluster, Generic[IsAsynchronous]):
    """Create a Dask cluster with Coiled

    Parameters
    ----------
    n_workers
        Number of workers in this cluster. Defaults to 4.
    configuration
        Name of cluster configuration to create cluster from.
        If not specified, defaults to ``coiled/default`` for the
        current Python version.
    name
        Name to use for identifying this cluster. Defaults to ``None``.
    software
        Identifier of the software environment to use, in the format (<account>/)<name>. If the software environment
        is owned by the same account as that passed into "account", the (<account>/) prefix is optional.

        For example, suppose your account is "wondercorp", but your friends at "friendlycorp" have an environment
        named "xgboost" that you want to use; you can specify this with "friendlycorp/xgboost". If you simply
        entered "xgboost", this is shorthand for "wondercorp/xgboost".

        The "name" portion of (<account>/)<name> can only contain ASCII letters, hyphens and underscores.
    worker_cpu
        Number of CPUs allocated for each worker. Defaults to 2.
    worker_gpu
        Number of GPUs allocated for each worker. Defaults to 0 (no GPU support). Note that this will _always_
        allocate GPU-enabled workers, so is expensive. This option will always allocate on demand instances, you
        can change this behaviour by using ``"spot": False`` on the ``backend_options`` parameter.
    worker_gpu_type
        Type of GPU to use for this cluster. For AWS GPU types are tied to the instance type, but for
        GCP you can add different GPU types to an instance. Please refer to :doc:`gpu` for
        more information.
        You can run the command ``coiled.list_gpu_types()`` to see a list of allowed GPUs.
    worker_memory
        Amount of memory to allocate for each worker. Defaults to 8 GiB.
    worker_class
        Worker class to use. Defaults to "dask.distributed.Nanny".
    worker_options
        Mapping with keyword arguments to pass to ``worker_class``. Defaults to ``{}``.
    worker_vm_types
        List of instance types that you would like workers to use, this list can have up to five items.
        You can use the command ``coiled.list_instance_types()`` to se a list of allowed types.
    scheduler_cpu
        Number of CPUs allocated for the scheduler. Defaults to 1.
    scheduler_memory
        Amount of memory to allocate for the scheduler. Defaults to 4 GiB.
    scheduler_class
        Scheduler class to use. Defaults to "dask.distributed.Scheduler".
    scheduler_options
        Mapping with keyword arguments to pass to ``scheduler_class``. Defaults to ``{}``.
    scheduler_vm_types
        List of instance types that you would like the scheduler to use, this list can have up to
        five items.
        You can use the command ``coiled.list_instance_types()`` to se a list of allowed types.
    asynchronous
        Set to True if using this Cloud within ``async``/``await`` functions or
        within Tornado ``gen.coroutines``. Otherwise this should remain
        ``False`` for normal use. Default is ``False``.
    cloud
        Cloud object to use for interacting with Coiled.
    account
        Name of Coiled account to use. If not provided, will
        default to the user account for the ``cloud`` object being used.
    shutdown_on_close
        Whether or not to shut down the cluster when it finishes.
        Defaults to True, unless name points to an existing cluster.
    use_scheduler_public_ip
        Boolean value that determines if the Python client connects to the Dask scheduler using the scheduler machine's
        public IP address. The default behaviour when set to True is to connect to the scheduler using its public IP
        address, which means traffic will be routed over the public internet. When set to False, traffic will be
        routed over the local network the scheduler lives in, so make sure the scheduler private IP address is
        routable from where this function call is made when setting this to False.
    backend_options
        Dictionary of backend specific options (e.g. ``{'region': 'us-east-2'}``). Any options
        specified with this keyword argument will take precedence over those stored in the
        ``coiled.backend-options`` cofiguration value.
    credentials
        Which credentials to use for Dask operations and forward to Dask clusters --
        options are "account", "local", or "none". The default behavior is to prefer
        credentials associated with the Coiled Account, if available, then try to
        use local credentials, if available.
        NOTE: credential handling currently only works with AWS credentials.
    timeout
        Timeout in seconds to wait for a cluster to start, will use ``default_cluster_timeout``
        set on parent Cloud by default.
    environ
        Dictionary of environment variables.
    protocol
        Communication protocol for the cluster. Default is ``tls``.
    wait_for_workers
        Whether or not to wait for a number of workers before returning control of the prompt back to the user.
        Usually, computations will run better if you wait for most workers before submitting tasks to the cluster.
        You can wait for all workers by passing ``True``, or not wait for any by passing ``False``.
        You can pass a fraction of the total number of workers requested as a float(like 0.6),
        or a fixed number of workers as an int (like 13). If None, the value from
        ``coiled.wait-for-workers`` in your Dask config will be used. Default: 0.3.
        If the requested number of workers don't launch within 10 minutes, the cluster will be shut down,
        then a TimeoutError is raised.

    """

    _instances = weakref.WeakSet()

    @overload
    def __init__(
        self: Cluster[Sync],
        name: Optional[str] = None,
        *,
        n_workers: int = 4,
        configuration: Optional[str] = None,
        software: Optional[str] = None,
        worker_cpu: Optional[int] = None,
        worker_gpu: Optional[int] = None,
        worker_gpu_type: Optional[str] = None,
        worker_memory: Optional[str] = None,
        worker_class: Optional[str] = None,
        worker_options: Optional[dict] = None,
        worker_vm_types: Optional[list] = None,
        scheduler_cpu: Optional[int] = None,
        scheduler_memory: Optional[str] = None,
        scheduler_class: Optional[str] = None,
        scheduler_options: Optional[dict] = None,
        scheduler_vm_types: Optional[list] = None,
        asynchronous: Sync = False,
        cloud: Optional[Literal[None]] = None,
        account: Optional[str] = None,
        shutdown_on_close=None,
        backend_options: Optional[Dict] = None,
        credentials: Optional[str] = "local",
        timeout: Optional[int] = None,
        environ: Optional[Dict[str, str]] = None,
        protocol: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(
        self: Cluster[Sync],
        name: Optional[str] = None,
        *,
        n_workers: int = 4,
        configuration: Optional[str] = None,
        software: Optional[str] = None,
        worker_cpu: Optional[int] = None,
        worker_gpu: Optional[int] = None,
        worker_gpu_type: Optional[str] = None,
        worker_memory: Optional[str] = None,
        worker_class: Optional[str] = None,
        worker_options: Optional[dict] = None,
        worker_vm_types: Optional[list] = None,
        scheduler_cpu: Optional[int] = None,
        scheduler_memory: Optional[str] = None,
        scheduler_class: Optional[str] = None,
        scheduler_options: Optional[dict] = None,
        scheduler_vm_types: Optional[list] = None,
        asynchronous: bool = False,
        cloud: Cloud[Sync],
        account: Optional[str] = None,
        shutdown_on_close=None,
        backend_options: Optional[Dict] = None,
        credentials: Optional[str] = "local",
        timeout: Optional[int] = None,
        environ: Optional[Dict[str, str]] = None,
        protocol: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(
        self: Cluster[Async],
        name: Optional[str] = None,
        *,
        n_workers: int = 4,
        configuration: Optional[str] = None,
        software: Optional[str] = None,
        worker_cpu: Optional[int] = None,
        worker_gpu: Optional[int] = None,
        worker_gpu_type: Optional[str] = None,
        worker_memory: Optional[str] = None,
        worker_class: Optional[str] = None,
        worker_options: Optional[dict] = None,
        worker_vm_types: Optional[list] = None,
        scheduler_cpu: Optional[int] = None,
        scheduler_memory: Optional[str] = None,
        scheduler_class: Optional[str] = None,
        scheduler_options: Optional[dict] = None,
        scheduler_vm_types: Optional[list] = None,
        asynchronous: Async = True,
        cloud: Optional[Literal[None]] = None,
        account: Optional[str] = None,
        shutdown_on_close=None,
        backend_options: Optional[Dict] = None,
        credentials: Optional[str] = "local",
        timeout: Optional[int] = None,
        environ: Optional[Dict[str, str]] = None,
        protocol: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(
        self: Cluster[Async],
        name: Optional[str] = None,
        *,
        n_workers: int = 4,
        configuration: Optional[str] = None,
        software: Optional[str] = None,
        worker_cpu: Optional[int] = None,
        worker_gpu: Optional[int] = None,
        worker_gpu_type: Optional[str] = None,
        worker_memory: Optional[str] = None,
        worker_class: Optional[str] = None,
        worker_options: Optional[dict] = None,
        worker_vm_types: Optional[list] = None,
        scheduler_cpu: Optional[int] = None,
        scheduler_memory: Optional[str] = None,
        scheduler_class: Optional[str] = None,
        scheduler_options: Optional[dict] = None,
        scheduler_vm_types: Optional[list] = None,
        asynchronous: bool = False,
        cloud: Cloud[Async],
        account: Optional[str] = None,
        shutdown_on_close=None,
        backend_options: Optional[Dict] = None,
        credentials: Optional[str] = "local",
        timeout: Optional[int] = None,
        environ: Optional[Dict[str, str]] = None,
        protocol: Optional[str] = None,
    ):
        ...

    def __init__(
        self,
        name: Optional[str] = None,
        *,
        n_workers: int = 4,
        configuration: Optional[str] = None,
        software: Optional[str] = None,
        worker_cpu: Optional[int] = None,
        worker_gpu: Optional[int] = None,
        worker_gpu_type: Optional[str] = None,
        worker_memory: Optional[str] = None,
        worker_class: Optional[str] = None,
        worker_options: Optional[dict] = None,
        worker_vm_types: Optional[list] = None,
        scheduler_cpu: Optional[int] = None,
        scheduler_memory: Optional[str] = None,
        scheduler_class: Optional[str] = None,
        scheduler_options: Optional[dict] = None,
        scheduler_vm_types: Optional[list] = None,
        asynchronous: bool = False,
        cloud: Optional[Cloud] = None,
        account: Optional[str] = None,
        shutdown_on_close=None,
        use_scheduler_public_ip: Optional[bool] = None,
        backend_options: Optional[Dict] = None,
        credentials: Optional[str] = "local",
        timeout: Optional[int] = None,
        environ: Optional[Dict[str, str]] = None,
        protocol: Optional[str] = None,
        wait_for_workers: Optional[bool | int | float] = None,
    ):
        type(self)._instances.add(self)
        # Determine consistent sync/async
        if cloud and asynchronous is not None and cloud.asynchronous != asynchronous:
            warnings.warn(
                f"Requested a Cluster with asynchronous={asynchronous}, but "
                f"cloud.asynchronous={cloud.asynchronous}, so the cluster will be"
                f"{cloud.asynchronous}"
            )
            asynchronous = cloud.asynchronous

        self.scheduler_comm: Optional[dask.distributed.rpc] = None

        self.cloud: Cloud[IsAsynchronous] = cloud or Cloud.current(
            asynchronous=asynchronous
        )

        # As of distributed 2021.12.0, deploy.Cluster has a ``loop`` attribute on the
        # base class. We add the attribute manually here for backwards compatibility.
        # TODO: if/when we set the minimum distributed version to be >= 2021.12.0,
        # remove this check.
        if DISTRIBUTED_VERSION >= "2021.12.0":
            kwargs = {"loop": self.cloud.loop}
        else:
            kwargs = {}
            self.loop = self.cloud.loop

        # we really need to call this first before any of the below code errors
        # out; otherwise because of the fact that this object inherits from
        # deploy.Cloud __del__ (and perhaps __repr__) will have AttributeErrors
        # because the gc will run and attributes like `.status` and
        # `.scheduler_comm` will not have been assigned to the object's instance
        # yet
        super().__init__(asynchronous, **kwargs)

        self.timeout = (
            timeout if timeout is None else self.cloud.default_cluster_timeout
        )
        if configuration is None:
            v = "".join(map(str, sys.version_info[:2]))
            configuration = f"coiled/default-py{v}"
        self.configuration = configuration
        if software is None:
            software = dask.config.get("coiled.software")
        self.software = software
        if worker_cpu is None:
            worker_cpu = dask.config.get("coiled.worker.cpu")
        self.worker_cpu = worker_cpu
        if worker_gpu is None:
            worker_gpu = dask.config.get("coiled.worker.gpu")
        self.worker_gpu = worker_gpu
        if worker_memory is None:
            worker_memory = dask.config.get("coiled.worker.memory")
        self.worker_memory = worker_memory
        self.worker_class = worker_class or dask.config.get("coiled.worker.class")
        self.worker_options = {
            **(dask.config.get("coiled.worker-options", {})),
            **(worker_options or {}),
        }
        if worker_vm_types is None:
            worker_vm_types = dask.config.get("coiled.worker.vm-types")
        self.worker_vm_types = worker_vm_types
        if worker_gpu_type is None:
            worker_gpu_type = dask.config.get("coiled.worker.gpu-types")
        self.worker_gpu_type = worker_gpu_type
        if scheduler_cpu is None:
            scheduler_cpu = dask.config.get("coiled.scheduler.cpu")
        self.scheduler_cpu = scheduler_cpu
        if scheduler_memory is None:
            scheduler_memory = dask.config.get("coiled.scheduler.memory")
        self.scheduler_memory = scheduler_memory
        self.scheduler_class = scheduler_class or dask.config.get(
            "coiled.scheduler.class"
        )
        self.scheduler_options = {
            **(dask.config.get("coiled.scheduler-options", {})),
            **(scheduler_options or {}),
        }
        if scheduler_vm_types is None:
            scheduler_vm_types = dask.config.get("coiled.scheduler.vm_types")
        self.scheduler_vm_types = scheduler_vm_types
        if account:
            validate_account(account)
        self.name = name or dask.config.get("coiled.name")
        self.account = account
        self._start_n_workers = n_workers
        self._lock = None
        self._asynchronous = asynchronous
        self.shutdown_on_close = shutdown_on_close
        self.environ = {k: str(v) for (k, v) in (environ or {}).items() if v}
        self.credentials = CredentialsPreferred(credentials)
        self._default_protocol = dask.config.get("coiled.protocol", "tls")
        self._requested: Set[str] = set()
        self._plan: Set[str] = set()
        self._adaptive_options: Dict[str, Union[str, int]] = {}
        self.cluster_id: Optional[int] = None
        self.use_scheduler_public_ip: bool = (
            dask.config.get("coiled.use_scheduler_public_ip", True)
            if use_scheduler_public_ip is None
            else use_scheduler_public_ip
        )
        self.backend_options = {
            **(dask.config.get("coiled.backend-options", None) or {}),
            **(backend_options or {}),
        }

        self._name = "coiled.Cluster"  # Used in Dask's Cluster._ipython_display_
        self.wait_for_workers = parse_wait_for_workers(n_workers, wait_for_workers)
        if self.scheduler_options:
            if "protocol" in self.scheduler_options:
                if protocol:
                    raise RuntimeError(
                        "Top level `protocol` collides with `scheduler_options`"
                    )
            else:
                self.scheduler_options.update(
                    {"protocol": protocol or self._default_protocol}
                )
            if "port" not in self.scheduler_options:
                self.scheduler_options.update(
                    {"port": scheduler_ports(self.scheduler_options["protocol"])}
                )
        else:
            self.scheduler_options = {
                "protocol": protocol or self._default_protocol,
                "port": scheduler_ports(protocol or self._default_protocol),
            }

        if self.worker_options:
            if "protocol" in self.worker_options:
                if protocol:
                    raise RuntimeError(
                        "Top level `protocol` collides with `worker_options`"
                    )
            else:
                self.worker_options.update(
                    {"protocol": protocol or self._default_protocol}
                )
        else:
            self.worker_options = {"protocol": protocol or self._default_protocol}

        if not self.asynchronous:
            self.sync(self._start)

    @property
    def requested(self):
        return self._requested

    @property
    def plan(self):
        return self._plan

    @overload
    def sync(
        self: Cluster[Sync],
        func: Callable[..., Awaitable[_T]],
        *args,
        asynchronous: Union[Sync, Literal[None]] = None,
        callback_timeout=None,
        **kwargs,
    ) -> _T:
        ...

    @overload
    def sync(
        self: Cluster[Async],
        func: Callable[..., Awaitable[_T]],
        *args,
        asynchronous: Union[bool, Literal[None]] = None,
        callback_timeout=None,
        **kwargs,
    ) -> Awaitable[_T]:
        ...

    def sync(
        self,
        func: Callable[..., Awaitable[_T]],
        *args,
        asynchronous: Optional[bool] = None,
        callback_timeout=None,
        **kwargs,
    ) -> Union[_T, Awaitable[_T]]:
        return super().sync(
            func,
            *args,
            asynchronous=asynchronous,
            callback_timeout=callback_timeout,
            **kwargs,
        )

    def _ensure_scheduler_comm(self) -> dask.distributed.rpc:
        """
        Guard to make sure that the scheduler comm exists before trying to use it.
        """
        if not self.scheduler_comm:
            raise RuntimeError(
                "Scheduler comm is not set, have you been disconnected from Coiled?"
            )
        return self.scheduler_comm

    @track_context
    async def _wait_for_workers(
        self,
        n_workers,
        timeout=None,
        err_msg=None,
    ) -> None:
        if timeout is None:
            deadline = None
        else:
            timeout = dask.utils.parse_timedelta(timeout, "s")
            deadline = time.time() + timeout
        while n_workers and len(self.scheduler_info["workers"]) < n_workers:
            if deadline and time.time() > deadline:
                err_msg = err_msg or (
                    f"Timed out after {timeout} seconds waiting for {n_workers} workers to arrive, "
                    "check your notifications with coiled.get_notifications() for further details"
                )
                raise TimeoutError(err_msg)
            await asyncio.sleep(1)

    async def _check_software_environment_exists(
        self, cloud: Cloud[Async]
    ) -> Optional[dict]:
        """Check if software environment exists.

        When we list software environments, we get the user software environments
        and any software environments from the team that the user belongs to. We
        should check if the software environment name that he user is trying to use
        exists. If we can't find the software environment with the given name, we
        will use coiled's default one and tell the user about this. That way we
        don't stop the Cluster creation process if the software env doesn't exist.

        """
        if self.software:
            account, software_name, revision = parse_identifier(
                self.software,
                property_name="software_environment",
                can_have_revision=True,
            )

            software_envs = await cloud.list_software_environments(account=account)

            if name_exists_in_dict(
                user=self.account or cloud.default_account,
                name=self.software,
                dictionary=software_envs,
            ):

                return software_envs

            raise ValueError(
                f" Unable to create Cluster: Software environment with the name '{software_name}' "
                "not found. Have you created this software environment or have you specified your "
                "software environment in the format '<account>/<software environment>'?"
            )

        return None

    @staticmethod
    async def _get_aws_local_session_token() -> AWSSessionCredentials:
        token_creds = AWSSessionCredentials(
            AccessKeyId="", SecretAccessKey="", SessionToken=None, Expiration=None
        )
        try:
            from aiobotocore.session import get_session as get_aiobotocore_session

            session = get_aiobotocore_session()
            async with session.create_client("sts") as sts:
                try:
                    credentials = await sts.get_session_token()
                    credentials = credentials["Credentials"]
                    token_creds = AWSSessionCredentials(
                        AccessKeyId=credentials.get("AccessKeyId", ""),
                        SecretAccessKey=credentials.get("SecretAccessKey", ""),
                        SessionToken=credentials.get("SessionToken"),
                        Expiration=credentials.get("Expiration"),
                    )
                except botocore.errorfactory.ClientError as e:
                    if "session credentials" in str(e):
                        # Credentials are already an STS token, which gives us this error:
                        # > Cannot call GetSessionToken with session credentials
                        # In this case we'll just use the existing STS token for the active, local session.
                        # Note that in some cases this will have a shorter TTL than the default 12 hour tokens.
                        credentials = await session.get_credentials()
                        frozen_creds = await credentials.get_frozen_credentials()

                        token_creds = AWSSessionCredentials(
                            AccessKeyId=frozen_creds.access_key,
                            SecretAccessKey=frozen_creds.secret_key,
                            SessionToken=frozen_creds.token,
                            Expiration=credentials._expiry_time
                            if hasattr(credentials, "_expiry_time")
                            else None,
                        )

        except (
            botocore.exceptions.ProfileNotFound,
            botocore.exceptions.NoCredentialsError,
        ):
            # no AWS credentials (maybe not running against AWS?), fail gracefully
            pass
        except Exception as e:
            # for some aiobotocore versions (e.g. 2.3.4) we get one of these errors
            # rather than NoCredentialsError
            if "Could not connect to the endpoint URL" in str(e):
                pass
            elif "Connect timeout on endpoint URL" in str(e):
                pass
            else:
                # warn, but don't crash
                logging.warning(f"Error getting STS token from client AWS session: {e}")

        return token_creds

    async def _send_credentials(self, schedule_callback: bool = True):
        """
        Get credentials and pass them to the scheduler.
        """
        if self.credentials is not CredentialsPreferred.NONE:
            try:
                if self.credentials is CredentialsPreferred.ACCOUNT:
                    # cloud.get_aws_credentials doesn't return credentials for currently implemented backends
                    # aws_creds = await cloud.get_aws_credentials(self.account)
                    logging.warning(
                        "Using account backend AWS credentials is not currently supported, "
                        "local AWS credentials (if present) will be used."
                    )

                token_creds = await self._get_aws_local_session_token()
                if token_creds:
                    scheduler_comm = self._ensure_scheduler_comm()

                    await scheduler_comm.aws_update_credentials(
                        credentials={
                            k: token_creds.get(k)
                            for k in [
                                "AccessKeyId",
                                "SecretAccessKey",
                                "SessionToken",
                            ]
                        }
                    )

                    if schedule_callback:
                        # schedule callback for updating creds before they expire

                        # default to updating every 55 minutes
                        delay = 55 * 60

                        expiration = token_creds.get("Expiration")
                        if expiration:
                            diff = expiration - datetime.datetime.now(tz=tz.UTC)
                            delay = (diff * 0.9).total_seconds()

                            if diff < datetime.timedelta(minutes=5):
                                # we shouldn't expect to see this, but it's possible if local session is old STS token
                                # TODO give user information about what to do in this case
                                logging.warning(
                                    f"Locally generated AWS STS token expires in less than 5 minutes ({diff}). "
                                    "Code running on your cluster may be unable to access other AWS services (e.g, S3) "
                                    "when this token expires."
                                )

                        # don't try to update sooner than in 5 minute
                        delay = max(300, delay)

                        self.loop.call_later(
                            delay=delay, callback=self._send_credentials
                        )

            except Exception as e:
                terminating_states = (
                    Status.closing,
                    Status.closed,
                    Status.closing_gracefully,
                    Status.failed,
                )
                if self.status not in terminating_states:
                    # warn, but don't crash
                    logging.warning(f"error sending AWS credentials to cluster: {e}")

    def __await__(self: Cluster[Async]):
        async def _():
            if self._lock is None:
                self._lock = asyncio.Lock()
            async with self._lock:
                if self.status == Status.created:
                    await wait_for(self._start(), self.timeout)
                assert self.status == Status.running
            return self

        return _().__await__()

    @overload
    def close(self: Cluster[Sync], force_shutdown: bool = False) -> None:
        ...

    @overload
    def close(self: Cluster[Async], force_shutdown: bool = False) -> Awaitable[None]:
        ...

    def close(self, force_shutdown: bool = False) -> Union[None, Awaitable[None]]:
        """
        Close the cluster.
        """
        return self.sync(self._close, force_shutdown=force_shutdown)

    @track_context
    async def _close(self, force_shutdown: bool = False) -> None:
        # Send a profile snapshot on close, before workers have been torn down.
        # If profiling data has been sent recently, this should be a no-op.
        if self.scheduler_comm:
            await self.scheduler_comm.send_profile()

        cloud = cast(Cloud[Async], self.cloud)
        with suppress(AttributeError):
            self._adaptive.stop()

        # Stop here because otherwise we get intermittent `OSError: Timed out` when
        # deleting cluster takes a while and callback tries to poll cluster status.
        for pc in self.periodic_callbacks.values():
            pc.stop()

        if hasattr(self, "cluster_id") and self.cluster_id:
            if force_shutdown or self.shutdown_on_close in (True, None):
                await cloud.delete_cluster(
                    account=self.account,
                    cluster_id=self.cluster_id,
                )
        await super()._close()

    @overload
    def shutdown(self: Cluster[Sync]) -> None:
        ...

    @overload
    def shutdown(self: Cluster[Async]) -> Awaitable[None]:
        ...

    def shutdown(self) -> Union[None, Awaitable[None]]:
        """
        Shutdown the cluster; useful when shutdown_on_close is False.
        """
        return self.sync(self._close, force_shutdown=True)

    @track_context
    async def _scale(self, n: int) -> None:
        if not self.cluster_id:
            raise ValueError("No cluster available to scale!")
        recommendations = await self.recommendations(n)
        status = recommendations.pop("status")
        if status == "same":
            return
        if status == "up":
            return await self.scale_up(**recommendations)
        if status == "down":
            return await self.scale_down(**recommendations)

    @overload
    def scale(self: Cluster[Sync], n: int) -> None:
        ...

    @overload
    def scale(self: Cluster[Async], n: int) -> Awaitable[None]:
        ...

    def scale(self, n: int) -> Optional[Awaitable[None]]:
        """Scale cluster to ``n`` workers

        Parameters
        ----------
        n
            Number of workers to scale cluster size to.
        """
        return self.sync(self._scale, n=n)

    @track_context
    async def scale_up(self, n: int) -> None:
        if not self.cluster_id:
            raise ValueError(
                "No cluster available to scale! "
                "Check cluster was not closed by another process."
            )
        cloud = cast(Cloud[Async], self.cloud)
        response = await cloud._scale_up(
            account=self.account,
            cluster_id=self.cluster_id,
            n=n,
        )
        if response:
            self._plan.update(set(response.get("workers", [])))
            self._requested.update(set(response.get("workers", [])))

    @track_context
    async def scale_down(self, workers: set) -> None:
        if not self.cluster_id:
            raise ValueError("No cluster available to scale!")
        cloud = cast(Cloud[Async], self.cloud)
        try:
            scheduler_comm = self._ensure_scheduler_comm()
            await scheduler_comm.retire_workers(
                names=workers,
                remove=True,
                close_workers=True,
            )
        except Exception as e:
            logging.warning(f"error retiring workers {e}. Trying more forcefully")
        # close workers more forcefully
        await cloud._scale_down(
            account=self.account,
            cluster_id=self.cluster_id,
            workers=workers,
        )
        self._plan.difference_update(workers)
        self._requested.difference_update(workers)

    async def recommendations(self, target: int) -> dict:
        """
        Make scale up/down recommendations based on current state and target
        """
        plan = self.plan
        requested = self.requested
        observed = self.observed

        if target == len(plan):
            return {"status": "same"}

        if target > len(plan):
            return {"status": "up", "n": target}

        not_yet_arrived = requested - observed
        to_close = set()
        if not_yet_arrived:
            to_close.update(toolz.take(len(plan) - target, not_yet_arrived))

        if target < len(plan) - len(to_close):
            L = await self.workers_to_close(target=target)
            to_close.update(L)
        return {"status": "down", "workers": list(to_close)}

    async def workers_to_close(self, target: int):
        """
        Determine which, if any, workers should potentially be removed from
        the cluster.

        Notes
        -----
        ``Cluster.workers_to_close`` dispatches to Scheduler.workers_to_close(),
        but may be overridden in subclasses.

        Returns
        -------
        List of worker addresses to close, if any

        See Also
        --------
        Scheduler.workers_to_close
        """
        scheduler_comm = self._ensure_scheduler_comm()
        ret = await scheduler_comm.workers_to_close(
            target=target,
            attribute="name",
        )
        return ret

    def adapt(self, Adaptive=CoiledAdaptive, **kwargs) -> Adaptive:
        """Dynamically scale the number of workers in the cluster
        based on scaling heuristics.

        Parameters
        ----------
        minimum : int
            Minimum number of workers that the cluster should have while
            on low load, defaults to 1.
        maximum : int
            Maximum numbers of workers that the cluster should have while
            on high load. If maximum is not set, this value will be based
            on your core count limit. This value is also capped by your
            core count limit.
        wait_count : int
            Number of consecutive times that a worker should be suggested
            for removal before the cluster removes it, defaults to 60.
        interval : timedelta or str
            Milliseconds between checks, default sto 5000 ms.
        target_duration : timedelta or str
            Amount of time we want a computation to take. This affects how
            aggressively the cluster scales up, defaults to 5s.

        """
        maximum = kwargs.pop("maximum", None)
        if maximum is not None:
            kwargs["maximum"] = maximum
        return super().adapt(Adaptive=Adaptive, **kwargs)

    def _set_adaptive_options(self, info):
        cpu = info["configuration"]["worker"]["cpu"]
        limit = self.cloud.accounts[self.account or self.cloud.default_account][
            "user_limit"
        ]
        self._adaptive_options = {
            "interval": "5s",
            "wait_count": 60,
            "minimum": 1,
            "maximum": int(limit / cpu),
        }

    def __enter__(self: Cluster[Sync]) -> Cluster[Sync]:
        return self.sync(self.__aenter__)

    def __exit__(self: Cluster[Sync], *args, **kwargs) -> None:
        return self.sync(self.__aexit__, *args, **kwargs)

    @overload
    def get_logs(self: Cluster[Sync], scheduler: bool, workers: bool = True) -> dict:
        ...

    @overload
    def get_logs(
        self: Cluster[Async], scheduler: bool, workers: bool = True
    ) -> Awaitable[dict]:
        ...

    def get_logs(
        self, scheduler: bool = True, workers: bool = True
    ) -> Union[dict, Awaitable[dict]]:
        """Return logs for the scheduler and workers
        Parameters
        ----------
        scheduler : boolean
            Whether or not to collect logs for the scheduler
        workers : boolean
            Whether or not to collect logs for the workers
        Returns
        -------
        logs: Dict[str]
            A dictionary of logs, with one item for the scheduler and one for
            the workers
        """
        return self.sync(self._get_logs, scheduler=scheduler, workers=workers)

    @track_context
    async def _get_logs(self, scheduler: bool = True, workers: bool = True) -> dict:
        if not self.cluster_id:
            raise ValueError("No cluster available for logs!")
        cloud = cast(Cloud[Async], self.cloud)
        return await cloud.cluster_logs(
            cluster_id=self.cluster_id,
            account=self.account,
            scheduler=scheduler,
            workers=workers,
        )

    @property
    def dashboard_link(self):
        # Only use proxied dashboard address if we're in a hosted notebook
        # Otherwise fall back to the non-proxied address
        if self._proxy or dask.config.get("coiled.dashboard.proxy", False):
            return f"{self.cloud.server}/dashboard/{self.cluster_id}/status"
        else:
            return self._dashboard_address
