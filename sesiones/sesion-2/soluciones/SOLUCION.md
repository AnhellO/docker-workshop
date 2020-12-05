# Guía de Solución

1. Mongo: `docker run -d -p 27017:27017 --name m1 mongo`
2. PHPMoAdmin: `docker run --name moadmin -d --link m1:db -p 8080:80 thinkcube/phpmoadmin`
3. Creamos el `Dockerfile`
   1. Asegúrate de apuntar el host de mongo dentro de los scripts de `Python` a que use el nombre o el ID del contenedor de mongo
   2. Construimos la imágen con el comando `docker build -t tarea-sesion2 .`
   3. Creamos un contenedor en base a la nueva imágen con `docker run -d --link m1:db --name tarea_sesion2 tarea-sesion2`
