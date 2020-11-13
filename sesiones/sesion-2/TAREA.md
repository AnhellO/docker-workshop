# Ejercicios

Ejercicios propuestos para practicar lo visto en la 2da sesión.

## Ejercicio 1

* Completar el capítulo 5 del libro `The Docker Book`

## Ejercicio 2

Partiendo del [ejemplo-2](../../ejemplos/ejemplo-2/) de comandos básicos con Docker:

* Mover la lógica de Python (incluída la instalación de la librería de `pymongo`) a que funcione con contenedores (es decir, vamos a "_Dockerizar_" la parte de Python)
* Agregar un nuevo contenedor que establezca una conexión a la BD de Mongo con [PHPMoAdmin](https://hub.docker.com/r/thinkcube/phpmoadmin)
* Una vez finalizado, agrega el `Dockerfile` de la app de Python "_dockerizada_" junto a los comandos de `docker-cli` que utilizaste para correr toda la app completa. Asegúrate de agregar los comandos de `docker build` y `docker-run` necesarios. Estos pueden agregarse en un archivo `.md`

## Ejercicio 3

* Crear un fork del siguiente repositorio <https://github.com/AnhellO/pokepy>. Después de crear el fork, deberás clonar éste a tu máquina local (es decir, tu propio fork del repositorio)
* Deberás de modificar el código existente para que cumpla con los siguientes requisitos:
  * Agregar el soporte al código para mostrar todos los pokemon existentes en la [API](https://pokeapi.co/), no solamente los primeros `151` pokemon como está actualmente en el código
  * Aparte del nombre y la imágen del pokemon, deberás de mostrar al menos `10` campos más de información para el pokemon en cuestión. Puedes utilizar los campos que tu quieras para cumplir con este requisito
  * Deberás de modificar el [template actual](https://github.com/AnhellO/pokepy/blob/master/templates/index.html) para que esta nueva información se muestre en una etiqueta [`<table>`](https://www.w3schools.com/html/html_tables.asp). También deberás de actualizar el aspecto de la página a que use diferentes colores, fuentes y demás atributos. Lo anterior es a gusto propio, pero debe de ser diferente al template original
  * Agrega soporte para que ahora sea posible obtener la información de un pokemon en base a un [parámetro en la URL](https://en.wikipedia.org/wiki/Query_string), en vez de obtener la información de un pokemon aleatoriamente en cada carga, ejemplo [`http://0.0.0.0:5050/?pokemon=alakazam`](http://0.0.0.0:5050/?pokemon=alakazam)
* Una vez que tu práctica este actualizada y ya que hayas probado que todo funciona correctamente, crea una nueva imagen de docker, con la version `1.0`, y publicala a tu cuenta de [Dockerhub](https://hub.docker.com/). Asegurate de compartir la URL final de la ubicación de tu imagen, es decir [`https://hub.docker.com/r/anhellojz/pokepy`](https://hub.docker.com/r/anhellojz/pokepy) como resultado para este punto