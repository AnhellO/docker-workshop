# Guía

Esta guía pretende mostrar paso por paso como ejecutar un par de contenedores de `MySQL` y de `PHPMyAdmin` que estén conectados entre si.

1. Inicia container de MySQL: `docker run --name=db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=secret-pw -d mysql:8`
   1. Puedes revisar los logs del contenedor con `docker logs db`
   2. Puedes conectarte al contenedor con `docker exec -it db bash` y luego conectarte a MySQL por medio del comando `mysql -u root -p`
   3. Para salir de la terminal interactiva del contenedor, primero hay que salir de `MySQL` por medio de `exit`, y una vez fuera podemos tecler la combinación `Ctrl+P` y `Ctrl+Q` para salir. Esto no detendrá nuestro contenedor
2. Inicia container de `PHPMyAdmin`: `docker run --name=my-admin -p 82:80 --link db:db -d phpmyadmin`
   1. Podrás ver tu contenedor de `PHPMyAdmin` corriendo desde <http://localhost:82/>
   2. Una vez ahí introduce las credenciales correctas para acceder y comenzar a jugar con tus contenedores
3. Una vez que hayas jugado un poco con los contenedores, asegúrate de detenerlos y borrarlos utilizando `docker stop` para detenerlos, y `docker rm` para removerlos
