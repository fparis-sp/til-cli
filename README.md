# TIL CLI - Today I Learned

Un diario de aprendizaje desde la terminal. Guarda lo que aprendes cada día.

## Requisitos

- Python 3.12+

## Uso

```bash
# Añadir una entrada
python til.py add "Hoy aprendí que Python tiene walrus operator :="

# Añadir con etiquetas
python til.py add "Los decoradores son funciones que envuelven otras funciones" --tag python --tag basics

# Listar todas las entradas
python til.py list

# Listar solo las de hoy
python til.py list --today

# Filtrar por etiqueta
python til.py list --tag python

# Buscar en el contenido
python til.py search "decoradores"

# Eliminar una entrada
python til.py delete 1
```

## Dónde se guardan los datos

Las entradas se guardan en `~/.til/entries.json`.

## Estructura del proyecto

```
til-cli/
├── til.py              # Punto de entrada (CLI)
├── src/
│   ├── models.py       # Modelo de datos (Entry)
│   ├── storage.py      # Lectura/escritura JSON
│   └── commands.py     # Lógica de comandos
└── tests/              # Tests (vacío por ahora)
```
