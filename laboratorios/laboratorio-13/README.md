# Guía

Esta guía muestra un ejemplo básico de como interactuar con un message broker de `RabbitMQ` de tal manera que se puedan enviar y recibir mensajes del mismo. El ejemplo está codificado tanto para `Python` como para `GO`.

En ambos casos existen dos archivos diferentes, uno funge como el _productor_ ([`send.py`](python/app/send.py) para `Python` y [`send/main.go`](go/app/send/main.go) para `GO`), y otro como el _consumidor_ ([`receive.py`](python/app/receive.py) para `Python` y [`receive/main.go`](go/app/receive/main.go) para `GO`).

El ejemplo parte del **1er tutorial** de la [guía oficial de `RabbitMQ`](https://www.rabbitmq.com/tutorials/tutorial-one-python.html), pero en este caso Dockeriza el ejemplo para que nada tenga que ser instalado ni ejecutado localmente (con excepción de `Docker` claro está), y hace algunas cuantas modificaciones menores para poder ser capaces de utilizar el dashboard de `RabbitMQ` a través de la URL <http://localhost:15672/>.

Para ejecutarlo, basta con utilizar el comando `docker-compose up -d --build` en la versión en la que quieras revisarlo (`Python` o `GO`).

El respectivo contenedor de `consumer` estará siempre en ejecución, en cambio el de `producer` terminará después de cierto tiempo de ejecución. Podemos volver a ejecutarlo por medio de los comandos `docker restart producer` o `docker start producer` una vez que este se encuentre en estatus de `stop`, si es que deseamos que se vuelvan a enviar mensajes.

Podemos jugar un poco con este ejemplo y hacer cambios a los respectivos scripts directamente sin tener que reiniciar todo el stack de compose, ya que se utilizan [_bind-mount volumes_](https://docs.docker.com/storage/bind-mounts/) para agilizar este proceso.

Una vez que hayamos terminado con las pruebas necesarias podemos proceder a detener todo el stack con el comando `docker-compose down`.

## Recursos

- <https://www.rabbitmq.com/getstarted.html>
- <https://hub.docker.com/_/rabbitmq>
- <https://pika.readthedocs.io/en/stable/>
