# ProyectoJorge

Hola Jorge, aqui te explico un poco en lo que consiste cada modelo y atributos de mi pagina web :D


Mi pagina web consiste en una pagina de alquiereles de Airbnb, tanto como los huespedes puedan mirar y elegir las que mas le guste
tanto como las Propietarios puedan ofertar y tal sus Airbnb.

help_text= este parametro sirve para poder aclarar para ayudar el usuario, yo lo uso en total de pago para indicarle que es el total que se va a pagar definitivamente


Usuario(

Este modelo representa a las personas que utilizan la plataforma, tanto como propietarios como inquilinos


    nombre: Pues nombre completo del usuario 

    email: El correo electronico del usuario

    Telefono: EL telefono del usuario  

    Fecha_registro: fecha y hora en el que el usuario se a regristado en la plataforma


        Relaciones

        OneToOne con perfil: Cada usuario tiene un perfil unico
)



Perfil (

    Este modelo se utiliza para almacenar informacion  sobre los usuarios

    genero: el genro del usuario

    edad: edad del usuario

    foto_perfil: pues una foto del usuario

    biografia: una pequeña biografia del usuario

)


Propiedad(

    Este modelo representa a las propiedades que los anfitriones ofrecen, para qjue los inquilinos puedan alojarse

    titulo: titulo de la propiedad

    direccion: direccion de donde se encuentra la propiedad

    precio_por_noche: pues el costo que tiene alquilar una noche esa propiedad

    max_usuarios: capacidad maxima de personas que pueden alojarse

        Relaciones

        ManyToOne con ususario: que asocia a la propiedad del anfitrion 

        ManyToMany con Categoria: puedas ayudar a categorizar las propiedades

        ManyToMany con servicioExtra: pues los muchos  usuarios pueden contratar muchos servicios extras

        ManyToMany con fotoPropiedad: Porque muchas propiedades pueden tener muchas fotos de como es 
        
)    


Reserva (

    Este modelo representa una reserva de un inquilino a una propiedad 

    fecha_inicio: fecha y hora de inicio de la reserva

    fecha_fin: fecha y hora de finalizacion de la reserva

    total: costo total de la reserva

    estado estado de la reserva si esta en pendiente, confirmada o cancelada


        Relaciones 

        forenkey con propirdad que se a reservado

        OneTOne con pago ya que 1 pago es para 1 reserva
)

Comentario(


    Este modelo permite que los inquilinos puedan jdejar comentarios y valoraciones sobre las propiedades


    contenido: El texto del comentario

    fecha_comentario: Fecha y hora en que se publico el comentario

    valoracion: valoracion de la propiedad

    anonimo: Indica si el comentario es anonimo o desde un perfil 

        Relacion

        ManyToOne con propiedad: ya que en 1 propiedad puede poner varios comentarios
)

ServicioExtra(

    Este modelo representa a los servicios extras que los inquilinos pueden contratar, como desayuno, tal 


    nombre: nombre del servicio extra

    descripcion: descripcion del servicio

    precio: precio del servicio

    disponible: indica si el servicio estra disponoble en la propiedad

)

Categoria (

    Este modelo representa las categorias que se pueden clasificar las propiedades

    nombre= nombre de la categoria por ejemplo Apartamento, Casa de campo... etc

    descripcion: descripcion de la categoria 

    icono: icono que representa la categoria visualmente

    principal: indica si la categoria es principal


        Relaciones

        ManyTomany con propiedad: ya que una propiedad puede tener muchas categorias y tal 

)

CategoriaPrincipal (

    Este modelo representa una tabla intermedia que asocia propiedades con categoria

    fecha_asignacion: fecha en que se asigno la categoria la propiedad

    priodidad: indica la prioridad de la categoria en la relacion con la propiedad

        Relaciones 

        ManyToOne porque por ejemplo varias propiedadades pueden pertenecer a 1 categoria Apartamento o casa campo...

        ManyToOne por ejemplo varias propiedades se pueden clasificar como 1 prioridad, prioridad 1,2 ,3 ...

)

Pago(

    Este modelo representa la informacion de los pagos realizada por las reservar

    total: el total pagado

    fecha_pago: fecha y hora que se realizo el pago

    metodo_pago: metodo de pago utilizado, tarjeta, efectivo, paypal ...

    cog_transacion: identificador unico de cada transacion


        Relacion

        OneToOne con reserva: ya que 1 pago se hace en 1 reserva

)

FotoPropiedad(

    Este modelo representa las imagenes de las propiedades, que permiten a los inquilinos ver como son las propiedades

    foto: imagen de la propiedad

    descripcion: descripcion de la foto

    orden: indica en que orden se deben mostrar las fotos

    destacada: indica si la foto es destacada o no

        Relacion

        ManyToOne con propiedad, ya que 1 propiedad puede tener varias fotos 


)

Prioridad(

    Este modelo representa la prioridad de cada propiedad, asi como "alta", "media" "baja

    nombre: indica el nombre de la prioridad

    descripcion: descripcion de la prioridad

        Relaciones

        ManyTOone con prioridad: ya que muchas propiedades pueden tener 1 misma prioridad
        

    


)



No se porque no me deja la base de datos en el portatil, supongo que me faltara alguna extension, te adjunto foto de lo que me sale, me e descargado un programa 
para poder verla se llama DB Browser y esta bien creada, te adjunto foto de todo, espero que te sirva

FIN :D