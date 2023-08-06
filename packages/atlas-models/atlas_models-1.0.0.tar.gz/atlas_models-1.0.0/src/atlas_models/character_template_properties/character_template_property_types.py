from typing import Dict

from .base_property import BaseProperty
from .float_property import FloatProperty
from .integer_property import IntegerProperty
from .string_property import StringProperty


class CharacterTemplatePropertyTypes:
    integer = 'integer'
    float = 'float'
    string = 'string'


property_map: Dict[str, type(BaseProperty)] = {
    CharacterTemplatePropertyTypes.integer: IntegerProperty,
    CharacterTemplatePropertyTypes.float: FloatProperty,
    CharacterTemplatePropertyTypes.string: StringProperty
}
