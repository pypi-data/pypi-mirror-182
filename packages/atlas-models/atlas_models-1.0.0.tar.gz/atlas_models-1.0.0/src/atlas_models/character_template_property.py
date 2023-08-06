from typing import Union

from atlas_flask_utils.db_utils.db_handlers import global_session
from atlas_flask_utils.db_utils.helper_models.item import Item


class CharacterTemplateProperty(Item):
    __tablename__ = 'CharacterTemplateProperty'

    name: Union[str, global_session.Column] = global_session.Column('Name', global_session.String)
    property_type: Union[str, global_session.Column] = global_session.Column('PropertyType', global_session.String)
    character_template_id: Union[int, global_session.Column] = global_session.Column('CharacterTemplateId',
                                                                                     global_session.ForeignKey('CharacterTemplate.Id'))

    def __init__(self, name: str, property_type: str, character_template_id: int = None, property_id: int = None,
                 **kwargs):
        super(CharacterTemplateProperty, self).__init__(property_id)
        self.name = name
        self.property_type = property_type
        self.character_template_id = character_template_id

    def _serialize(self) -> dict:
        return {
            'name': self.name,
            'propertyType': self.property_type,
            'characterTemplateId': self.character_template_id
        }
