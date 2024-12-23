from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=254,)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_registro = models.DateTimeField(db_column="fecha", auto_now_add=True)


class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil')
    genero = models.CharField(max_length=10)
    edad = models.PositiveIntegerField()
    ubicacion = models.TextField()
    biografia = models.TextField()


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    premiun = models.BooleanField()
    principal = models.BooleanField()


class ServicioExtra(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    disponible = models.BooleanField()

class Propiedad(models.Model):
    titulo = models.CharField(max_length=200, editable=False)
    direccion = models.CharField(max_length=200)
    precio_por_noche = models.IntegerField()
    max_usuarios = models.PositiveIntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='propiedades')
    categoria = models.ManyToManyField(Categoria, through='CategoriaPrincipal', related_name='propiedades')
    servicios_extra = models.ManyToManyField(ServicioExtra, related_name='propiedades')

class Prioridad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True)
    premiun = models.BooleanField()
    numero = models.IntegerField()
    propiedades = models.ManyToManyField(Propiedad, related_name='prioridades')

class Pago(models.Model):
    total = models.FloatField(help_text="Total del pago")
    fecha_pago = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50)
    cod_transaccion = models.CharField(max_length=100)

class Reserva(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateTimeField()
    total = models.FloatField()
    estado = models.CharField(max_length=20)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name='reservas')
    pago = models.OneToOneField(Pago, on_delete=models.CASCADE, related_name='reserva_pago', null=True, blank=True)
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, related_name='reserva')

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField() 
    valoracion = models.IntegerField()
    anonimo = models.BooleanField()
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name='comentarios')


class CategoriaPrincipal(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_principal')
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name='categoria_principal')
