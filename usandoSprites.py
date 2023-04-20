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
        self.rect.center = (ANCHO // 2, ALTO // 2)

    def update(self):
        pass