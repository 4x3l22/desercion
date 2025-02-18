from datetime import datetime

class BaseService:
    dao = None  # Se debe definir en la subclase
    model = None  # Se debe definir en la subclase

    @classmethod
    def crear(cls, **kwargs):
        obj = cls.model(**kwargs)
        obj.save()
        return obj

    @classmethod
    def obtener_por_id(cls, id):
        return cls.dao.obtener_por_id(id)

    @classmethod
    def actualizar(cls, id, **kwargs):
        obj = cls.obtener_por_id(id)
        if obj:
            for key, value in kwargs.items():
                setattr(obj, key, value)
            obj.fechaModifico = datetime.now()
            obj.save()
            return obj
        return None

    @classmethod
    def eliminar(cls, id):
        obj = cls.obtener_por_id(id)
        if obj:
            obj.fechaElimino = datetime.now()
            obj.save()
            return True
        return False

    @classmethod
    def obtener_activos(cls):
        return cls.model.objects.filter(estado=True)
