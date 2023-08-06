from typing import Union

from atlas_flask_utils.db_utils.db_handlers import global_session
from atlas_flask_utils.db_utils.helper_models.item import Item


class CharacterTemplate(Item):
    __tablename__ = 'CharacterTemplate'

    name: Union[str, global_session.Column] = global_session.Column('Name', global_session.String)

    def __init__(self, name: str, template_id: int = None):
        super(CharacterTemplate, self).__init__(template_id)
        self.name = name

    def _serialize(self) -> dict:
        return {
            'name': self.name
        }
