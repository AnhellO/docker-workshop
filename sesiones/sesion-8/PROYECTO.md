# Proyecto

## Tema

* Micro-Services Architecture: Implementa el proyecto siguiendo los lineamientos y requisitos del patrón de arquitectura de microservicios

## Especificaciones

### Inicio

Crear un nuevo repositorio para el proyecto final en la cuenta de cualquiera de los miembros del equipo.

Los miembros restantes deberán de crear un fork de este repositorio y contribuir en él conforme se vaya desarrollando la práctica.

Al final cada elemento del equipo deberá de subir un link al repositorio del proyecto final en su propia carpeta de alumno dentro de un archivo `.md` el cual deberá de estar bajo una nueva sub-carpeta que se llame `Ordinario`.

### Desarrollo

Crear un archivo `docker-compose.yml` por medio del cual se instancien **5** contenedores:

#### Contenedor A - DB

* Se encargará de correr un servidor de base de datos en alguno de los motores de base de datos que se revisaron en clase, es decir, elegir entre `PostgreSQL`, `MySQL`, `MongoDB` y `Redis`. Esta base de datos almacenará la información de nuestra aplicación en general
* La base de datos debe de tener persistencia habilitada, es decir, no importa cuantas veces iniciemos o detengamos nuestro container de `DB`, incluso si lo removemos, los datos que previamente almacenamos estarán disponible en el host/equipo local. Recuerda usar volúmenes para lograr esto :wink:

#### Contenedor B - DBMS/DBAdmin

* Se encargará de ejecutar alguno de los `DBMS` que vimos en clase, dependiendo del motor de base de datos elegido. También es posible investigar e implementar algún otro `DBMS` que funcione sobre `Docker` y que sea más sencillo y/o a gusto del equipo
* Este contenedor se conectará con la base de datos del contenedor `A` de tal manera que podamos visualizar el esquema de datos creado para este proyecto

#### Contenedor C - API Scraper/Fetcher/Consumer

