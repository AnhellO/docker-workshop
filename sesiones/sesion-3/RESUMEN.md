# Resumen - 3ra Sesión

- Revisión de práctica de tarea de la sesión pasada
  - Dudas, preguntas y problemas
  - Se proponen soluciones en la carpeta de [`sesion-2/soluciones`](../sesion-2/soluciones/)
  - Analizamos `Dockerfile` spec <https://docs.docker.com/engine/reference/builder/>
- Revisión de lecturas de `Docker`
  - Se hicieron algunos ajustes para ir trabajando el capítulo 5 del libro `The Docker Book` por partes
- Continuamos jugando con los [laboratorios](../../laboratorios/)
  - Laboratorio 3
    - `docker build`: Construye imágenes
    - `docker push`: Envíamos imágenes a un registro remoto
    - Se aplicaron algunos cambios a la app de pokepy, y se taggearon nuevas imágenes que se subieron a `DockerHub`: <https://hub.docker.com/repository/docker/anhellojz/pokepy>
  - Laboratorio 4
    - Revisamos diferencias entre los 3 tipos de volúmenes en `Docker`
    - Seguimos la guía descrita en el laboratorio
    - `docker volume`: para administrar volúmenes
      - `--help`: para ver ayuda
    - `docker restart`: reiniciamos un contenedor
      - `--help`: para ver ayuda
  - Utilizamos `bind` volumes para poder aplicar cambios al laboratorio 3 y no tener que reconstruir la imágen
  