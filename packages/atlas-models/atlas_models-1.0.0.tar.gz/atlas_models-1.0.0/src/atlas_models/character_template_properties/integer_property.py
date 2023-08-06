from typing import Any

from .base_property import BaseProperty


class IntegerProperty(BaseProperty):
    def is_type(self) -> bool:
        if isinstance(self.value, int):
            return True

        try:
            int(self.value)
        except TypeError:
            return False
        else:
            return True

    def convert_string_value_to_type(self) -> Any:
        return int(self.value)

    @staticmethod
    def get_default_value() -> Any:
        return 0
