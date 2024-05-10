"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
# Establecer el título de la ventana de la aplicación
title("Memoria")
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


tap_count = 0  # Inicializamos el contador de taps
juego_terminado = True  # Inicializamos la variable que indica si el juego ha terminado

def tap(x, y):
    global tap_count, juego_terminado  # Agregar la variable juego_terminado como global

    if all(hide[i] == False for i in range(len(hide))):
        juego_terminado = False
    if not juego_terminado:
        return  # Si el juego no está activo, no procesar el tap

    # Obtener las coordenadas del centro de la casilla más cercana al punto (x, y)
    spot_x = int(x // 50) * 50 + 25  # Calcula la coordenada x del centro de la casilla
    spot_y = int(y // 50) * 50 + 25  # Calcula la coordenada y del centro de la casilla

    # Verificar si el punto (x, y) está dentro del área visible de la pantalla (410x410)
    if (-205 <= spot_x <= 205) and (-205 <= spot_y <= 205):
        spot = index(spot_x, spot_y)
        mark = state['mark']

        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
        else:
            hide[spot] = False
            hide[mark] = False
            state['mark'] = None

        # Incrementamos el contador de taps después de procesar el tap
        tap_count += 1

    else:
        # El tap está fuera del área visible de la pantalla, no hacer nada
        pass


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Verificar si todas las fichas están reveladas
    if all(hide[i] == False for i in range(len(hide))):
        mensaje_ganaste()

    update()
    update_tap_count()
    ontimer(draw, 100)


def update_tap_count():
    """Update tap count display on screen."""
    penup()
    goto(-180, 210)
    color('black')
    write(f"Taps: {tap_count}", font=('Arial', 20, 'normal'))


def mensaje_ganaste():
    """Mostrar mensaje de 'Ganaste!!!'."""
    penup()
    goto(0, 0)
    color('green')
    write("Ganaste!!!", align='center', font=('Arial', 30, 'normal'))


shuffle(tiles)
setup(500, 500, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
