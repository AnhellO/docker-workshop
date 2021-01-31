# Resumen - 7ta Sesión

- Dudas técnicas con la instalación de `Docker`
- Revisamos práctica de la [sesión pasada](../sesion-6/TAREA.md) y dudas de la misma
  - Se propuso el uso de `restart: on-failure:{N}`
- Se trabajó sobre el laboratorio 11
  - Repasamos sobre volúmenes
  - Platicamos sobre los settings específicos del archivo `docker-compose.yml`
    - Especificación completa: <https://docs.docker.com/compose/compose-file/compose-file-v3/>
  - Consumimos nuestra pequeña `API` utilizando `Postman`, `Insomnia` y `curl`
  - Utilizamos la combinación de docker bind-mount volumes + `docker restart` para poder aplicar cambios inmediatos a la aplicación
- Se revisó también el laboratorio 12
  - Revisamos como utilizar un mismo `Dockerfile` para múltiples contenedores/servicios
  - Revisamos algunas nuevas settings para configuración
  - Vimos como montar más de un volúmen a un servicio
