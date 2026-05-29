# Contador de días sin usar algo

Aplicación de terminal en Python para llevar contadores personales con persistencia local en un archivo de texto. Permite crear, listar, consultar y eliminar contadores, y almacena la fecha y hora exacta de inicio para un seguimiento más preciso.

## Funcionalidades

- `python3 counter.py add <nombre> -n "nota"`: agregar un nuevo contador con nombre y nota opcional.
- `python3 counter.py list`: consultar todos los contadores registrados, mostrando el tiempo transcurrido en días, horas y minutos.
- `python3 counter.py show <nombre>`: consultar un contador por nombre.
- `python3 counter.py delete <nombre>`: eliminar un contador, con confirmación interactiva antes de borrar.

## Notas

- Los datos se guardan en `counters.txt` en la misma carpeta del proyecto.
- El formato de inicio es `YYYY-MM-DD HH:MM`.
