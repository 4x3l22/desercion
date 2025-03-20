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

## 1. Administrador
- Registra formularios.
- Asigna roles a los usuarios.
- Controla los accesos y las vistas disponibles para cada usuario.

## 2. Instructor
- Valida la existencia de un aprendiz en el sistema.
- Si el aprendiz existe, le asigna un proceso utilizando el formulario creado por el administrador.
- Si el aprendiz no está registrado, puede añadirlo al sistema.
- Cuando el proceso de deserción es aprobado, puede registrar la deserción del aprendiz.
- No puede registrar una deserción sin la aprobación correspondiente.

## 3. Coordinador Académico
- Revisa las solicitudes de deserción.
- Puede aprobar o rechazar las solicitudes.
- Deja comentarios justificando su decisión.

## 4. Coordinador FPI
- Tiene las mismas funciones que el Coordinador Académico.
- Puede aprobar o rechazar solicitudes y dejar comentarios.

## 5. Bienestar
- Tiene las mismas funciones que el Coordinador Académico.
- Puede aprobar o rechazar solicitudes y dejar comentarios.

# Tecnologías
## 1. Back-end
- Django: Framework de desarrollo en Python utilizado para la gestión del servidor y la lógica de negocio.
- Implementa el patrón MTV (Model-Template-View) para una estructura organizada del código.
- Maneja la comunicación con la base de datos y expone APIs para el consumo del front-end.

## 2. Front-end
- React.js: Biblioteca de JavaScript utilizada para la construcción de la interfaz de usuario.
- Facilita una experiencia interactiva y dinámica mediante componentes reutilizables.

## 3. Base de datos
- MySQL: Sistema de gestión de bases de datos relacional utilizado para almacenar la información del módulo.
- La base de datos está dockerizada, lo que permite mayor portabilidad y facilidad de despliegue.

## 4. Contenedorización
- Docker: Se utiliza para la gestión de contenedores, asegurando que la base de datos y otros servicios funcionen de manera uniforme en diferentes entornos.

# Estructura del proyecto
El módulo de deserción sigue una arquitectura de capas, permitiendo un mejor orden de datos y lógica. Cada capa cumple una función específica dentro del sistema, asegurando una separación clara entre la manipulación de datos, la lógica de negocio y la presentación.

Organización:
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
│── docker-compose.yml         # Configuración de Docker  
│── .env                       # Variables de entorno  
```

# Cómo ejecutar el proyecto
Para ejecutar el proyecto de Django, sigue los siguientes pasos:
1. Clona el repositorio y navega a la carpeta del proyecto:
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd proyecto-desercion
   ```
2. Crea un entorno virtual y actívalo:
   ```sh
   python -m venv venv
   source venv/bin/activate  # En MacOS/Linux
   venv\Scripts\activate     # En Windows
   ```
3. Instala las dependencias del proyecto:
   ```sh
   pip install -r requirements.txt
   ```
4. Ejecuta las migraciones para configurar la base de datos:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Crea un superusuario para acceder al panel de administración:
   ```sh
   python manage.py createsuperuser
   ```
6. Inicia el servidor de desarrollo:
   ```sh
   python manage.py runserver
   ```
