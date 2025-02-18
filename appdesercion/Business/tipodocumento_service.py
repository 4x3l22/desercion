from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.tipodocumento_dao import TipoDocumentoDAO
from appdesercion.models import TipoDocumento


class TipoDocumentoService(BaseService):
    DAO = TipoDocumentoDAO
    model = TipoDocumento