from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.models import TipoDocumento


class TipoDocumentoDAO(BaseDAO):
    model = TipoDocumento