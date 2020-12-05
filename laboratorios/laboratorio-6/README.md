# Guía

Esta guía parte de la solución de la tarea propuesta en la 2da sesión, pero utiliza el concepto de `docker networks` para comunicar los contenedores entre si.

También cambiaremos de utilizar el cliente de [`PHPMoAdmin`](https://hub.docker.com/r/thinkcube/phpmoadmin) a utilizar el de [`Mongo-Express`](https://hub.docker.com/_/mongo-express).

Vamos a partir de la solución propuesta, pero aplicando algunos cambios menores.

- Comenzamos por crear una network custom con el comando `docker network create lab6`
- Vamos a ejecutar el contenedor de `MongoDB`, pero ahora montándolo sobre nuestra nueva red: `docker run -d -p 27017:27017 --name m1 --network lab6 mongo`
- Procedemos a ejecutar el contenedor de `Mongo Express` con el siguiente comando: `docker run -d --name moexpress --network lab6 -e ME_CONFIG_MONGODB_SERVER=m1 -e ME_CONFIG_BASICAUTH_USERNAME=admin -e ME_CONFIG_BASICAUTH_PASSWORD=karlitabb -p 8081:8081 mongo-express`
  - Puedes visitar el cliente DBMS en la URL <http://0.0.0.0:8081/>
- Después de tener nuestros dos contenedores iniciales de `Mongo` y del cliente de `Mongo Express` en ejecución, vamos a construir una imagen taggeada específicamente para este laboratorio con la cual ejecutaremos la solución propuesta en `GO` para que se conecté con el contenedor de mongo, pero ahora por medio de la docker network custom que hemos creado
  - Construimos la imagen con el comando `docker build -t lab6 .`
  - Instanciamos un contenedor de la imagen construída previamente con el comando `docker run -d --network lab6 --name mongogo lab6`
  - Visita el cliente de `Mongo Express` para poder ver los cambios reflejados

## Recursos

- <https://docs.docker.com/network/>
- <https://hub.docker.com/_/mongo-express>
