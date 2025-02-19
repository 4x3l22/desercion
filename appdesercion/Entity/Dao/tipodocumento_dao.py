from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.Entity.Dto.tipodocumento_dto import TipoDocumentoDTO
from appdesercion.models import TipoDocumento


class TipoDocumentoDAO(BaseDAO):
    model = TipoDocumento