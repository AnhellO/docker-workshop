# Guía

Esta guía pretende enseñar un breve ejemplo de como llevar a cabo operaciones `CRUD` por medio de un `ORM` en `Python`, el cual será [`Peewee`](http://docs.peewee-orm.com/en/latest/) para este ejemplo.

Las operaciones `CRUD` se llevan a cabo en un contenedor de `PostgreSQL`, el cual inicializaremos por medio de un archivo `init.sql` y el entrypoint de Docker `docker-entrypoint-initdb.d`, que permite que todos los scripts dentro de esa ruta sean ejecutados al inicializar un nuevo contenedor. Para ello utilizaremos el [`Dockerfile`](Dockerfile) que se encuentra dentro de la carpeta del ejemplo.

1. Construye la imagen con el comando `docker build -t mipostgre .`
   1. Recuerda que puedes revisar tu imagen recién creada utilizando el comando `docker images`
2. Ahora ejecuta un contenedor en base a la imágen que acabas de crear utilizando el comando `docker run -d --name postgres -p 5432:5432 mipostgre`
   1. Utiliza el comando `docker logs postgres` para poder verificar la inicialización del contenedor, ¿puedes ver como nuestro script de `init.sql` se ejecuta en la línea de `running /docker-entrypoint-initdb.d/init.sql`?
3. Después de esto ejecuta el script [`orm.py`](orm.py) utilizando el comando `python orm.py`
   1. Asegúrate de instalar las librerías necesarias antes por medio del comando `pip install --no-cache-dir -r requirements.txt`
   2. El script debe de correr sin problema alguno, y deberías de poder ver en el output de tu consola como se imprimen registros de la `DB` y valores de las operaciones `CRUD`
   3. Puedes revisar la base de datos directamente desde el contenedor de `PostgreSQL`, siguiendo los pasos descritos a continuación:
      1. Ejecuta el comando `docker exec -it postgres bin/bash` para meterte al contenedor de `PostgreSQL`
      2. Una vez dentro ejecuta el cliente de CLI `psql` con el siguiente comando: `psql -U the_cat -d random_cats`
      3. Una vez dentro de la DB puedes utilizar el comando `\dt` para ver las tablas existentes en la base de datos, y ahí deberías de ver la tabla de `my_cats`. Teclea el query `SELECT * FROM my_cats;` para poder ver los rows existentes
      4. Puedes salir del client `psql` utilizando el comando `\q`, y después salir del contenedor de `PostgreSQL` tecleando `exit`
   4. Siéntete libre de jugar todo lo necesario con el archivo de `orm.py` y con el contenedor en ejecución, y una vez que hayas terminado asegúrate de remover el contenedor de `PostgreSQL` por medio del comando `docker stop postgres; docker rm postgres`

## Recursos

* <https://www.docker.com/>
* <https://www.postgresql.org/>
* <https://hub.docker.com/_/postgres>
* <http://docs.peewee-orm.com/en/latest/>
* <https://parzibyte.me/blog/2019/06/17/python-postgresql-ejemplo-conexion-crud/>
* <https://cosasdedevs.com/posts/como-crear-un-crud-en-python-parte-4-conexion-a-postgresql/>
* <https://www.fullstackpython.com/object-relational-mappers-orms.html>
