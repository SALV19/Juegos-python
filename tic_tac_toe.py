import turtle as tr
from freegames import line


def grid():
    # Dibujar el tablero mediante líneas rectas
    line(70, 200, 70, -200)
    line(-70, 200, -70, -200)
    line(-200, -70, 200, -70)
    line(-200, 70, 200, 70)


def actualizar_tablero(x, y, tablero):
    x_0 = int((x + 140) / 140)
    y_0 = int((y + 140) / 140)
    tablero[x_0][y_0] = 1
    return tablero


def validar_tablero(x, y, tablero):
    x_0 = int((x + 140) / 140)
    y_0 = int((y + 140) / 140)
    if (tablero[x_0][y_0] != 1):
        return True
    else:
        return False


def drawx(x, y):
    # Dibujar pieza del jugador X
    size = 40
    tr.color("red")
    line(x - size, y - size, x + size, y + size)
    line(x - size, y + size, x + size, y - size)


def drawo(x, y):
    # Dibujar pieza del jugador O
    radio = 50
    tr.up()
    tr.goto(x, y - radio)
    tr.down()
    tr.color("blue")
    tr.circle(radio)


def floor(value):
    # Redondear valor del click con 130 para centrar la posición a dibujar
    # return ((value + 200) // 130) * 130 - 200
    return ((value + 200) // 130) * 140 - 140


state = {'player': 0}
players = [drawx, drawo]
tablero = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
            ]


def tap(x, y):
    """Draw X or O in tapped square."""
    global tablero

    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]

    if (validar_tablero(x, y, tablero)):
        tablero = actualizar_tablero(x, y, tablero)
        draw(x, y)
        tr.update()
        # Intercambiar jugador
        state['player'] = not player


tr.setup(420, 420)
tr.hideturtle()
tr.tracer(False)
tr.grid()
tr.update()
tr.onscreenclick(tap)
tr.done()
