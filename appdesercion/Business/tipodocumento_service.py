from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.tipodocumento_dao import TipoDocumentoDAO
from appdesercion.Entity.Dto.tipodocumento_dto import TipoDocumentoDTO


class TipoDocumentoService(BaseService):
    DAO = TipoDocumentoDAO
    model = TipoDocumentoDTO