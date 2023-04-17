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
    def __int__(self):
        # Heredo el init de la clase Sprite de Pygame
        super().__init__()

        # Rectángulo (jugador)
        self.image = pygame.Surface((200, 200))
        self.image.fill(H_FA2F2F)

        #Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()

        # Centra el rectángulo (sprite)
        self.rect.center = (ANCHO // 2, ALTO // 2)

    def update(self):
        pass