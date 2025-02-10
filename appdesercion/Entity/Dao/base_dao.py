from django.db import models

class BaseDAO:
    model = None  # Se debe definir en la subclase

    @classmethod
    def obtener_datos(cls):
        return cls.model.objects.all()
    
    @classmethod
    def obtener_por_id(cls, id):
        return cls.model.objects.filter(id=id).first()
    
    @classmethod
    def crear(cls, **kwargs):
        instancia = cls.model(**kwargs)
        instancia.save()
        return instancia
    
    @classmethod
    def actualizar(cls, objeto_id, **kwargs):
        cls.model.objects.filter(id=objeto_id).update(**kwargs)
    
    @classmethod
    def eliminar(cls, objeto_id):
        cls.model.objects.filter(id=objeto_id).delete()