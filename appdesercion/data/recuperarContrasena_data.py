from appdesercion.Entity.Dao.recuperarcontrasena_dao import RecuperarContrasenaDAO
from appdesercion.Entity.Dto.recuperarcontrasena_dto import RecuperarContrasenaDTO
from appdesercion.data.baseData import BaseData


class RecuperarContrasenaData(BaseData):
    dao=RecuperarContrasenaDAO
    dto_class=RecuperarContrasenaDTO