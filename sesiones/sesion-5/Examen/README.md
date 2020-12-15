# Examen de Diagnóstico

## Ejercicios

- Si el ejemplo solamente necesita comandos escritos entonces agregalos en un archivo `.md` que anexes por separado dentro de tu carpeta con las soluciones al examen
- En caso de que el ejercicio necesite algún otro archivo, asegúrate de adjuntarlo junt a tu solución

### Ejercicio 1

¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de `Docker` que corra un servidor de [`MySQL`](https://hub.docker.com/_/mysql) versión **8** y que cumpla con los siguientes puntos?

- Que el contenedor se llame `mysql_db`
- Que el contenedor se ejecute en el background (es decir, que se mantenga en ejecución)
- Que el puerto asignado a la máquina host sea el `4000`
- Que el usuario sea `foo`
- Que el password sea `bar123`
- Que se cree una base de datos llamada `baz`

Finalmente, ¿con qué comando(s) puedo conectarme a mi base de datos de `MySQL` corriendo dentro de mi contenedor de `mysql_db`?

### Ejercicio 2

Crea 2 contenedores por medio del cliente `CLI` de `docker`:

- El **1er contenedor** ejecutará un servidor de [`MongoDB`](https://hub.docker.com/_/mongo) y su nombre deberá de ser `m1`
- El **2do contenedor** ejecutará un cliente de [`Mongo Express`](https://hub.docker.com/_/mongo-express) el cual se llame `mexpress` y que se conectará al contenedor `m1` creado en el punto anterior. Otro requisito más es que este cliente tiene que estar protegido por medio de las siguientes credenciales:
  - Usuario: `DAS`
  - Password: `extra123`

Anexa los comandos utilizados en el proceso

### Ejercicio 3

Crea un volumen que se llame `mongo_volume` y que utilice el driver por default para los `Docker` volumes.

Ejecuta un contenedor de [`MongoDB`](https://hub.docker.com/_/mongo) que se llame `mongo` y que monte el volumen creado en el paso anterior, y una vez que todo este listo ejecuta los siguientes pasos:

- Corre el script [`populate.py`](ejercicio-3/populate.py)
- Luego corre el otro script [`find.py`](ejercicio-3/find.py), deberías de obtener una salida como la siguiente:

``` shell
##### RECORDS #####
{'_id': ObjectId('5fbf475bece16a8442cfe774'), 'first_name': 'foo', 'last_name': 'bar', 'email': 'foo@mail.com'}
{'_id': ObjectId('5fbf475bece16a8442cfe775'), 'first_name': 'foo', 'last_name': 'baz', 'email': 'baz@mail.com'}
{'_id': ObjectId('5fbf475bece16a8442cfe776'), 'first_name': 'bar', 'last_name': 'baz', 'email': 'bar@mail.com'}
{'_id': ObjectId('5fbf475bece16a8442cfe777'), 'first_name': 'fulano', 'last_name': 'mengano', 'email': 'fulano@mail.com'}
{'_id': ObjectId('5fbf475bece16a8442cfe778'), 'first_name': 'zultano', 'last_name': 'perengano', 'email': 'zultano@mail.com'}
```

Ahora detén y borra el contenedor de `mongo`, y levanta un nuevo contenedor que también ejecute un servidor de `MongoDB` y que utilice el mismo volumen de `mongo_volume` previamente creado, pero que en esta ocasión se llame `mongo2`.

Vuelve a ejecutar el script de [`find.py`](ejercicio-3/find.py) y contesta a la siguiente pregunta: ¿Cuál fue nuestra salida en esta ocasión?

### Ejercicio 4

Crea un `Dockerfile` que cumpla con los siguientes requisitos:

- Que extienda de la imágen base de [`Python3`](https://hub.docker.com/_/python)
- Que utilice el directorio `/usr/src` como el directorio de trabajo
- Que clone el siguiente repositorio: <https://github.com/joaoventura/flask-static-site>
- Que instale todas las dependencias necesarias especificadas en el archivo de [`requirements.txt`](https://github.com/joaoventura/flask-static-site/blob/master/requirements.txt) por medio de `pip`
- Y finalmente que ejecute el script [`site.py`](https://github.com/joaoventura/flask-static-site/blob/master/site.py), justo como se especifíca en el [`README`](https://github.com/joaoventura/flask-static-site#development--building) del repositorio
- Ten en cuenta que los contenedores creados en base a esta imágen deben de ser accesibles desde el exterior :wink:

Construye una imágen basada en el `Dockerfile` que acabas de crear y llámala `{mi-user}/static_flask`, donde `{mi-user}` equivale a tu usuario de [`DockerHub`](https://hub.docker.com/). Una vez que hayas creado la imagen envíala a tu cuenta de `DockerHub`. Debe de estar accesible similar a como lo está en [este ejemplo](https://hub.docker.com/r/anhellojz/static_flask). Asegúrate de adjuntar el link a ella en tus resultados del ejercicio.

Para finalizar, ejecuta un nuevo contenedor basado en la imágen recién creada que se llame `flask`, que corra "_daemonizado_", y que esté accesible a través del puerto `5000` de tu máquina.
