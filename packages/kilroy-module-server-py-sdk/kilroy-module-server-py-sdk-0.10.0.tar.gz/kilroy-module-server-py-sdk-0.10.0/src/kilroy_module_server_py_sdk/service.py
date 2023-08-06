import json
from pathlib import Path
from typing import AsyncIterator, Dict, AsyncIterable, Tuple, Any

import aiostream
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase
from grpclib import server

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
    MetricConfig,
    ResetRequest,
    ResetResponse,
    SetConfigRequest,
    SetConfigResponse,
    Status,
    WatchConfigRequest,
    WatchConfigResponse,
    WatchMetricsRequest,
    WatchMetricsResponse,
    WatchStatusRequest,
    WatchStatusResponse,
    SaveRequest,
    SaveResponse,
    FitSupervisedRequest,
    FitSupervisedResponse,
    FitReinforcedRequest,
    FitReinforcedResponse,
)
from kilroy_module_server_py_sdk import Metric, Module


class ModuleServiceBase(ServiceBase):
    async def get_metadata(
        self, get_metadata_request: "GetMetadataRequest"
    ) -> "GetMetadataResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_post_schema(
        self, get_post_schema_request: "GetPostSchemaRequest"
    ) -> "GetPostSchemaResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_status(
        self, get_status_request: "GetStatusRequest"
    ) -> "GetStatusResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def watch_status(
        self, watch_status_request: "WatchStatusRequest"
    ) -> AsyncIterator["WatchStatusResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_config_schema(
        self, get_config_schema_request: "GetConfigSchemaRequest"
    ) -> "GetConfigSchemaResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_config(
        self, get_config_request: "GetConfigRequest"
    ) -> "GetConfigResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def watch_config(
        self, watch_config_request: "WatchConfigRequest"
    ) -> AsyncIterator["WatchConfigResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def set_config(
        self, set_config_request: "SetConfigRequest"
    ) -> "SetConfigResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def generate(
        self, generate_request: "GenerateRequest"
    ) -> AsyncIterator["GenerateResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def fit_supervised(
        self,
        fit_supervised_request_iterator: AsyncIterator["FitSupervisedRequest"],
    ) -> "FitSupervisedResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def fit_reinforced(
        self,
        fit_reinforced_request_iterator: AsyncIterator["FitReinforcedRequest"],
    ) -> "FitReinforcedResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_metrics_config(
        self, get_metrics_config_request: "GetMetricsConfigRequest"
    ) -> "GetMetricsConfigResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def watch_metrics(
        self, watch_metrics_request: "WatchMetricsRequest"
    ) -> AsyncIterator["WatchMetricsResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def reset(self, reset_request: "ResetRequest") -> "ResetResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def save(self, save_request: "SaveRequest") -> "SaveResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_get_metadata(
        self,
        stream: "grpclib.server.Stream[GetMetadataRequest, GetMetadataResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_metadata(request)
        await stream.send_message(response)

    async def __rpc_get_post_schema(
        self,
        stream: "grpclib.server.Stream[GetPostSchemaRequest, GetPostSchemaResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_post_schema(request)
        await stream.send_message(response)

    async def __rpc_get_status(
        self,
        stream: "grpclib.server.Stream[GetStatusRequest, GetStatusResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_status(request)
        await stream.send_message(response)

    async def __rpc_watch_status(
        self,
        stream: "grpclib.server.Stream[WatchStatusRequest, WatchStatusResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.watch_status,
            stream,
            request,
        )

    async def __rpc_get_config_schema(
        self,
        stream: "grpclib.server.Stream[GetConfigSchemaRequest, GetConfigSchemaResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_config_schema(request)
        await stream.send_message(response)

    async def __rpc_get_config(
        self,
        stream: "grpclib.server.Stream[GetConfigRequest, GetConfigResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_config(request)
        await stream.send_message(response)

    async def __rpc_watch_config(
        self,
        stream: "grpclib.server.Stream[WatchConfigRequest, WatchConfigResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.watch_config,
            stream,
            request,
        )

    async def __rpc_set_config(
        self,
        stream: "grpclib.server.Stream[SetConfigRequest, SetConfigResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.set_config(request)
        await stream.send_message(response)

    async def __rpc_generate(
        self,
        stream: "grpclib.server.Stream[GenerateRequest, GenerateResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.generate,
            stream,
            request,
        )

    async def __rpc_fit_supervised(
        self,
        stream: "grpclib.server.Stream[FitSupervisedRequest, FitSupervisedResponse]",
    ) -> None:
        request = stream.__aiter__()
        response = await self.fit_supervised(request)
        await stream.send_message(response)

    async def __rpc_fit_reinforced(
        self,
        stream: "grpclib.server.Stream[FitReinforcedRequest, FitReinforcedResponse]",
    ) -> None:
        request = stream.__aiter__()
        response = await self.fit_reinforced(request)
        await stream.send_message(response)

    async def __rpc_get_metrics_config(
        self,
        stream: "grpclib.server.Stream[GetMetricsConfigRequest, GetMetricsConfigResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_metrics_config(request)
        await stream.send_message(response)

    async def __rpc_watch_metrics(
        self,
        stream: "grpclib.server.Stream[WatchMetricsRequest, WatchMetricsResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.watch_metrics,
            stream,
            request,
        )

    async def __rpc_reset(
        self, stream: "grpclib.server.Stream[ResetRequest, ResetResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.reset(request)
        await stream.send_message(response)

    async def __rpc_save(
        self, stream: "grpclib.server.Stream[SaveRequest, SaveResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.save(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/kilroy.module.v1alpha.ModuleService/GetMetadata": grpclib.const.Handler(
                self.__rpc_get_metadata,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetMetadataRequest,
                GetMetadataResponse,
            ),
            "/kilroy.module.v1alpha.ModuleService/GetPostSchema": grpclib.const.Handler(
                self.__rpc_get_post_schema,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetPostSchemaRequest,
                GetPostSchemaResponse,
            ),
            "/kilroy.module.v1alpha.ModuleService/GetStatus": grpclib.const.Handler(
                self.__rpc_get_status,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetStatusRequest,
                GetStatusResponse,
            ),
            "/kilroy.module.v1alpha.ModuleService/WatchStatus": grpclib.const.Handler(
                self.__rpc_watch_status,
                grpclib.const.Cardinality.UNARY_STREAM,
                WatchStatusRequest,
                WatchStatusResponse,
            ),
            "/kilroy.module.v1alpha.ModuleService/GetConfigSchema": grpclib.const.Handler(
                self.__rpc_get_config_schema,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetConfigSchemaRequest,
                GetConfigSchemaResponse,
            ),
            "/kilroy.module.v1alpha.ModuleService/GetConfig": grpclib.const.Handler(
                self.__rpc_get_config,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetConfigRequest,
                GetConfigResponse,
            ),
            "/kilroy.module.v1alpha.ModuleService/WatchConfig": grpclib.const.Handler(
                self.__rpc_watch_config,
                grpclib.const.Cardinality.UNARY_STREAM,
                WatchConfigRequest,
                WatchConfigResponse,
            ),
            "/kilroy.module.v1alpha.ModuleService/SetConfig": grpclib.const.Handler(
                self.__rpc_set_config,
                grpclib.const.Cardinality.UNARY_UNARY,
                SetConfigRequest,
                SetConfigResponse,
            ),
            "/kilroy.module.v1alpha.ModuleService/Generate": grpclib.const.Handler(
                self.__rpc_generate,
                grpclib.const.Cardinality.UNARY_STREAM,
                GenerateRequest,
                GenerateResponse,
            ),
            "/kilroy.module.v1alpha.ModuleService/FitSupervised": grpclib.const.Handler(
                self.__rpc_fit_supervised,
                grpclib.const.Cardinality.STREAM_UNARY,
                FitSupervisedRequest,
                FitSupervisedResponse,
            ),
            "/kilroy.module.v1alpha.ModuleService/FitReinforced": grpclib.const.Handler(
                self.__rpc_fit_reinforced,
                grpclib.const.Cardinality.STREAM_UNARY,
                FitReinforcedRequest,
                FitReinforcedResponse,
            ),
            "/kilroy.module.v1alpha.ModuleService/GetMetricsConfig": grpclib.const.Handler(
                self.__rpc_get_metrics_config,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetMetricsConfigRequest,
                GetMetricsConfigResponse,
            ),
            "/kilroy.module.v1alpha.ModuleService/WatchMetrics": grpclib.const.Handler(
                self.__rpc_watch_metrics,
                grpclib.const.Cardinality.UNARY_STREAM,
                WatchMetricsRequest,
                WatchMetricsResponse,
            ),
            "/kilroy.module.v1alpha.ModuleService/Reset": grpclib.const.Handler(
                self.__rpc_reset,
                grpclib.const.Cardinality.UNARY_UNARY,
                ResetRequest,
                ResetResponse,
            ),
            "/kilroy.module.v1alpha.ModuleService/Save": grpclib.const.Handler(
                self.__rpc_save,
                grpclib.const.Cardinality.UNARY_UNARY,
                SaveRequest,
                SaveResponse,
            ),
        }


class ModuleService(ModuleServiceBase):
    def __init__(self, module: Module, state_directory: Path) -> None:
        super().__init__()
        self._module = module
        self._state_directory = state_directory

    async def get_metadata(
        self, get_metadata_request: "GetMetadataRequest"
    ) -> "GetMetadataResponse":
        metadata = self._module.metadata
        return GetMetadataResponse().from_dict(
            {
                "key": metadata.key,
                "description": metadata.description,
            }
        )

    async def get_post_schema(
        self, get_post_schema_request: "GetPostSchemaRequest"
    ) -> "GetPostSchemaResponse":
        schema = self._module.post_schema
        return GetPostSchemaResponse().from_dict({"schema": schema.json()})

    async def get_status(
        self, get_status_request: "GetStatusRequest"
    ) -> "GetStatusResponse":
        ready = await self._module.state.ready.fetch()
        status = Status.STATUS_READY if ready else Status.STATUS_LOADING
        return GetStatusResponse().from_dict({"status": status})

    async def watch_status(
        self, watch_status_request: "WatchStatusRequest"
    ) -> AsyncIterator["WatchStatusResponse"]:
        async for ready in self._module.state.ready.subscribe():
            status = Status.STATUS_READY if ready else Status.STATUS_LOADING
            yield WatchStatusResponse().from_dict({"status": status})

    async def get_config_schema(
        self, get_config_schema_request: "GetConfigSchemaRequest"
    ) -> "GetConfigSchemaResponse":
        schema = self._module.schema
        return GetConfigSchemaResponse().from_dict({"schema": schema.json()})

    async def get_config(
        self, get_config_request: "GetConfigRequest"
    ) -> "GetConfigResponse":
        config = await self._module.config.json.fetch()
        return GetConfigResponse().from_dict({"config": json.dumps(config)})

    async def watch_config(
        self, watch_config_request: "WatchConfigRequest"
    ) -> AsyncIterator["WatchConfigResponse"]:
        async for config in self._module.config.json.subscribe():
            yield WatchConfigResponse().from_dict(
                {"config": json.dumps(config)}
            )

    async def set_config(
        self, set_config_request: "SetConfigRequest"
    ) -> "SetConfigResponse":
        config = json.loads(set_config_request.config)
        config = await self._module.config.set(config)
        return SetConfigResponse().from_dict({"config": json.dumps(config)})

    async def generate(
        self, generate_request: "GenerateRequest"
    ) -> AsyncIterator["GenerateResponse"]:
        async for content, metadata in self._module.generate(
            generate_request.quantity
        ):
            yield GenerateResponse(
                content=json.dumps(content), metadata=json.dumps(metadata)
            )

    async def fit_supervised(
        self,
        fit_supervised_request_iterator: AsyncIterator["FitSupervisedRequest"],
    ) -> "FitSupervisedResponse":
        async def __to_data(
            it: AsyncIterator["FitSupervisedRequest"],
        ) -> AsyncIterable[Tuple[Dict[str, Any], float]]:
            async for request in it:
                yield json.loads(request.content), request.score

        await self._module.fit_supervised(
            __to_data(fit_supervised_request_iterator)
        )
        return FitSupervisedResponse()

    async def fit_reinforced(
        self,
        fit_reinforced_request_iterator: AsyncIterator["FitReinforcedRequest"],
    ) -> "FitReinforcedResponse":
        async def __to_data(
            it: AsyncIterator["FitReinforcedRequest"],
        ) -> AsyncIterable[Tuple[Dict[str, Any], Dict[str, Any], float]]:
            async for request in it:
                yield (
                    json.loads(request.content),
                    json.loads(request.metadata),
                    request.score,
                )

        await self._module.fit_reinforced(
            __to_data(fit_reinforced_request_iterator)
        )
        return FitReinforcedResponse()

    async def get_metrics_config(
        self, get_metrics_config_request: "GetMetricsConfigRequest"
    ) -> "GetMetricsConfigResponse":
        configs = [
            MetricConfig().from_dict(
                {
                    "id": metric.name,
                    "label": metric.label,
                    "config": json.dumps(metric.config),
                    "tags": metric.tags,
                }
            )
            for metric in await self._module.get_metrics()
        ]
        return GetMetricsConfigResponse(configs=configs)

    async def watch_metrics(
        self, watch_metrics_request: "WatchMetricsRequest"
    ) -> AsyncIterator["WatchMetricsResponse"]:
        async def converted(
            metric: Metric,
        ) -> AsyncIterator["WatchMetricsResponse"]:
            async for dataset_id, data in metric.watch():
                yield WatchMetricsResponse().from_dict(
                    {
                        "metric_id": metric.name,
                        "dataset_id": dataset_id,
                        "data": json.dumps(data),
                    }
                )

        combine = aiostream.stream.merge(
            *(converted(metric) for metric in await self._module.get_metrics())
        )

        async with combine.stream() as streamer:
            async for message in streamer:
                yield message

    async def reset(self, reset_request: "ResetRequest") -> "ResetResponse":
        await self._module.reset_self()
        return ResetResponse()

    async def save(self, save_request: "SaveRequest") -> "SaveResponse":
        await self._module.save_self(self._state_directory)
        return SaveResponse()
