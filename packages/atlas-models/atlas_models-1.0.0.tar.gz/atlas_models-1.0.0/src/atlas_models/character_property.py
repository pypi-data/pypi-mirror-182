from typing import Any, Union
from atlas_flask_utils.db_utils.db_handlers import global_session
from atlas_flask_utils.db_utils.helper_models.item import Item

from .character_template_properties.character_template_property_types import property_map
from .character_template_property import CharacterTemplateProperty


class CharacterProperty(Item):
    __tablename__ = 'CharacterProperty'

    character_template_property_id: Union[int, global_session.Column] = global_session.Column('CharacterTemplatePropertyId',
                                                                                              global_session.ForeignKey('CharacterTemplateProperty.Id'))
    __character_template_property: CharacterTemplateProperty = global_session.relationship('CharacterTemplateProperty')
    character_id: Union[int, global_session.Column] = global_session.Column('CharacterId',
                                                                            global_session.ForeignKey('Character.Id'))
    __value: Union[Any, global_session.Column] = global_session.Column('Value', global_session.String)

    def __init__(self, character_template_property_id: int, character_id: int, value: Any,
                 character_property_id: int = None):
        super(CharacterProperty, self).__init__(character_property_id)
        self.character_template_property_id = character_template_property_id
        self.character_id = character_id
        self.value = value

    @property
    def value(self):
        return property_map[self.__character_template_property.property_type](self.__value).convert_string_value_to_type()

    @value.setter
    def value(self, value: Any):
        self.__value = value

    def _serialize(self):
        return {
            'characterTemplatePropertyId': self.character_template_property_id,
            'characterId': self.character_id,
            'value': self.value
        }
