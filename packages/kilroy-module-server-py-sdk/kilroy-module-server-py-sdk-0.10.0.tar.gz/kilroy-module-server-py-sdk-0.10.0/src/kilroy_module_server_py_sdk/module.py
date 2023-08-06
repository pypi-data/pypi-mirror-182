from abc import ABC, abstractmethod
from pathlib import Path
from typing import (
    Any,
    AsyncIterable,
    Dict,
    Generic,
    Tuple,
    TypeVar,
    Collection,
)

from kilroy_module_py_shared import Metadata
from kilroy_module_server_py_sdk.metrics import Metric, Metrizable
from kilroy_server_py_utils import Configurable, classproperty
from kilroy_server_py_utils.schema import JSONSchema

StateType = TypeVar("StateType")


class Module(Metrizable, Configurable[StateType], ABC, Generic[StateType]):
    # noinspection PyMethodParameters
    @classproperty
    @abstractmethod
    def metadata(cls) -> Metadata:
        pass

    # noinspection PyMethodParameters
    @classproperty
    @abstractmethod
    def post_schema(cls) -> JSONSchema:
        pass

    @abstractmethod
    async def get_metrics(self) -> Collection[Metric]:
        pass

    @abstractmethod
    def generate(
        self, n: int
    ) -> AsyncIterable[Tuple[Dict[str, Any], Dict[str, Any]]]:
        pass

    @abstractmethod
    async def fit_supervised(
        self, data: AsyncIterable[Tuple[Dict[str, Any], float]]
    ) -> None:
        pass

    @abstractmethod
    async def fit_reinforced(
        self, data: AsyncIterable[Tuple[Dict[str, Any], Dict[str, Any], float]]
    ) -> None:
        pass

    async def cleanup(self) -> None:
        metrics = await self.get_metrics()
        for metric in metrics:
            await metric.cleanup()

    async def reset_self(self) -> None:
        await self.cleanup()
        await self.init()

    async def save_self(self, directory: Path) -> None:
        await self.save(directory)
