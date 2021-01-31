# Ejercicios

Ejercicios propuestos para practicar lo visto en la 6ta sesión.

## Ejercicio 1

- Crear un archivo `docker-compose.yml` que ejecute **3** contenedores. Estos 3 contenedores serán una combinación de lo visto en los laboratorios 9 y 10:
  - **1er Contenedor:** Base de datos de `PostgreSQL`
  - **2do Contenedor:** `DBMS` de `PgAdmin` para poder revisar las base de datos a través de localhost
  - **3er Contenedor:** Este se encargará de ejecutar el script de operaciones `CRUD` de `python` o `GO`, tú decides cual elegir
    - Agrega una función extra para insertar `N` registros, donde `N` puede ser cualquier número entre `1` y `1000`
