# Importa funciones específicas de la biblioteca 'turtle' y un método 'line' de 'freegames'
from turtle import *
from freegames import line

# Define una función para dibujar la cuadrícula del juego de gato
def grid():
    # Dibuja líneas verticales de la cuadrícula
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    # Dibuja líneas horizontales de la cuadrícula
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

# Define la función para dibujar una 'X' en la posición (x, y)
def drawx(x, y):
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)

# Define la función para dibujar un 'O' en la posición (x, y)
def drawo(x, y):
    up()  # Levanta el lápiz para no dibujar mientras se mueve
    goto(x + 67, y + 5)  # Mueve el lápiz a la posición inicial para el círculo
    down()  # Baja el lápiz para empezar a dibujar
    circle(62)  # Dibuja un círculo de radio 62

# Función para normalizar las coordenadas de los clics a la cuadrícula del juego
def floor(value):
    return ((value + 200) // 133) * 133 - 200

# Estado inicial del juego, indicando quién es el jugador actual (0 = X, 1 = O)
state = {'player': 0}
players = [drawx, drawo]  # Lista de funciones de dibujo para cada jugador

# Función llamada en cada clic en la pantalla
def tap(x, y):
    x = floor(x)  # Normaliza la coordenada x
    y = floor(y)  # Normaliza la coordenada y
    player = state['player']  # Obtiene el jugador actual
    draw = players[player]  # Obtiene la función de dibujo del jugador actual
    draw(x, y)  # Dibuja la marca en la posición clickeada
    update()  # Actualiza la pantalla de turtle
    state['player'] = not player  # Cambia el jugador

# Configura la ventana del juego
setup(420, 420, 370, 0)
hideturtle()  # Oculta la tortuga para que no se vea en la ventana
tracer(False)  # Desactiva la animación de turtle para dibujar instantáneamente
grid()  # Dibuja la cuadrícula del juego
update()  # Actualiza la pantalla
onscreenclick(tap)  # Establece la función 'tap' como handler de clics en la pantalla
done()  # Inicia el bucle de eventos de turtle
