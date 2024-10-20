from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField()

class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil')
    
    
    genero = models.CharField(max_length=10)
    edad = models.PositiveIntegerField()
    foto_perfil=models.ImageField
    biografia = models.TextField()

class Propiedad(models.Model):
    titulo = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    precio_por_noche = models.IntegerField()
    max_usuarios = models.PositiveIntegerField()
    
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='propiedades')
    categoria = models.ManyToManyField('Categoria', through='CategoriaPrincipal', related_name='propiedades')
    servicios_extra = models.ManyToManyField('ServicioExtra', related_name='propiedades')
    fotos = models.ManyToManyField('FotoPropiedad', related_name='propiedades')

class Reserva(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    total = models.IntegerField()
    estado = models.CharField(max_length=20)


    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name='reservas')
    pago = models.OneToOneField('Pago', on_delete=models.CASCADE, related_name='reserva_pago', null=True, blank=True)

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    valoracion = models.IntegerField()
    anonimo = models.BooleanField()


    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name='comentarios')

class ServicioExtra(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    disponible = models.BooleanField()

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    icono = models.ImageField(upload_to='iconos/')
    principal = models.BooleanField()

    Propiedad=models.ManyToManyField(Propiedad, related_name='categoria_propiedad')

class CategoriaPrincipal(models.Model):
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    prioridad = models.IntegerField()
    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_principal')
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name='categoria_principal')

class Pago(models.Model):
    total = models.IntegerField()
    fecha_pago = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50)
    cod_transaccion = models.CharField(max_length=100, unique=True)
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE, related_name='pago_reserva')

class FotoPropiedad(models.Model):
    foto = models.ImageField(upload_to='fotos/')
    descripcion = models.TextField()
    orden = models.PositiveIntegerField()
    destacada = models.BooleanField(default=False)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name='fotos_propiedad')

class Prioridad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    propiedades = models.ManyToManyField(Propiedad, related_name='prioridades')
