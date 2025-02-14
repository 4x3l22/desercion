from django.db import models
from django.contrib.auth.hashers import check_password

# Create your models here.
class Modulo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    icono = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Modulo'

class Vista(models.Model):
    id = models.AutoField(primary_key=True)
    modulo_id = models.ForeignKey(Modulo, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    icono = models.TextField(blank=True, null=True)
    ruta = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Vista'

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Rol'
     
class RolVista(models.Model):
    id = models.AutoField(primary_key=True)
    rol_id = models.ForeignKey(Rol, on_delete= models.CASCADE)
    vista_id = models.ForeignKey(Vista, on_delete= models.CASCADE)
    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'RolVista'

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    correo = models.EmailField(unique=True)
    contrasena = models.TextField(blank=True, null=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    documento = models.CharField(max_length=10, unique=True, null=False, blank=False)
    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    def verificar_contasena(self, contrasena):
        return check_password(contrasena, self.contrasena)
    
    class Meta: 
        db_table = 'Usuario'

class UsuarioRol(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_id =models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol_id = models.ForeignKey(Rol, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'UsuarioRol'


class Cuestionario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_cuestionario = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    usuariio_id = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Cuestionario'

class Tipopciones(models.TextChoices):
    ABIERTAS = 'A', 'Abiertas'
    OPCIONMULTIPLE = 'O', 'Opcion multiples'

class Preguntas(models.Model):
    id = models.AutoField(primary_key=True)
    Cuestionario_id = models.ForeignKey(Cuestionario, on_delete= models.CASCADE)
    tipo_pregunta = models.CharField(
        max_length=1,
        choices=Tipopciones.choices
    ) 
    opciones_id = models.ForeignKey(
        'self',
        on_delete= models.CASCADE,
        null=True,
        blank=True,
        related_name= 'opciones'
    )
    textoopciones = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Preguntas'

class Respuestas(models.Model):
    id = models.AutoField(primary_key=True)
    Preguntas_id = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    repuestas = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Respuestas'

class Proceso(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='procesos_creados')
    cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE, related_name='procesos')

    estado_aprobacion = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('coordinador', 'Coordinador'),
            ('bienestar', 'Bienestar'),
            ('finalizado', 'Finalizado')
        ],
        default='pendiente'
    )
    coordinadorfpi = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='procesos_aprobados_fpi')
    comentario_coordinadorfpi = models.TextField(blank=True, null=True)
    fecha_aprobacion_coordinadorfpi = models.DateTimeField(blank=True, null=True)

    coordinador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='procesos_aprobados_cf')
    comentario_coordinador = models.TextField(blank=True, null=True)
    fecha_aprobacion_coordinador = models.DateTimeField(blank=True, null=True)

    bienestar = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='procesos_aprobados_bienestar')
    comentario_bienestar = models.TextField(blank=True, null=True)
    fecha_aprobacion_bienestar = models.DateTimeField(blank=True, null=True)

    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Proceso'

class Deserciones(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cuestionario_id = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Deserciones'

class RecuperarContrasena(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10)
    expiracion = models.DateTimeField(blank=True, null=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    usado = models.BooleanField(default=False)

    class Meta:
        db_table = 'RecuperarContrasena'