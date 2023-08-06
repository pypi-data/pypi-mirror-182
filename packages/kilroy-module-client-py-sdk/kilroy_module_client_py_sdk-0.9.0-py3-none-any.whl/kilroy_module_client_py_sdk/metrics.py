from typing import Any, Dict, List

from kilroy_module_py_shared import SerializableModel


class MetricConfig(SerializableModel):
    id: str
    label: str
    config: Dict[str, Any]
    tags: List[str]


class MetricData(SerializableModel):
    metric_id: str
    dataset_id: int
    data: Dict[str, Any]
