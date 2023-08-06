from typing import Any

from .base_property import BaseProperty


class FloatProperty(BaseProperty):
    def is_type(self) -> bool:
        if isinstance(self.value, float) or isinstance(self.value, int):
            return True

        try:
            float(self.value)
        except TypeError:
            return False
        else:
            return True

    def convert_string_value_to_type(self) -> Any:
        return float(self.value)

    @staticmethod
    def get_default_value() -> Any:
        return 0
