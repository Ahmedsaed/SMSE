from pathlib import Path
from typing import Any, Dict, Union

from smse.pipelines.base import BasePipeline


# Multimodal Pipeline
class MultimodalPipeline:
    def __init__(self, pipelines: Dict[str, BasePipeline]):
        self.pipelines = pipelines

    def process(self, inputs: Dict[str, Union[str, Path, Any]]) -> Dict[str, Any]:
        """Process multiple modalities"""
        results = {}
        for data_type, input_data in inputs.items():
            if data_type in self.pipelines:
                results[data_type] = self.pipelines[data_type](input_data)
            else:
                raise ValueError(f"No pipeline configured for data type: {data_type}")
        return results
