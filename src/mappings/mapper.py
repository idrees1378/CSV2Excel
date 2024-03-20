"""
For mapping dict external dict keys to custom keys
"""
from collections.abc import Mapping
from typing import Iterator, TypeVar

from src.constants import (
    BusinessProcessType,
    BusinessProcessTypeToMappping,
)
from src.eib_builder_logger import EibBuilderLogger

KT = TypeVar("KT")
VT = TypeVar("VT")
logger = EibBuilderLogger()


class Map(Mapping):
    """
    This class maps Change job csv to workday xlsx file header
    """

    def __init__(self, data: dict[KT, VT]):
        self.data = data

    def wdmap(
        self, process_type: BusinessProcessType = BusinessProcessType.CHANGE_JOB
    ) -> dict[KT, VT]:
        """
        create a new instance of this class with mapped keys
        """
        mapping = {
            self.__keys_map(key, process_type): value
            for key, value in self.data.items()
        }
        return self.__class__(mapping)

    def __getitem__(self, __key: KT) -> VT:
        return self.data[__key]

    def __iter__(self) -> Iterator:
        return iter(self.data)

    def __len__(self) -> int:
        return len(self.data)

    def __keys_map(self, key: KT, process_type: BusinessProcessType):
        try:
            return BusinessProcessTypeToMappping[process_type][key]
        except Exception:
            return None
