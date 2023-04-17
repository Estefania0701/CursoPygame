import pygame
import sys
from pygame.locals import *

# fundamental para que pygame se ejecute
pygame.init()

# creando una pantalla (ancho por alto en pixeles)
W, H = 1000, 600
PANTALLA = pygame.display.set_mode((W, H))

# --------- TÍTULO E ÍCONO
pygame.display.set_caption("Jueguito")
icono = pygame.image.load("recursos/icono.png") # cargo la imagen
pygame.display.set_icon(icono)

# --------- FONDO
# importante que el tamaño en píxeles de la imagen coincida con el de la ventana
fondo = pygame.image.load("recursos/fondos/abandonCity/ajustado.png").convert() #convert optimiza el juego

# ---------- PERSONAJE
quieto = pygame.image.load("recursos/sprites/personaje/idle1.png")


# ------------------------------- ANIMACIONES -------------------------

# ---------- HACIA LA DERECHA
caminaDerecha = [pygame.image.load("recursos/sprites/personaje/run1.png"),
                 pygame.image.load("recursos/sprites/personaje/run2.png"),
                 pygame.image.load("recursos/sprites/personaje/run3.png"),
                 pygame.image.load("recursos/sprites/personaje/run4.png"),
                 pygame.image.load("recursos/sprites/personaje/run5.png"),
                 pygame.image.load("recursos/sprites/personaje/run6.png")]

# ---------- HACIA LA IZQUIERDA
caminaIzquierda = [pygame.image.load("recursos/sprites/personaje/run1-izq.png"),
                 pygame.image.load("recursos/sprites/personaje/run2-izq.png"),
                 pygame.image.load("recursos/sprites/personaje/run3-izq.png"),
                 pygame.image.load("recursos/sprites/personaje/run4-izq.png"),
                 pygame.image.load("recursos/sprites/personaje/run5-izq.png"),
                 pygame.image.load("recursos/sprites/personaje/run6-izq.png")]

# ---------- SALTA
salta = [pygame.image.load("recursos/sprites/personaje/jump1.png"),
         pygame.image.load("recursos/sprites/personaje/jump2.png")]


# --------------------------------- SONIDOS -----------------------------

# --------- MÚSICA DE FONDO
pygame.mixer.music.load("recursos/sonidos/sonido_intergalactic_odyssey.ogg")
pygame.mixer.music.play(-1) # reproduce la música (-1: infinito, 1 para 1 vez, 5 para 5 veces...)

# --------- Indicador de volumen
sonido_arriba = pygame.image.load("recursos/sonidos/volumen/volume_up.png")
sonido_abajo = pygame.image.load("recursos/sonidos/volumen/volume_down.png")
sonido_mute = pygame.image.load("recursos/sonidos/volumen/volume_muted.png")
sonido_max = pygame.image.load("recursos/sonidos/volumen/volume_max.png")

x = 0
px = 50
py = 200
ancho = 40
velocidad = 10

# Control de FPS
reloj = pygame.time.Clock()

# variables salto
salto = False
# altura del salto
cuentaSalto = 10

# variables dirección
izquierda = False
derecha = False

# pasos
cuentaPasos = 0

# movimiento
def recargaPantalla():
    # variables globales
    global cuentaPasos
    global x

    # fondo en movimiento
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < W:
        PANTALLA.blit(fondo, (x_relativa, 0))
    x -= 5

    # contador de pasos
    if cuentaPasos + 1 >= 6: # 6 por ser 6 imagenes de run
        cuentaPasos = 0

    # movimiento a la izquierda
    if izquierda:
        PANTALLA.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1
    # movimiento a la derecha
    elif derecha:
        PANTALLA.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1
    elif salto + 1 >= 2: # 2 porque solo hay 2 imágenes de jump
        cuentaPasos = 0
        PANTALLA.blit(salta[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1
    else:
        PANTALLA.blit(quieto, (int(px), int(py)))

    # actualización de la ventana
    pygame.display.update()

ejecuta = True

# bucle de acciones y controles
while ejecuta:
    # FPS
    reloj.tick(18)

    # Bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    # tecla pulsada
    # permite que se pueda dejar pulsada una tecla para repetir
    # de forma continua una acción
    keys = pygame.key.get_pressed()

    # tecla A - Movimiento a a izquierda
    if keys[pygame.K_a] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False
    # tecla D - Movimiento a la derecha
    elif keys[pygame.K_d] and px < (900 - velocidad - ancho):
        px += velocidad
        izquierda = False
        derecha = True
    # personaje quieto:
    else:
        izquierda = False
        derecha = False
        cuentaPasos = 0

    # Tecla W - movimiento hacia arriba
    if keys[pygame.K_w] and py > 100:
        py -= velocidad

    # Tecla S - movimiento hacia abajo
    if keys[pygame.K_s] and py < 300:
        py += velocidad

    # Tecla SPACE - SALTO
    if not (salto):
        if keys[pygame.K_SPACE]:
            salto = True
            izquierda = False
            derecha = False
            cuentaPasos = 0
    else:
        if cuentaSalto >= -10:
            py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
            cuentaSalto -= 1
        else:
            cuentaSalto = 10
            salto = False


    # ---- control de la música de fondo
    volumen = pygame.mixer.music.get_volume()
    # Baja volumen
    if keys[pygame.K_9] and volumen > 0.0:
        pygame.mixer.music.set_volume(volumen - 0.01)
        PANTALLA.blit(sonido_abajo, (850, 25))
    elif keys[pygame.K_9] and volumen == 0.0:
        PANTALLA.blit(sonido_mute, (850, 25))

    # Sube volumen
    if keys[pygame.K_0] and volumen < 1.0:
        pygame.mixer.music.set_volume(volumen + 0.01)
        PANTALLA.blit(sonido_arriba, (850, 25))
    elif keys[pygame.K_0] and volumen == 1.0:
        PANTALLA.blit(sonido_max, (850, 25))

    # Mutear
    elif keys[pygame.K_m]:
        pygame.mixer.music.set_volume(0.0)
        PANTALLA.blit(sonido_mute, (850, 25))

    # Desmutear
    elif keys[pygame.K_COMMA]:
        pygame.mixer.music.set_volume(1.0)
        PANTALLA.blit(sonido_max, (850, 25))

    # actualización de la ventana
    pygame.display.update()
    # llamada a la función de actualización de la ventana
    recargaPantalla()

# salida del juego
pygame.quit()




# salida del juego
