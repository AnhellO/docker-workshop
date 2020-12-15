# Soluciones

A continuación se presentan las soluciones propuestas para los ejercicios del examen de diagnóstico.

## Ejercicio 1

- MySQL: `docker run --name mysql_db -p 4000:3306 -e MYSQL_ROOT_PASSWORD=secret123 -e MYSQL_USER=foo -e MYSQL_PASSWORD=bar123 -e MYSQL_DATABASE=baz -d mysql:8`
- Conectarse a la DB con alguno de los 2 comandos siguientes:
  - `docker exec -it mysql_db mysql -u foo -pbar123`
  - `docker exec -it mysql_db /bin/bash` y luego dentro de la sesión de bash del contenedor `mysql -u foo -pbar123`

## Ejercicio 2

- Creamos una network para que los contenedores puedan comunicarse: `docker network create mongo`
- Contenedor de `MongoDB`: `docker run --network mongo -d -p 27017:27017 --name m1 mongo`
- Contenedor de `Mongo Express`: `docker run --network mongo -d -p 8081:8081 -e ME_CONFIG_MONGODB_SERVER=m1 -e ME_CONFIG_BASICAUTH_USERNAME=DAS -e ME_CONFIG_BASICAUTH_PASSWORD=extra123 --name mexpress mongo-express`

## Ejercicio 3

- Volumen: `docker volume create mongo_volume`
- 1er contenedor de Mongo: `docker run -d -p 27017:27017 --name mongo -v mongo_volume:/data/db mongo`
- Ejecuta los scripts con `python ejercicio3/populate.py` y `python ejercicio3/find.py`
- Detén y borra el contenedor actual de Mongo: `docker stop mongo; docker rm mongo`
- 2do contenedor de Mongo: `docker run -d -p 27017:27017 --name mongo2 -v mongo_volume:/data/db mongo`
- Ejecuta el script `python ejercicio3/find.py` de nuevo

## Ejercicio 4

- Dockerfile final: [`Dockerfile`](ejercicio-4/Dockerfile)
- Construye la imágen con `docker build -t {mi-user}/static_flask .`
- Envíala a tu cuenta de `DockerHub` con `docker push {mi-user}/static_flask`
- Instancia un contenedor con `docker run --name flask -d -p 5000:8000 {mi-user}/static_flask`
