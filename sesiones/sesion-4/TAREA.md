# Ejercicios

Ejercicios propuestos para practicar lo visto en la 4ta sesión.

## Ejercicio 1

- Completar ejercicio 2 del capítulo 5 del libro `The Docker Book`: `Using Docker to build and test a web application.`

## Ejercicio 2

- Lleva a cabo la guía propuesta en el [laboratorio 7](../../laboratorios/laboratorio-7/README.md)

## Ejercicio 3

Crea 2 contenedores por medio del cliente `CLI` de `docker`:

- El **1er contenedor** ejecutará un servidor de [`Redis`](https://hub.docker.com/_/redis) y su nombre deberá de ser `redis`
- El **2do contenedor** deberá de ejecutar un servidor de [`Redis Commander`](https://hub.docker.com/r/rediscommander/redis-commander) el cual tiene que estar protegido con usuario y contraseña para poder acceder a él. El contenedor debe de llamarse `commander`

Asegúrate de probar que todo funciona correctamente y que el servidor de `redis-commander` puede contectarse al de `redis` sin problema alguno visitando la URL correcta. Utiliza `docker networks` para llevar a cabo este proceso.

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste este ejercicio a cabo en tu equipo.
