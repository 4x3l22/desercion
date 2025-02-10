from datetime import datetime
from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.modulo_dao import ModuloDAO
from appdesercion.models import Modulo


class ModuloService(BaseService):

    dao=ModuloDAO
    model=Modulo

    # def crear_modulo(self, nombre, descripcion, icono):
    #     modulo = Modulo(
    #         nombre=nombre,
    #         descripcion=descripcion,
    #         icono=icono,
    #         estado=True
    #     )
    #     modulo.save()
    #     return modulo
    
    # def obtener_modulo_por_id(self, id, nombre=None, descripcion=None, icono=None):
    #     return Modulo.objects.filter(id=id, nombre=None).first()
    
    # def actualizar_modulo(self, id, nombre=None, descripcion=None, icono=None):
    #     modulo = self.obtener_modulo_por_id(id)
    #     if modulo:
    #         if nombre:
    #             modulo.nombre = nombre
    #         if descripcion:
    #             modulo.descripcion = descripcion
    #         if icono:
    #             modulo.icono = icono
    #         modulo.fechaModifico = datetime.now()
    #         modulo.save()
    #         return modulo
    #     return None
    
    # def eliminar_modulo(self, id):
        
    #     modulo = self.obtener_modulo_por_id(id)
    #     if modulo:
    #         modulo.estado = False
    #         modulo.fechaElimino = datetime.now()
    #         modulo.save()
    #         return True
    #     return False
    
    # def obtener_modulos_activos(self):
    #     return Modulo.objects.filter(estado=True)