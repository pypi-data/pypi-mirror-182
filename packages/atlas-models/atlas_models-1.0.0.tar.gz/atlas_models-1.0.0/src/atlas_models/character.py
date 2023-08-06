from typing import Union

from atlas_flask_utils.db_utils.db_handlers import global_session
from atlas_flask_utils.db_utils.helper_models.item import Item


class Character(Item):
    __tablename__ = 'Character'

    user_id: Union[int, global_session.Column] = global_session.Column('UserId', global_session.Integer)
    name: Union[str, global_session.Column] = global_session.Column('Name', global_session.String)
    character_template_id: Union[int, global_session.Column] = global_session.Column('CharacterTemplateId',
                                                                                     global_session.ForeignKey('CharacterTemplate.Id'))

    def __init__(self, user_id: int, name: str, character_template_id: int, character_id: int = None):
        super(Character, self).__init__(character_id)
        self.user_id = user_id
        self.name = name
        self.character_template_id = character_template_id

    def _serialize(self) -> dict:
        return {
            'userId': self.user_id,
            'name': self.name,
            'characterTemplateId': self.character_template_id
        }
