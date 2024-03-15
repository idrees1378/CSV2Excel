"""
For mapping dict external dict keys to custom keys
"""
from collections.abc import Mapping
from typing import Iterator, TypeVar
from enum import Enum

from src.mappings.maps import WDChangeJobMap

KT = TypeVar('KT')
VT = TypeVar('VT')

class KeysGroup(Enum):
    """
        Enum to represent key groups to be mapped on to
    """
    JOB_CHANGE = 1
    COMPENSATION = 2

class Map(Mapping):
    """
    This class maps Change job csv to workday xlsx file header
    """
    def __init__(self, data: dict[KT, VT], keys_group: KeysGroup):
        self.data = data
        self.keys_group = keys_group

    @property
    def wdmap(self) -> dict[KT: VT]:
        """
            create a new instance of this class with mapped keys
        """
        mapping = {self.__keys_map(key, self.keys_group): value for key, value in self.data.items()}
        return self.__class__(mapping, self.keys_group)

    def __getitem__(self, __key: KT) -> VT:
        return self.data[__key]

    def __iter__(self) -> Iterator:
        return iter(self.data)

    def __len__(self) -> int:
        return len(self.data)

    def __keys_map(self, key: KT, key_group: KeysGroup):
        if key_group == KeysGroup.JOB_CHANGE:
            return WDChangeJobMap[key]
        return key
