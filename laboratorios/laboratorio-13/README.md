# Guía

Esta guía muestra un ejemplo de `Python` interactuando con un message broker de `RabbitMQ` de tal manera que se puedan enviar y recibir mensajes del mismo.

Hay dos scripts de `Python`, uno funge como _productor_ ([`send.py`](app/send.py)) y otro como _consumidor_ ([`receive.py`](app/receive.py)).

El ejemplo parte del 1er tutorial de la [guía oficial de `RabbitMQ`](https://www.rabbitmq.com/tutorials/tutorial-one-python.html), pero en este caso Dockeriza el ejemplo para que nada tenga que ser instalado ni ejecutado localmente (con excepción de `Docker` claro está), y hace algunas cuantas modificaciones menores para poder ser capaces de utilizar el dashboard de `RabbitMQ` a través de la URL <http://localhost:15672/>.

Para ejecutarlo, basta con utilizar el comando `docker-compose up -d --build`.

El contenedor de `pyconsumer` estará siempre en ejecución, en cambio el de `pyproducer` terminará después de cierto tiempo. Podemos volver a ejecutarlo por medio de los comandos `docker restart pyproducer` o `docker start pyproducer`, una vez que este se encuentre en estatus de `stop`.

Podemos jugar un poco con este ejemplo y hacer cambios a los scripts de `Python` directamente sin tener que reiniciar todo el stack de compose, ya que se utilizan bind-mount volumes para agilizar este proceso.

Una vez que hayamos terminado con las pruebas necesarias podemos proceder a detener todo el stack con el comando `docker-compose down`.

## Recursos

- <https://www.rabbitmq.com/getstarted.html>
- <https://hub.docker.com/_/rabbitmq>
- <https://pika.readthedocs.io/en/stable/>
