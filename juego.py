import pygame
import sys
from pygame.locals import *

# fundamental para que pygame se ejecute
pygame.init()

# creando una pantalla (ancho por alto en pixeles)
W, H = 1000, 600
PANTALLA = pygame.display.set_mode((W, H))
# para ajustar los FPS del juego
FPS = 60
RELOJ = pygame.time.Clock()

# título de la pantalla
pygame.display.set_caption("Mi primera ventana")

# paleta de colores RGB (en mayúsculas porque son constantes)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
H3DBE9A = (61, 190, 154)
H9285A9 = (146, 133, 169)

# --------- coloreando la pantalla
PANTALLA.fill(BLANCO)

# --------- dibujando un rectángulo
# (pantalla, color, (X, Y, largo, alto)) ----> las medidas son en pixeles
rectangulo1 = pygame.draw.rect(PANTALLA, ROJO, (100, 50, 100, 50))

# --------- dibujando una línea
# (pantalla, color, (X, Y), (X, Y), grosor en px)
# las primeras coordenadas son donde comienza la línea
# las segundas donde termina
pygame.draw.line(PANTALLA, VERDE, (100, 50), (200, 100), 4)

# --------- dibujando un circulo
# (pantalla, color, (X, Y), radio, relleno)
# las coordenadas son para el centro del circulo
# relleno en 0: quedará coloreado por completo
# entre más grande el número del relleno, más píxeles sin colorear por dentro
# por eje: 10 serán 10 píxeles por radio sin relleno
pygame.draw.circle(PANTALLA, NEGRO, (120, 120), 20, 10)

# --------- dibujando una elipse
# (pantalla, color (X, Y, ancho x, largo y), grosor)
pygame.draw.ellipse(PANTALLA, H9285A9, (200, 200, 40, 80), 10)


# --------- dibujando polígonos
# los puntos son tuplas de x, y
# linea
puntos = [(50, 300), (50, 100)]
pygame.draw.polygon(PANTALLA, (0, 150, 255), puntos, 8)
# triángulo
puntos = [(300, 300), (300, 100), (350, 100)]
pygame.draw.polygon(PANTALLA, (0, 150, 255), puntos, 8)


# --------- ÍCONO Y TÍTULO
pygame.display.set_caption("Jueguito")
icono = pygame.image.load("recursos/icono.png") # cargo la imagen
pygame.display.set_icon(icono)

# --------- FONDO
# importante que el tamaño en píxeles de la imagen coincida con el de la ventana
fondo = pygame.image.load("recursos/fondos/abandonCity/ajustado.png").convert() #convert optimiza el juego
x = 0

# bucle para ejecutar la pantalla
while True:
    # registrando todos los eventos del sistema
    for event in pygame.event.get():
        # cerrar la pantalla
        if event.type == pygame.QUIT:
            sys.exit()
    # para que el fondo se mueva
    x_relativa = x % fondo.get_rect().width # obtengo el ancho del fondo y lo divido por x
    PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))

    if x_relativa < W:
        PANTALLA.blit(fondo, (x_relativa, 0))
    x -= 5
    # para que se actualice la pantalla constantemente
    pygame.display.update()
    RELOJ.tick(FPS)
