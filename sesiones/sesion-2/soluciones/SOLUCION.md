# Guía de Solución

1. Mongo: `docker run -d -p 27017:27017 --name m1 mongo`
2. PHPMoAdmin: `docker run --name moadmin -d --link m1:db -p 8080:80 thinkcube/phpmoadmin`
3. Construimos [`Dockerfile`](Dockerfile)
   1. Asegurarse de apuntar el host de mongo dentro de los scripts de `Python` a que use el nombre o el ID del contenedor de mongo
