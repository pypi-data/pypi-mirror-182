from abc import ABC, abstractmethod
from math import isfinite
from typing import (
    Any,
    AsyncIterable,
    Dict,
    Generic,
    Tuple,
    Type,
    TypeVar,
    Optional,
    Collection,
    List,
)

from kilroy_server_py_utils import Observable

DataType = TypeVar("DataType")
MetricType = TypeVar("MetricType", bound="Metric")


class Metric(Generic[DataType], ABC):
    _observable: Observable[Tuple[int, DataType]]

    def __init__(self, observable: Observable[Tuple[int, DataType]]) -> None:
        super().__init__()
        self._observable = observable

    @classmethod
    async def create(cls: Type[MetricType], *args, **kwargs) -> MetricType:
        return cls(*args, observable=await Observable.build(), **kwargs)

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def label(self) -> str:
        pass

    @property
    @abstractmethod
    def tags(self) -> List[str]:
        return []

    @property
    @abstractmethod
    def config(self) -> Dict[str, Any]:
        pass

    async def report_data(self, data: DataType, dataset: int = 0) -> None:
        await self._observable.set((dataset, data))

    async def cleanup(self) -> None:
        await self._observable.cleanup()

    async def watch(self) -> AsyncIterable[Tuple[int, DataType]]:
        async for dataset_id, data in self._observable.subscribe():
            yield dataset_id, data


class StandardMetric(Metric[Dict[str, Any]], ABC):
    def __init__(
        self,
        observable: Observable[Tuple[int, Dict[str, Any]]],
        name: str,
        label: str,
        type: str,
        x_axis_key: str,
        x_axis_label: str,
        y_axis_key: str,
        y_axis_label: str,
        tags: Optional[List[str]] = None,
    ) -> None:
        self._name = name
        self._label = label
        self._type = type
        self._x_axis_key = x_axis_key
        self._x_axis_label = x_axis_label
        self._y_axis_key = y_axis_key
        self._y_axis_label = y_axis_label
        self._tags = tags or []
        super().__init__(observable)

    @property
    def name(self) -> str:
        return self._name

    @property
    def label(self) -> str:
        return self._label

    @property
    def tags(self) -> List[str]:
        return self._tags

    @property
    def config(self) -> Dict[str, Any]:
        return {
            "type": self._type,
            "data": {"datasets": [{"label": self._label, "data": []}]},
            "options": {
                "parsing": {
                    "xAxisKey": self._x_axis_key,
                    "yAxisKey": self._y_axis_key,
                },
                "scales": {
                    "x": {"title": {"text": self._x_axis_label}},
                    "y": {"title": {"text": self._y_axis_label}},
                },
            },
        }

    async def report_data(
        self, data: Dict[str, Any], dataset: int = 0
    ) -> None:
        await self._observable.set((dataset, data))

    async def report(self, x: float, y: float) -> None:
        await self.report_data(
            {
                self._x_axis_key: x if isfinite(x) else None,
                self._y_axis_key: y if isfinite(y) else None,
            }
        )

    async def cleanup(self) -> None:
        await self._observable.cleanup()

    async def watch(self) -> AsyncIterable[Tuple[int, Dict[str, Any]]]:
        async for dataset_id, data in self._observable.subscribe():
            yield dataset_id, data


class Metrizable(ABC):
    @abstractmethod
    async def get_metrics(self) -> Collection[Metric]:
        pass
