from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.persona_dao import PersonaDAO
from appdesercion.models import Persona


class PersonaService(BaseService):
    model=Persona
    dao=PersonaDAO