* Este contenedor se encargará de correr un scraper/consumer para obtener los datos de una API
* La API es opcional de entre las disponibles en el listado de [Public APIs](https://github.com/public-apis/public-apis), pero debe de contar con al menos 3 diferentes endpoints/recursos. Por ejemplo, tenemos la API de [Marvel](https://developer.marvel.com/docs), y `/v1/public/characters`, `/v1/public/comics`, `/v1/public/creators`, `/v1/public/events`, `/v1/public/series` y `/v1/public/stories` son cada uno diferentes recursos, es decir que tenemos **6** endpoints/recursos en esta API
* No puede elegirse la API de Marvel que se mostró en el ejemplo del punto anterior
* Se deben de obtener todos los datos disponibles en la `API` para cada endpoint/recurso y estos no deben de guardarse en una sola tabla, por lo que hay que analizar, definir y estructurar correctamente la base de datos al momento de diseñarla

#### Contenedor D - Front-End

* Para esta parte puedes utilizar [`GO-Chi`](https://github.com/go-chi/chi), [`GO-Fiber`](https://github.com/gofiber/fiber) o cualquier otro framework `MVC` como [`GO-Gin`](https://github.com/gin-gonic/gin) por ejemplo. Incluso puedes desarrollarlo "_from scratch_" si lo consideras pertinente y necesario :wink:
* Este contenedor estará a cargo de correr una pequeña "_web-app_" que muestre un índice de todos los endpoints/recursos obtenidos de la `API` a través de la página principal. Después, para cada endpoint/recurso en específico tendremos un link a una página nueva
* En la página nueva se deben de mostrar todos los datos obtenidos para cada endpoint/recurso en específico, es decir, partiendo del ejemplo de la API de Marvel, suponiendo que yo el usuario di click al link del endpoint `/characters/78` en la página del índice, la nueva página me deberá de mostrar toda la información relacionada al personaje con ese `ID = 78`
* Se puede crear una página "_índice_" para cada uno de los diferentes endpoints/recursos, o bien, una sola página de este tipo que agrupe a todos los endpoints/recursos pero separados de alguna manera explícita (por ejemplo una etiqueta `<h2>` o una etiqueta `<hr />`)
* Puedes utilizar el sistema de templates nativo de `GO`, o bien utilizar los templates provistos por alguno de los web frameworks (si es que elegiste alguno)
* Finalmente, para cada uno de los endpoints/recursos que hayas agregado, habilita la opción de crear registros por medio del mismo, es decir, ser capaz de hacer un request de tipo [`HTTP - POST`](https://developer.mozilla.org/es/docs/Web/HTTP/Methods/POST) a esa ruta en tu frontend, de tal manera que alguien que consuma tu "_web-app_" también pueda crear registros por medio de la misma. Partiendo una vez más del ejemplo de Marvel, si yo quisiera crear un nuevo personaje en la `BD`, entonces yo tendría que mandar un `POST` request al endpoint de `/characters/` en mi "_web-app_". Asegúrate de que para cada endpoint/recurso se pasen todos los datos necesarios para poder crear un registro en la BD con éxito. Puedes hacer pruebas para este punto en específico con herramientas gratuitas como [`Postman`](https://www.postman.com/) o [`Insomnia`](https://insomnia.rest/)

#### Contenedor E - Message Queue Broker

* Este contenedor se encargará de ejecutar un message queue broker como [RabbitMQ](https://www.rabbitmq.com/), [Apache Kafka](https://kafka.apache.org/) o [Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)
* El nuevo servicio pasará a ser el intermediario entre el contenedor `D` del front end y el contenedor `A` de la base de datos, de tal manera que habrá que sobreescribir un poco la lógica en el contenedor `D` para la creación de registros por medio de `HTTP POST` de tal manera que ahora soporte operaciones asíncronas por medio del contenedor `E`, es decir, si escogiste `RabbitMQ` como message queue broker, entonces al enviar peticiones `POST` para crear un nuevo registro estas pasarían por `RabbitMQ` primero, y este sería el que se encargaría de enviarlo al contenedor/servicio correcto que este suscrito a un tipo concreto de mensajes, en este caso el de `PostgreSQL`. Lo mismo aplica en la otra dirección, es decir `PostgreSQL` respondiéndole al servicio del front end por medio de `RabbitMQ`. Pueden crear un endpoint/recurso nuevo para este punto, de tal manera que la aplicación tenga soporte tanto síncrono como asíncrono, o bien, sobreescribir la funcionalidad del endpoint original, como se más sencillo para ustedes

#### Opcional - Puntos Extra

Los siguientes puntos son opcionales, sin embargo implementarlos provee **1** punto extra por cada uno sobre la calificación total final.

* Habilitar soporte para las operacions [`PATCH`](https://developer.mozilla.org/es/docs/Web/HTTP/Methods/PATCH), [`PUT`](https://developer.mozilla.org/es/docs/Web/HTTP/Methods/PUT) y [`DELETE`](https://developer.mozilla.org/es/docs/Web/HTTP/Methods/DELETE) en el contenedor del front end
* Agregar un contenedor extra con el front end separado del contenedor `D`, es decir, el contenedor `D` pasaría a tener el papel de una API propia, mientras que el nuevo contenedor `F` sería el que tendría el front end con la interfaz. Acá puedes utilizar tecnologías como `CSS`, `Javascript`, `Bootstrap`, `Angular` o `ReactJS` para hacer más efectivo este proceso :wink:
* Agregar tests unitarios y de integración para el proyecto
* Si agregaste soporte para `PATCH`, `PUT` y `DELETE`, entonces agregar soporte asíncrono para estos te dará otro punto extra :wink:

### Conclusión

Crear un archivo `README.md` en el que se incluya lo siguiente:

* Un diagrama de la arquitectura de tu proyecto y un diagrama de la base de datos (`DER`). Pueden apoyarse de algunas herramientas como <https://github.com/mingrammer/diagrams> o <https://app.diagrams.net/> para generar los diagramas del proyecto. Este diagrama también debe de incluirse como imágen dentro del proyecto final
* Los pasos a seguir, detallados y concisos, para hacer funcionar el proyecto, de tal manera que pueda ser revisado sin mayores complicaciones

## Recursos

### Arquitectura

* <https://www.oreilly.com/library/view/software-architecture-patterns/9781491971437/ch04.html>
* <https://www.microservices.com/>
* <https://microservices.io/patterns/microservices.html>
* <https://medium.com/hashmapinc/the-what-why-and-how-of-a-microservices-architecture-4179579423a9>
* <https://github.com/GoogleCloudPlatform/microservices-demo>
* <https://microservices-scaffold.readthedocs.io/en/latest/>
* <https://codigofacilito.com/articulos/microservcios>
* <https://medium.com/seek-blog/microservices-in-go-2fc1570f6800>
* <https://www.avantica.com/es/blog/construyendo-microservicios-con-golang-y-go-kit>

### Librerías

* <https://www.rabbitmq.com/getstarted.html>
* <https://github.com/Pungyeon/go-rabbitmq-example/blob/master/README.md>
* <https://kafka.apache.org/>
* <https://redislabs.com/blog/use-redis-event-store-communication-microservices/>
* <https://docs.celeryproject.org/en/stable/getting-started/introduction.html>
* <https://autobahn.readthedocs.io/en/latest/asynchronous-programming.html>
* <https://xpdays.com.ua/programs/event-driven-systems-with-mongodb/>
* <https://nameko.readthedocs.io/en/stable/>

## Deadline

* `Sábado 27 de Febrero`
