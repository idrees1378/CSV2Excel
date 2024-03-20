from __future__ import annotations

import csvfile

from src.eib_builder import BusinessProcessType
from src.mappings.mapper import Map


class LoadInputData:
    def __init__(self, data_path):
        self.data_path = data_path

    @classmethod
    def load_csv(cls, file_name: str) -> list[Map]:
        """
        loads csv file and converts it into a list of objects
        e.g
        [
            {"key1": "{row1.col1}", "key2": "{row1.col1}"},
            {"key1": "{row2.col1}", "key2": "{row2.col1}"},
            ...
        ]
        """

        return [Map(row) for row in csvfile.load(file_name)]

    @classmethod
    def load_json(
        cls,
        json_string: str,
        process_type: BusinessProcessType = BusinessProcessType.CHANGE_JOB,
    ) -> None:
        """
        loads json file and converts it into a list of objects
        e.g
        [
            {"key1": "{row1.col1}", "key2": "{row1.col1}"},
            {"key1": "{row2.col1}", "key2": "{row2.col1}"},
            ...
        ]
        """
        pass
