# Guía de Solución

1. Mongo: `docker run -d -p 27017:27017 --name db --hostname db mongo`
2. PHPMoAdmin: `docker run --link db:db --name moadmin -d -p 8080:80 thinkcube/phpmoadmin`
3. Creamos el `Dockerfile`
   1. Versión en [`Python`](python/Dockerfile)
   2. Versión en [`GO`](go/Dockerfile)
   3. Apuntar el host dentro de las conexiones de los scripts a que utilicen el nombre o el ID del contenedor de mongo
   4. Construimos la imágen con el comando `docker build -t tarea-sesion2 .`
   5. Creamos un contenedor en base a la nueva imágen con `docker run -d --link db:db --name tarea_sesion2 tarea-sesion2`
