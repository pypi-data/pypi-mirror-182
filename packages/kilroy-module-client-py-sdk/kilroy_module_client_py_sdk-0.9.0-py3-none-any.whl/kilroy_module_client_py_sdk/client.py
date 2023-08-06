import json
from typing import (
    Any,
    AsyncIterable,
    AsyncIterator,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    Union,
)

import betterproto
from aiostream import stream
from betterproto.grpc.grpclib_client import MetadataLike
from grpclib.metadata import Deadline

from kilroy_module_client_py_sdk.metrics import MetricConfig, MetricData
from kilroy_module_py_shared import (
    GenerateRequest,
    GenerateResponse,
    GetConfigRequest,
    GetConfigResponse,
    GetConfigSchemaRequest,
    GetConfigSchemaResponse,
    GetMetadataRequest,
    GetMetadataResponse,
    GetMetricsConfigRequest,
    GetMetricsConfigResponse,
    GetPostSchemaRequest,
    GetPostSchemaResponse,
    GetStatusRequest,
    GetStatusResponse,
    Metadata,
    SetConfigRequest,
    SetConfigResponse,
    Status,
    WatchConfigRequest,
    WatchConfigResponse,
    WatchMetricsRequest,
    WatchMetricsResponse,
    WatchStatusRequest,
    WatchStatusResponse,
    ResetRequest,
    ResetResponse,
    SaveRequest,
    SaveResponse,
    FitSupervisedRequest,
    FitSupervisedResponse,
    FitReinforcedRequest,
    FitReinforcedResponse,
)


