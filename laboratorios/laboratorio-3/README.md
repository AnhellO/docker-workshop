# Guía

La intención de esta guía es involucrarse con el uso de Dockerfiles y la construcción de imágenes en `Docker`.

1. Clona el repositorio de <https://github.com/AnhellO/pokepy> en esta ubicación
2. Muévete al directorio a través de la CLI y ejecuta el comando `docker build` para construir una nueva imágen de Docker en base al Dockerfile existente en el repositorio, por ejemplo `docker build -t fulanito-hub/pokepy-ejemplo:1.0 .`, donde `fulanito-hub` es el nombre de usuario en `DockerHub`, `pokepy-ejemplo` es el nombre que le vas a poner a tu imagen (puede ser cualquiera, el que tu gustes), y `1.0` la versión de tu imagen (puedes utilizar cualquier versión para este ejemplo)
3. Utiliza el comando `docker images` para que puedas listar todas las imágenes existentes en tu computadora o máquina host. Si te das cuenta, la nueva imagen que acabas de construir debería estar listada ahí
4. Instancia un contenedor en base a esa nueva imagen utilizando `docker run`
5. Verifica que tu contenedor está corriendo correctamente por medio de <http://localhost:5000/>
6. Esta imágen existe solamente en tu máquina host, puedes proceder a subirla a tu cuenta de docker hub utilizando el comando [`docker push`](https://docs.docker.com/engine/reference/commandline/push/) o bien, borrarla de tu máquina local con `docker rmi <image-name>`
