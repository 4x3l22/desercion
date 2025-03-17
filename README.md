# Introducción

El aplicativo busca optimizar y simplificar procesos que actualmente presentan limitaciones, ya que algunos formularios y solicitudes se gestionan a través de Power Automate, lo que restringe el control y manejo de la información. Además, el flujo de trabajo se divide en dos programas, donde uno inicia el proceso y el otro lo finaliza, lo que hace que la gestión sea menos eficiente.

Dentro del aplicativo existen varios módulos, y uno de ellos es el módulo de deserción, en el cual fui asignado. Este módulo permite a los instructores, coordinación académica, bienestar y coordinador FPI gestionar las deserciones de los aprendices de manera más estructurada y eficiente. Una de sus ventajas es que puede integrarse fácilmente con el resto de los módulos gracias al módulo de seguridad, el cual permite la conexión sin afectar la estructura general del sistema.

# Objetivo del software

El software tiene como objetivo mejorar los sistemas utilizados por el SENA, brindando mayor seguridad y optimizando la gestión de los procesos. Su implementación permite simplificar tareas, facilitar su comprensión y mejorar el flujo de trabajo. Además, contribuye a la reducción de costos operativos al hacer que los procedimientos sean más eficientes y estructurados.

# Alcance del módulo de deserción

El módulo de deserción está diseñado para gestionar y optimizar el proceso de registro y validación de deserciones dentro del sistema. Su enfoque principal es garantizar un flujo de trabajo eficiente y estructurado para los instructores y demás usuarios involucrados.

# Funcionalidades incluidas

- Registro de deserciones.
- Validación de información.
- Generación de reportes para las áreas correspondientes.
- Registro de usuarios.
- Validación de la existencia de aprendices.
- Validaciones en el registro de procesos.
- Asignación de roles, vistas y formularios.
- Control de acceso para usuarios nuevos.
- Listado de procesos registrados para aprendices.
- Posibilidad de rechazo y aprobación de solicitudes con comentarios.
- Listado de procesos pendientes y en ejecución.

# Límites del módulo

Este módulo se enfoca exclusivamente en la gestión de deserciones y los registros pertinentes dentro del módulo de seguridad. No abarca funciones ajenas a este proceso ni la administración de otros módulos dentro del sistema.

# Usuarios del sistema

El módulo de deserción cuenta con distintos roles de usuario, cada uno con permisos y responsabilidades específicas dentro del sistema.

## Administrador
- Registra formularios.
- Asigna roles a los usuarios.
- Controla los accesos y las vistas disponibles para cada usuario.

## Instructor
- Valida la existencia de un aprendiz en el sistema.
- Asigna un proceso utilizando el formulario creado por el administrador.
- Si el aprendiz no está registrado, puede añadirlo al sistema.
- Cuando el proceso de deserción es aprobado, puede registrar la deserción del aprendiz.
- No puede registrar una deserción sin la aprobación correspondiente.

## Coordinador Académico
- Revisa las solicitudes de deserción.
- Puede aprobar o rechazar las solicitudes.
- Deja comentarios justificando su decisión.

## Coordinador FPI
- Tiene las mismas funciones que el Coordinador Académico.
- Puede aprobar o rechazar solicitudes y dejar comentarios.

## Bienestar
- Tiene las mismas funciones que el Coordinador Académico.
- Puede aprobar o rechazar solicitudes y dejar comentarios.

# Tecnologías

## Back-end
- Django: Framework de desarrollo en Python utilizado para la gestión del servidor y la lógica de negocio.
- Implementa el patrón MTV (Model-Template-View).

## Front-end
- React.js: Biblioteca de JavaScript utilizada para la construcción de la interfaz de usuario.

## Base de datos
- MySQL: Sistema de gestión de bases de datos relacional.
- Dockerizada para mayor portabilidad.

## Contenedorización
- Docker: Se utiliza para la gestión de contenedores.

# Estructura del proyecto

```
/proyecto-desercion  
│── appdesercion/              # Contiene toda la lógica del proyecto  
│   ├── Entity/                # Capa de datos  
│   │   ├── DTO/               # Data Transfer Objects (DTO)  
│   │   ├── DAO/               # Data Access Objects (DAO)  
│   │   ├── models.py          # Definición de modelos de base de datos  
│   ├── Business/              # Capa de negocio y validaciones  
│   │   ├── services.py        # Servicios que conectan DTO con API  
│   ├── Apis/                  # Capa de API  
│   │   ├── serializers.py     # Serialización de datos  
│   │   ├── views.py           # Controladores de las APIs  
│   │   ├── urls.py            # Rutas específicas de la API  
│   ├── utils/                 # Funciones auxiliares  
│   │   ├── email.py           # Código de envío de correos electrónicos  
│   ├── templates/             # Plantillas HTML para emails  
│   ├── migrations/            # Migraciones y cambios en la base de datos  
│   ├── urls.py                # Rutas principales del módulo  
│  
│── desercion/                 # Proyecto principal de Django  
│   ├── settings.py            # Configuración del proyecto  
│   ├── urls.py                # Rutas generales del sistema  
│   ├── wsgi.py                # Punto de entrada del servidor  
│  
│── docker-compose.yml         # Configuración de Docker  
│── .env                       # Variables de entorno  
```

# Consideraciones importantes

- El DTO nunca debe usarse directamente con el DAO, sino a través del service y la API.
- Revisar el envío de correos electrónicos en `utils/email.py`, ya que aún requiere ajustes.
- Para ejecutar el proyecto siempre debe ejecutar el comando `python manage.py runserver`.

# Mejoras

Las mejoras a hacer incluyen la gestión de listas rechazadas por los roles administrativos, asegurando que se respeten los roles definidos en los `enum` del sistema.

