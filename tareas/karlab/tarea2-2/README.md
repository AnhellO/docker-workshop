### Commands

1. Construimos la imagen de Python
`docker build -t karlab-t2 .`

2. Montamos un contenedor de Mongo
`docker run -d -p 27017:27017 --name m1 mongo`

3. Se agrega un nuevo contenedor que establezca una conexión a la BD de Mongo con [PHPMoAdmin](https://hub.docker.com/r/thinkcube/phpmoadmin) donde se expone el puerto 8080:80
`docker run --name phpmoadmin -d --link m1:db -p 8080:80 thinkcube/phpmoadmin`

4. Se ejecuta el contenedor de mongo con la imagen de Python
`docker run -d --link m1 --name appkarlab karlab-t2`

5. Puedes revisar que funcionó ejecutando
`docker logs appkarlab`

6. Visita [localhost:8080](http://localhost:8080/) para gestionar la DB creada