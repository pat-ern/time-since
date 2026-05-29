# Contador de días sin usar algo

Aplicación de terminal en Python que permite crear contadores con persistencia local en un archivo de texto.

## Funcionalidades

- Agregar un nuevo contador
- Consultar todos los contadores
- Consultar un contador por nombre
- Eliminar un contador
- Guarda fecha y hora de inicio para mayor precisión

## Uso

Desde la carpeta del proyecto:

```bash
python3 counter.py add instagram -n "Días sin Instagram"
python3 counter.py list
python3 counter.py show instagram
```

El archivo de datos se guarda como `counters.txt` en la misma carpeta.
