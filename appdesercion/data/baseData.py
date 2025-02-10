from datetime import datetime

class BaseData:
    dao = None  # Se debe definir en la subclase
    dto_class = None  # Se debe definir en la subclase

    @classmethod
    def obtener_datos(cls):
        objetos = cls.dao.obtener_datos()
        return [cls.dto_class(
            **{campo: getattr(obj, campo) for campo in cls.dto_class.__annotations__.keys()}
        ) for obj in objetos]

    @classmethod
    def obtener_por_id(cls, id):
        obj = cls.dao.obtener_por_id(id)
        if obj:
            return cls.dto_class(
                **{campo: getattr(obj, campo) for campo in cls.dto_class.__annotations__.keys()}
            )
        return None

    @classmethod
    def crear(cls, dto):
        obj = cls.dao.crear(**dto.__dict__)
        return cls.dto_class(
            **{campo: getattr(obj, campo) for campo in cls.dto_class.__annotations__.keys()}
        )

    @classmethod
    def actualizar(cls, id, dto):
        cls.dao.actualizar(id, **dto.__dict__)
        return cls.obtener_por_id(id)

    @classmethod
    def eliminar(cls, id):
        try:
            obj = cls.dao.model.objects.get(id=id)
            obj.estado = False
            obj.fechaElimino = datetime.now()
            obj.save()
            return True
        except cls.dao.model.DoesNotExist:
            return False
