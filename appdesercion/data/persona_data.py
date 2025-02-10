from appdesercion.Entity.Dao.persona_dao import PersonaDAO
from appdesercion.Entity.Dto.persona_dto import PersonaDTO
from appdesercion.data.baseData import BaseData


class PersonaData(BaseData):
    dao=PersonaDAO
    dto_class=PersonaDTO