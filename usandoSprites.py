import pygame

# Tamaño de pantalla
ANCHO = 800
ALTO = 600

# FPS
FPS = 30

# Paleta de colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
H_FA2F2F = (250, 47, 47)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
H_50D2FE = (94, 210, 244)

class Jugador (pygame.sprite.Sprite):
    # Sprite del jugador
    """ Hereda métodos y atributos de la clase Sprite de Pygame
    Sprite es una clase usada para representar objetos en un juego, tales
    como personakes, enemigos, obstáculos, etc"""

    def __int__(self):
        # Heredo el init de la clase Sprite de Pygame
        super().__init__()

        """ Creo una superficie (surface) de color rojo oscuro (definido como
        una constante previamente), que es el color de fondo de la imagen 
        del jugador."""
        self.image = pygame.Surface((200, 200))
        self.image.fill(H_FA2F2F)

        """ Obtengo el rectángulo que rodea a la superficie del jugador, 
        utilizando el método get_rect() de la superficie. 
        El rectángulo se utiliza para detectar colisiones entre el jugador 
        y otros objetos en el juego."""
        self.rect = self.image.get_rect()

        # Centro el rectángulo (jugador)
        # mediante división para que cambie si modifico ANCHO y ALTO después
        self.rect.center = (ANCHO // 2, ALTO // 2) # (300, 400)

    def update(self):
        # Actualiza esto cada vuelta de bucle

        """ Actualizo la posición del rectángulo del jugador en el eje y,
        moviéndolo hacia abajo en la ventana del juego."""
        self.rect.y += 10

        """ Verifico si el borde superior del rectángulo del jugador ha 
        pasado el borde inferior de la ventana del juego"""
        if self.rect.top > ALTO:
            self.rect.bottom = 0 # Su posición se restablece en la parte superior de la ventana
