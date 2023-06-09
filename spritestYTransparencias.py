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


class Jugador(pygame.sprite.Sprite):
    """ Hereda métodos y atributos de la clase Sprite de Pygame
    Sprite es una clase usada para representar objetos en un juego, tales
    como personakes, enemigos, obstáculos, etc"""

    def __init__(self):
        # Método constructor

        # Heredo el init de la clase Sprite de Pygame
        super().__init__()

        """ Creo una superficie (surface) de color rojo oscuro (definido como
        una constante previamente), que es el color de fondo de la imagen 
        del jugador."""
        self.image = pygame.image.load("recursos/car.png")

        # redimensiono la imagen porque la original es muy grande (640, 320)
        self.image = pygame.transform.scale(self.image, (100, 50))

        """convert() es un método que se puede llamar en una superficie 
        (Surface) para convertirla al formato de píxel óptimo para la 
        pantalla donde se mostrará. Esta conversión se realiza para mejorar 
        el rendimiento, ya que el formato óptimo de píxel es más rápido de 
        renderizar."""
        self.image.convert()

        """ Obtengo el rectángulo que rodea a la superficie del jugador, 
        utilizando el método get_rect() de la superficie. El rectángulo 
        se utiliza para detectar colisiones entre el jugador y otros objetos 
        en el juego."""
        self.rect = self.image.get_rect()

        # Centro el rectángulo (jugador)
        # mediante división para que cambie si modifico ANCHO y ALTO después
        self.rect.center = (ANCHO // 2, ALTO // 2)  # (300, 400)

    def update(self):
        """ Actualiza el estado de un sprite en cada ciclo del bucle principal
        del juego. Se puede sobrescribir para controlar el movimiento y la
        interacción del jugador con otros objetos en el juego"""

        """ Actualizo la posición del rectángulo del jugador en el eje x,
        moviéndolo hacia la derecha"""
        self.rect.x += 10

        """ Verifico si el borde izquierdo del rectángulo del jugador ha 
        pasado el borde derecho de la ventana del juego"""
        if self.rect.left > ANCHO:
            self.rect.right = 0  # Su posición se restablece en la parte izquierda


# ------------------------------------------------------------------------

# Inicializo todos los módulos de Pygame
pygame.init()

# Creo una ventana para mostrar el juego, asignándole dimensiones
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Establezco un título para la ventana
pygame.display.set_caption("Trabajando con Sprites")

""" Creo un objeto Clock de Pygame que se utiliza para controlar la 
velocidad de cuadros del juego. Este objeto se utiliza en el bucle 
principal del juego para asegurarse de que el juego se ejecute a una 
velocidad constante y no se ralentice en exceso."""
clock = pygame.time.Clock()

# --------------------------- GRUPO DE SPRITES -------------------------------

"""Creo un grupo de sprites vacíos. Los grupos de sprites se utilizan 
para manejar y actualizar varios sprites simultáneamente"""
sprites = pygame.sprite.Group()

# Creo un objeto de tipo Jugador
jugador = Jugador()

"""Agrego el objeto jugador al grupo de sprites. Esto permite que el objeto 
jugador sea actualizado y dibujado en la ventana del juego junto con otros 
sprites que puedan estar presentes en el grupo sprites"""
sprites.add(jugador)

# ----------------------- BUCLE PRINCIPAL DEL JUEGO ---------------------------

ejecutando = True
while ejecutando:

    """ Limito la velocidad de fotogramas del juego al valor definido
    en la constante FPS"""
    clock.tick(FPS)

    # Para cerrar la ventana y detener el juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    # Actualizo el estado de cada sprite en el juego
    sprites.update()

    # Relleno la pantalla de color negro
    pantalla.fill(NEGRO)

    # Dibujo los sprites en la pantalla, con el método draw del grupo de sprites
    sprites.draw(pantalla)

    # Dibujo 2 líneas para crear un plano cartesiano
    pygame.draw.line(pantalla, H_50D2FE, (400, 0), (400, 800), 1)
    pygame.draw.line(pantalla, AZUL, (0, 300), (800, 300), 1)

    # Actualizo la ventana con los cambios realizados
    pygame.display.flip()

# Cierro todos los módulos Pygame que había inicializado antes
""" NOTA: Si no se llama a pygame.quit(), se pueden producir errores o 
conflictos en el sistema y el programa puede no cerrarse adecuadamente."""
pygame.quit()
