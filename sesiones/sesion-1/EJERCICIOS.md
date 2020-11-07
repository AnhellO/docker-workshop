# Ejercicios

Ejercicios propuestos para practicar lo visto en la 1er sesión.

## Ejercicio 1

* Completar los capítulos 1 a 4 del libro `The Docker Book`.

## Ejercicio 2

Partiendo del [ejemplo-2](../../ejemplos/ejemplo-2/) de comandos básicos con Docker:

* Mover la lógica de Python (incluída la instalación de la librería de `pymongo`) a que funcione con contenedores (es decir, vamos a "_Dockerizar_" la parte de Python)
* Agregar un nuevo contenedor que establezca una conexión a la BD de Mongo con [PHPMoAdmin](https://hub.docker.com/r/thinkcube/phpmoadmin)
* Una vez finalizado, agrega el `Dockerfile` de la app de Python "_dockerizada_" junto a los comandos de `docker-cli` que utilizaste para correr toda la app completa. Asegúrate de agregar los comandos de `docker build` y `docker-run` necesarios. Estos pueden agregarse en un archivo `.md`.
