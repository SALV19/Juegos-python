"""
Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *
from freegames import line


def grid():
    # Dibujar el tablero mediante líneas rectas
    line(70, 200, 70, -200)
    line(-70, 200, -70, -200)
    line(-200, -70, 200, -70)
    line(-200, 70, 200, 70)



def drawx(x, y):
    # Dibujar pieza del jugador X
    line(x - 70, y - 70, x + 70, y + 70)
    line(x - 70, y + 70, x + 70, y - 70)


def drawo(x, y):
    # Dibujar pieza del jugador O
    up()
    goto(x, y - 62)
    down()
    circle(62)


def floor(value):
    # Redondear valor del click con 130 para centrar la posición a dibujar
    # return ((value + 200) // 130) * 130 - 200
    return ((value + 200) // 130) * 140 - 140


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)

    print(f"X: {x}, Y: {y}")

    player = state['player']
    draw = players[player]

    # Actualizar pantalla / buffer
    draw(x, y)
    update()

    # Intercambiar jugador
    state['player'] = not player


setup(420, 420)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
