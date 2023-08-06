from abc import ABC, abstractmethod
from typing import Any


class BaseProperty(ABC):
    def __init__(self, value: Any):
        self.value = value

    @abstractmethod
    def is_type(self) -> bool:
        pass

    @abstractmethod
    def convert_string_value_to_type(self) -> Any:
        pass

    @staticmethod
    @abstractmethod
    def get_default_value() -> Any:
        pass
