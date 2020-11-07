# Guía

Esta guía pretende mostrar paso por paso como ejecutar un contenedor que corre `MongoDB` y el cual utilizaremos para conectarnos con `Python`

1. Iniciar el container de `MongoDB` utilizando el comando `docker run -d -p 27017:27017 --name m1 mongo`
   1. Puedes conectarte al contenedor de Mongo con `docker exec -it m1 bash` y luego conectarte a MySQL por medio del comando `mongo`
   2. Para salir de la terminal interactiva del contenedor, primero hay que salir de `MongoDB` tecleando el comando `exit`, y una vez fuera podemos tecler la combinación `Ctrl+P` y `Ctrl+Q` para salir
2. Utilizaremos los scripts de `Python` existentes en la carpeta para popular la colección de mongo, utilizando la librería <https://api.mongodb.com/python/current/tutorial.html>
   1. Instalar la librería de mongo por medio del comando