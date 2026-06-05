# Contador de días

Aplicación de terminal en Python para llevar contadores personales con persistencia local en un archivo de texto. Permite crear, listar, consultar y eliminar contadores, y almacena la fecha y hora exacta de inicio para un seguimiento más preciso.

## Funcionalidades

- `python3 counter.py add <nombre> -n "nota"`: agregar un nuevo contador con nombre y nota opcional.
- `python3 counter.py list`: consultar todos los contadores registrados, mostrando el tiempo transcurrido en días, horas y minutos.
- `python3 counter.py show <nombre>`: consultar un contador por nombre.
- `python3 counter.py reset <nombre>`: reiniciar el inicio de un contador al momento actual; el comando solicitará confirmación antes de aplicar el cambio.
- `python3 counter.py delete <nombre>`: eliminar un contador, con confirmación interactiva antes de borrar.
- `python3 counter.py list` y `python3 counter.py show <nombre>` muestran la información en una tabla con bordes coloreados y el nombre del contador resaltado.

## Notas

- Los datos se guardan en `counters.txt` en la misma carpeta del proyecto.
- El formato de inicio es `YYYY-MM-DD HH:MM`.

## Uso directo desde Bash

Para usar el comando `counter` directamente desde cualquier carpeta, agrega este directorio al `PATH` de Bash:

```bash
export PATH="$PATH:$HOME/repositories/counter"
```

Luego puedes ejecutar:

```bash
counter add instagram -n "Días sin Instagram"
counter list
counter show instagram
counter reset instagram
counter delete instagram
```

Si quieres que esta configuración se aplique en todas tus sesiones, añade la línea anterior a `~/.bashrc`.
