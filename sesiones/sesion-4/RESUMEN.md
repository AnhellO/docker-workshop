# Resumen - 4ta Sesión

- Revisamos problemas y dudas con las prácticas pasadas
- Revisando docker networks
- Revisando [drivers disponibles](https://docs.docker.com/network/) en las networks
- Jugamos con el [`laboratorio-5`](../../laboratorios/laboratorio-5/README.md)
- Creamos el [`laboratorio-6`](../../laboratorios/laboratorio-6/README.md) en el proceso, partiendo de la solución propuesta para la tarea en la [2da sesión](../sesion-2/TAREA.md)
- Vimos algunos comandos nuevos en el proceso
  - `docker network`: cliente CLI de docker para administrar redes
    - `--help`: ayuda disponible
    - `ls`: lista las redes existentes
    - `create`: crea una nueva red
    - `rm`: borra una red
    - `inspect`: inspecciona una red
  - Para `docker run`:
    - Volvimos a repasar variables de ambiente conla opción `-e ENV=value`
    - Utilizamos el `--network` para ejecutar los contenedores dentro de nuestras propias redes customizadas
    - Utilizamos la opción `--hostname` para especificar un nombre de host custom para el contenedor
- Concluímos con el tema completo de las [capas de docker](../sesion-1/docker-layers.png), cubriendo los diferentes sub-clientes de CLI en el proceso
