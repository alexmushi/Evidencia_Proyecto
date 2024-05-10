# Importa funciones
from turtle import (
    color, up, down, goto, circle, setup,
    hideturtle, tracer, update, onscreenclick,
    done
)
from freegames import line


def grid():
    # Dibuja líneas verticales de la cuadrícula
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    # Dibuja líneas horizontales de la cuadrícula
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    color('red')  # Establece el color del lápiz a rojo
    line(x + 17, y + 17, x + 117, y + 117)
    line(x + 17, y + 117, x + 117, y + 17)


def drawo(x, y):
    color('blue')  # Establece el color del lápiz a azul
    up()  # Levanta el lápiz para no dibujar mientras se mueve
    goto(x + 67, y + 17)
    down()
    circle(50)


def floor(value):
    return ((value + 200) // 133) * 133 - 200


board = {}  # Diccionario para rastrear el estado de cada celda

state = {'player': 0}
players = [drawx, drawo]  # Lista de funciones de dibujo para cada jugador


def tap(x, y):
    x = floor(x)  # Normaliza la coordenada x
    y = floor(y)  # Normaliza la coordenada y
    key = (x, y)  # Crea una tupla con las coordenadas normalizadas
    if key in board:
        return  # Si la celda está ocupada, no hace nada
    board[key] = state['player']  # Guarda el jugador en la celda
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player  # Cambia el jugador


# Configura la ventana del juego
setup(420, 420, 370, 0)
hideturtle()  # Oculta la tortuga para que no se vea en la ventana
tracer(False)  # Desactiva la animación de turtle para dibujar instantáneamente
grid()
update()
onscreenclick(tap)
done()  # Inicia el bucle de eventos de turtle
