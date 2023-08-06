from typing import Any

from .base_property import BaseProperty


class StringProperty(BaseProperty):
    def is_type(self) -> bool:
        return isinstance(self.value, str)

    def convert_string_value_to_type(self) -> Any:
        return self.value

    @staticmethod
    def get_default_value() -> Any:
        return ''
