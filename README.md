# Juegos-python
#### Pac-man, Tic-Tac-Toe y Memoria

## ¿Cómo ejecutar los archivos de juegos?

#### Para ejecutar los archivos `pac_man.py`, `tic_tac_toe.py` y `memoria.py`, sigue estos pasos:

1. **Verificar la instalación de Python:**

##### Para asegurarte de que Python está instalado en tu sistema, ejecuta alguno de los siguientes comandos en tu terminal:

```bash
python3 --version
```

```bash
python --version
```

##### Luego ejecuta este comando, tedara la versión instalada que tengas de python.

##### Si Python está instalado correctamente, verás la versión instalada. Si no está instalado, puedes descargarlo desde python.org e instalarlo siguiendo las instrucciones.

2. **Instalar el módulo pip de Python (si no está instalado):**
- https://pip.pypa.io/en/stable/installation/Links to an external site.
- Descarga el archivo: https://bootstrap.pypa.io/get-pip.pyLinks to an external site.
- Ejecutalo como un script de Python:

```bash
   python get-pip.py 
```

3. **Instalar el módulo Free Python Games**
##### El módulo Free Python Games es necesario para ejecutar los archivos de juegos. Si no lo tienes instalado, puedes hacerlo con el siguiente comando:

```bash
   python3 -m pip install freegames
```

```bash
    python -m pip install freegames
```

##### Luego ejecuta este comando, para saber si se instalo bien.

```bash
   python3 -m freegames --help
```

```bash
    python -m freegames --help
```

4. **Una vez que hayas seguido estos pasos y todo esté instalado correctamente, podrás utilizar los archivos**


## Tic-Tac-Toe.

##### Codigo obtenido de:

##### Tic Tac Toe — Free Python Games 2.5.3 documentation. (2017). Grantjenks.com. https://grantjenks.com/docs/freegames/tictactoe.html

## Cambios realizados:

1. Se escaló la cuadrícula del tablero para que esté centrada en la ventana.
1. Se centraron y reescalaron las X y O en la cuadrícula.
1. Se les cambió de color a las X y O a rojo y azul respectivamente.
1. Se valida la casilla antes de dibujar la siguiente ficha. 
1. Se corrigió el código siguiendo el formato Pep8


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

## PAC-MAN.

##### Codigo obtenido de:

##### PAC-MAN  — Free Python Games 2.5.3 documentation. (2017). Grantjenks.com. https://grantjenks.com/docs/freegames/pacman.html

## Cambios realizados
1. Se adapto al formato PeP8.
2. Se cambio el mapa.
3. Los Fantasmas son más rápidos.
4. Comentarios en español

