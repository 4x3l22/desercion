from django.db import models

# Create your models here.
class Modulo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    icono = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True, null=True)
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
    fechaModifico = models.DateTimeField(auto_now=True, null=True)
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
    fechaModifico = models.DateTimeField(auto_now=True, null=True)
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
    fechaModifico = models.DateTimeField(auto_now=True, null=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'RolVista'

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    documento = models.BigIntegerField(unique=True)
    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True, null=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Persona'

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    persona_id = models.ForeignKey(Persona, on_delete= models.CASCADE)
    correo = models.CharField(max_length=100)
    contrasena = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True, null=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta: 
        db_table = 'Usuario'

class Cuestionario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_cuestionario = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    usuariio_id = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True, null=True)
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
    fechaModifico = models.DateTimeField(auto_now=True, null=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Preguntas'

class Respuestas(models.Model):
    id = models.AutoField(primary_key=True)
    Preguntas_id = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    repuestas = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True, null=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Respuestas'

class Proceso(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Cuestionario_id = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)
    comentarios = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True, null=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Proceso'

class Deserciones(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cuestionario_id = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True, null=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Deserciones'