class ModuleServiceStub(betterproto.ServiceStub):
    async def get_metadata(
        self,
        get_metadata_request: "GetMetadataRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "GetMetadataResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/GetMetadata",
            get_metadata_request,
            GetMetadataResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_post_schema(
        self,
        get_post_schema_request: "GetPostSchemaRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "GetPostSchemaResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/GetPostSchema",
            get_post_schema_request,
            GetPostSchemaResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_status(
        self,
        get_status_request: "GetStatusRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "GetStatusResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/GetStatus",
            get_status_request,
            GetStatusResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def watch_status(
        self,
        watch_status_request: "WatchStatusRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> AsyncIterator["WatchStatusResponse"]:
        async for response in self._unary_stream(
            "/kilroy.module.v1alpha.ModuleService/WatchStatus",
            watch_status_request,
            WatchStatusResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def get_config_schema(
        self,
        get_config_schema_request: "GetConfigSchemaRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "GetConfigSchemaResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/GetConfigSchema",
            get_config_schema_request,
            GetConfigSchemaResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_config(
        self,
        get_config_request: "GetConfigRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "GetConfigResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/GetConfig",
            get_config_request,
            GetConfigResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def watch_config(
        self,
        watch_config_request: "WatchConfigRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> AsyncIterator["WatchConfigResponse"]:
        async for response in self._unary_stream(
            "/kilroy.module.v1alpha.ModuleService/WatchConfig",
            watch_config_request,
            WatchConfigResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def set_config(
        self,
        set_config_request: "SetConfigRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "SetConfigResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/SetConfig",
            set_config_request,
            SetConfigResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def generate(
        self,
        generate_request: "GenerateRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> AsyncIterator["GenerateResponse"]:
        async for response in self._unary_stream(
            "/kilroy.module.v1alpha.ModuleService/Generate",
            generate_request,
            GenerateResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def fit_supervised(
        self,
        fit_supervised_request_iterator: Union[
            AsyncIterable["FitSupervisedRequest"],
            Iterable["FitSupervisedRequest"],
        ],
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "FitSupervisedResponse":
        return await self._stream_unary(
            "/kilroy.module.v1alpha.ModuleService/FitSupervised",
            fit_supervised_request_iterator,
            FitSupervisedRequest,
            FitSupervisedResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def fit_reinforced(
        self,
        fit_reinforced_request_iterator: Union[
            AsyncIterable["FitReinforcedRequest"],
            Iterable["FitReinforcedRequest"],
        ],
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "FitReinforcedResponse":
        return await self._stream_unary(
            "/kilroy.module.v1alpha.ModuleService/FitReinforced",
            fit_reinforced_request_iterator,
            FitReinforcedRequest,
            FitReinforcedResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_metrics_config(
        self,
        get_metrics_config_request: "GetMetricsConfigRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "GetMetricsConfigResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/GetMetricsConfig",
            get_metrics_config_request,
            GetMetricsConfigResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def watch_metrics(
        self,
        watch_metrics_request: "WatchMetricsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> AsyncIterator["WatchMetricsResponse"]:
        async for response in self._unary_stream(
            "/kilroy.module.v1alpha.ModuleService/WatchMetrics",
            watch_metrics_request,
            WatchMetricsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def reset(
        self,
        reset_request: "ResetRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "ResetResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/Reset",
            reset_request,
            ResetResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def save(
        self,
        save_request: "SaveRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "SaveResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/Save",
            save_request,
            SaveResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class ModuleService:
    def __init__(self, *args, **kwargs) -> None:
        self._stub = ModuleServiceStub(*args, **kwargs)

    async def get_metadata(self, *args, **kwargs) -> Metadata:
        response = await self._stub.get_metadata(
            GetMetadataRequest(), *args, **kwargs
        )
        return Metadata(key=response.key, description=response.description)

    async def get_post_schema(self, *args, **kwargs) -> Dict[str, Any]:
        response = await self._stub.get_post_schema(
            GetPostSchemaRequest(), *args, **kwargs
        )
        return json.loads(response.schema)

    async def get_status(self, *args, **kwargs) -> Status:
        response = await self._stub.get_status(
            GetStatusRequest(), *args, **kwargs
        )
        return response.status

    async def watch_status(self, *args, **kwargs) -> AsyncIterator[Status]:
        async for response in self._stub.watch_status(
            WatchStatusRequest(), *args, **kwargs
        ):
            yield response.status

    async def get_config_schema(self, *args, **kwargs) -> Dict[str, Any]:
        response = await self._stub.get_config_schema(
            GetConfigSchemaRequest(), *args, **kwargs
        )
        return json.loads(response.schema)

    async def get_config(self, *args, **kwargs) -> Dict[str, Any]:
        response = await self._stub.get_config(
            GetConfigRequest(), *args, **kwargs
        )
        return json.loads(response.config)

    async def watch_config(
        self, *args, **kwargs
    ) -> AsyncIterator[Dict[str, Any]]:
        async for response in self._stub.watch_config(
            WatchConfigRequest(), *args, **kwargs
        ):
            yield json.loads(response.config)

    async def set_config(
        self, config: Dict[str, Any], *args, **kwargs
    ) -> "SetConfigResponse":
        response = await self._stub.set_config(
            SetConfigRequest(config=json.dumps(config)), *args, **kwargs
        )
        return json.loads(response.config)

    async def generate(
        self, quantity: int = 1, *args, **kwargs
    ) -> AsyncIterator[Tuple[Dict[str, Any], Dict[str, Any]]]:
        async for response in self._stub.generate(
            GenerateRequest(quantity=quantity), *args, **kwargs
        ):
            yield json.loads(response.content), json.loads(response.metadata)

    async def fit_supervised(
        self,
        data: Union[
            AsyncIterable[Tuple[Dict[str, Any], float]],
            Iterable[Tuple[Dict[str, Any], float]],
        ],
        *args,
        **kwargs,
    ) -> None:
        async def __to_requests(
            _data: AsyncIterable[Tuple[Dict[str, Any], float]]
        ) -> AsyncIterable[FitSupervisedRequest]:
            async for post, score in _data:
                yield FitSupervisedRequest(
                    content=json.dumps(post), score=score
                )

        async with stream.iterate(data).stream() as data:
            await self._stub.fit_supervised(
                __to_requests(data), *args, **kwargs
            )

    async def fit_reinforced(
        self,
        data: Union[
            AsyncIterable[Tuple[Dict[str, Any], Dict[str, Any], float]],
            Iterable[Tuple[Dict[str, Any], Dict[str, Any], float]],
        ],
        *args,
        **kwargs,
    ) -> None:
        async def __to_requests(
            _data: AsyncIterable[Tuple[Dict[str, Any], Dict[str, Any], float]]
        ) -> AsyncIterable[FitReinforcedRequest]:
            async for content, metadata, score in _data:
                yield FitReinforcedRequest(
                    content=json.dumps(content),
                    metadata=json.dumps(metadata),
                    score=score,
                )

        async with stream.iterate(data).stream() as data:
            await self._stub.fit_reinforced(
                __to_requests(data), *args, **kwargs
            )

    async def get_metrics_config(self, *args, **kwargs) -> List[MetricConfig]:
        response = await self._stub.get_metrics_config(
            GetMetricsConfigRequest(), *args, **kwargs
        )

        return [
            MetricConfig(
                id=metric.id,
                label=metric.label,
                config=json.loads(metric.config),
                tags=metric.tags,
            )
            for metric in response.configs
        ]

    async def watch_metrics(
        self, *args, **kwargs
    ) -> AsyncIterator[MetricData]:
        async for response in self._stub.watch_metrics(
            WatchMetricsRequest(), *args, **kwargs
        ):
            yield MetricData(
                metric_id=response.metric_id,
                dataset_id=response.dataset_id,
                data=json.loads(response.data),
            )

    async def reset(self, *args, **kwargs) -> None:
        await self._stub.reset(ResetRequest(), *args, **kwargs)

    async def save(self, *args, **kwargs) -> None:
        await self._stub.save(SaveRequest(), *args, **kwargs)
