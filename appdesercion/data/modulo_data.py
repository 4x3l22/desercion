from appdesercion.Entity.Dao.modulo_dao import ModuloDAO
from appdesercion.Entity.Dto.modulo_dto import ModuloDTO
from appdesercion.data.baseData import BaseData


class ModuloData(BaseData):

    dao = ModuloDAO
    dto_class = ModuloDTO
    # @staticmethod
    # def obtener_datos():
    #     modulos = ModuloDAO.obtener_datos
    #     return [ModuloDTO(
    #         id=m.id,
    #         nombre=m.nombre,
    #         descripcion=m.descripcion,
    #         icono=m.icono,
    #         estado=m.estado,
    #         fechaCreo=m.fechaCreo,
    #         fechaModifico=m.fechaModifico,
    #         fechaElimino=m.fechaElimino
    #     ) for m in modulos]
    
    # @staticmethod
    # def obtener_por_id():
    #     m = ModuloDAO.obtener_por_id(id)
    #     if m:
    #         return ModuloDTO(
    #             id=m.id,
    #             nombre=m.nombre,
    #             descripcion=m.descripcion,
    #             icono=m.icono,
    #             estado=m.estado,
    #             fechaCreo=m.fechaCreo,
    #             fechaModifico=m.fechaModifico,
    #             fechaElimino=m.fechaElimino
    #         )
    #     return None
    
    # def crear_modulo(dto:ModuloDTO):
    #     modulo = ModuloDAO.crear_modulo(
    #         nombre=dto.nombre,
    #         descripcion=dto.descripcion,
    #         icono=dto.icono,
    #         estado=dto.estado
    #     )
    #     return ModuloDTO(
    #         id=modulo.id,
    #         nombre=modulo.nombre,
    #         descripcion=modulo.descripcion,
    #         icono=modulo.icono,
    #         estado=modulo.estado,
    #         fechaCreo=modulo.fechaCreo,
    #         fechaModifico=modulo.fechaModifico,
    #         fechaElimino=modulo.fechaElimino
    #     )
    
    # @staticmethod
    # def actualizar_modulo(id, dto: ModuloDTO):
    #     ModuloDAO.actualizar_modulo(id, 
    #         nombre=dto.nombre,
    #         descripcion=dto.descripcion,
    #         icono=dto.icono,
    #         estado=dto.estado
    #     )
    #     return ModuloData.obtener_por_id(id)

    # @staticmethod
    # def eliminar_modulo(id):
    #     try:
    #         modulo = Modulo.objects.get(id=id)
    #         modulo.estado = False
    #         modulo.fechaElimino = datetime.now()
    #         modulo.save()
    #         return True
    #     except Modulo.DoesNotExist:
    #         return False