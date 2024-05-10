# Juegos-python
#### Pac-man, Tic-Tac-Toe, Memoria

## Cómo ejecutar los archivos de juegos

#### Para ejecutar los archivos `pac_man.py`, `tic_tac_toe.py` y `memoria.py`, sigue estos pasos:

1. **Verificar la instalación de Python:**

##### Para asegurarte de que Python está instalado en tu sistema, ejecuta alguno de los siguientes comandos en tu terminal:

   ```bash
   python3 --version

   python --version
   ```

##### Si Python está instalado correctamente, verás la versión instalada. Si no está instalado, puedes descargarlo desde python.org e instalarlo siguiendo las instrucciones.

1. **Instalar el módulo pip de Python (si no está instalado):**
- https://pip.pypa.io/en/stable/installation/Links to an external site.
- Descarga el archivo: https://bootstrap.pypa.io/get-pip.pyLinks to an external site.
- Ejecutalo como un script de Python:

```bash
   python get-pip.py 
```

1. **Instalar el módulo Free Python Games**
##### El módulo Free Python Games es necesario para ejecutar los archivos de juegos. Si no lo tienes instalado, puedes hacerlo con el siguiente comando:

```bash
   python3 -m pip install freegames

    python -m pip install freegames
```

##### Luego ejecuta este comando, para saber si se instalo bien.

```bash
   python3 -m freegames --help

    python -m freegames --help
```

1. **Una vez que hayas seguido estos pasos y todo esté instalado correctamente, podrás utilizar los archivos**


## Memoria.

##### Codigo obtenido de:

##### Memory — Free Python Games 2.5.3 documentation. (2017). Grantjenks.com. https://grantjenks.com/docs/freegames/memory.html

## Cambios realizados:

1. Se agrandó el tamaño de la pantalla.
1. Se agregó un contador para los taps que el usuario da.
1. Se validó que el usuario solo pueda dar taps en la cuadrícula.
1. Se agregó un mensaje de "Ganaste!!!".
1. Se validó que cuando el usuario gana no se puedan dar más taps.
1. Se corrigió el código usando el formato PEP8, con ayuda de flake8.