"""Memory, juego de rompecabezas de pares de números.

Ejercicios:

1. Contar e imprimir cuántos toques ocurren.
2. Disminuir el número de fichas a una cuadrícula de 4x4.
3. Detectar cuando todas las fichas están reveladas.
4. Centrar la ficha de un solo dígito.
5. Usar letras en lugar de fichas.
"""

import random as rand
import turtle as t

from freegames import path

# Cargar imagen del memoria (car.gif)
car = path('car.gif')

# Establecer el título de la ventana
t.title("Memoria")

# Crear una lista de fichas con pares de números (de 0 a 31)
tiles = list(range(32)) * 2

# Estado inicial del juego: todas las fichas ocultas
state = {'mark': None}

# Crear una lista para rastrear si cada ficha está oculta o revelada
hide = [True] * 64


# Función para dibujar un cuadrado blanco con contorno negro en (x, y)
def square(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.color('black', 'white')
    t.begin_fill()
    for count in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()


# Función para convertir coordenadas (x, y) a índice de fichas
def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


# Función para convertir contador de fichas a coordenadas (x, y)
def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


# Inicializamos el contador de taps
tap_count = 0

# Inicializamos la variable que indica si el juego ha terminado
juego_terminado = True


# Función para manejar toques en la pantalla
def tap(x, y):
    # Agregar la variable juego_terminado como global
    global tap_count, juego_terminado

    # Verificar si el juego ha terminado
    if all(hide[i] is False for i in range(len(hide))):
        juego_terminado = False
    if not juego_terminado:
        return

    # Obtener las coordenadas del cuadro más cercano al punto (x, y)
    spot_x = int(x // 50) * 50 + 25
    spot_y = int(y // 50) * 50 + 25

    # Verificar si el punto (x, y) está dentro del área de juego
    if (-205 <= spot_x <= 205) and (-205 <= spot_y <= 205):
        spot = index(spot_x, spot_y)
        mark = state['mark']

        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
        else:
            hide[spot] = False
            hide[mark] = False
            state['mark'] = None

        tap_count += 1

    else:
        # El tap está fuera del área visible de la pantalla, no hacer nada
        pass


# Función para dibujar la imagen y las fichas
def draw():
    t.clear()
    t.goto(0, 0)
    t.shape(car)
    t.stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        t.up()
        t.goto(x + 2, y)
        t.color('black')
        t.write(tiles[mark], font=('Arial', 30, 'normal'))

    # Verificar si todas las fichas están reveladas
    if all(hide[i] is False for i in range(len(hide))):
        mensaje_ganaste()

    t.update()
    update_tap_count()
    t.ontimer(draw, 100)


# Función para actualizar el contador de taps en la pantalla
def update_tap_count():
    t.penup()
    t.goto(-180, 210)
    t.color('black')
    t.write(f"Taps: {tap_count}", font=('Arial', 20, 'normal'))


# Función para mostrar mensaje de 'Ganaste!!!'
def mensaje_ganaste():
    t.penup()
    t.goto(0, 0)
    t.color('green')
    t.write("Ganaste!!!", align='center', font=('Arial', 30, 'normal'))


# Mezclar las fichas
rand.shuffle(tiles)

# Inicializar la ventana de juego
t.setup(500, 500, 370, 0)

# Configurar la imagen del carro
t.addshape(car)

# Ocultar la tortuga y desactivar la animación
t.hideturtle()

# Desactivar el rastreo de la tortuga
t.tracer(False)

# Asignar la función tap al evento de toque en la pantalla
t.onscreenclick(tap)

# Dibujar la pantalla
draw()

# Mantener la ventana abierta
t.done()
