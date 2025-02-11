from appdesercion.Business.base_service import BaseService
from appdesercion.models import Deserciones


class DesercionesService(BaseService):
    model=Deserciones
    dao=Deserciones