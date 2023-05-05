import pygame
import random

# Tamaño de pantalla
ANCHO = 1000
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

# --------- FONDO
# importante que el tamaño en píxeles de la imagen coincida con el de la ventana
fondo = pygame.image.load("recursos/juego_spaceShip/fondo_space.jpg")

# esclalo el fondo al tamaño de la ventana
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

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
        self.image = pygame.image.load("recursos/juego_spaceShip/space_ship.png")

        # redimensiono la imagen porque la original es muy grande (640, 320)
        self.image = pygame.transform.scale(self.image, (50, 50))

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

        # Posiciono el rectángulo
        # mediante división para que cambie si modifico ANCHO y ALTO después
        self.rect.center = (ANCHO // 2, 500)  # (300, 500)

        # ---------------------- Control con el teclado

        # posición inicial
        self.posicion_x = 0
        self.posicion_y = 0

    def update(self):

        # posición predeterminada (inicio del juego)
        self.posicion_x = 0
        self.posicion_y = 0

        # -------------------- TECLAS DE MOVIMIENTO ------------------------

        # obtengo las teclas
        teclas = pygame.key.get_pressed()

        # movimiento izquierda
        if teclas[pygame.K_a]:
            self.posicion_x -= 15
        # movimiento derecha
        if teclas[pygame.K_d]:
            self.posicion_x += 15
        # movimiento arriba
        if teclas[pygame.K_w]:
            self.posicion_y -= 15
        # movimiento abajo
        if teclas[pygame.K_s]:
            self.posicion_y += 15

        # disparo
        if teclas[pygame.K_SPACE]:
            self.disparar()
            self.disparar_alas()

        # Actualizo la posición del personaje
        self.rect.x += self.posicion_x
        self.rect.y += self.posicion_y

        # ------------------ MARGENES DE MOVIMIENTO ----------------------

        # si el lado derecho del rectángulo sobrepasa el borde derecho
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO # establezco la pos del lado derecho igual que el ANCHO
        # si el lado izquierdo del rectángulo sobrepasa el borde izquierdo
        if self.rect.left < 0:
            self.rect.left = 0  # establezo la pos del lado izquierdo en 0
        # si el lado inferior del rectángulo sobrepasa el borde inferior
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO # establezo la pos del lado inferior igual que el ALTO
        # si el lado superior del rectángulo sobrepasa el borde superior
        if self.rect.top < 0:
            self.rect.top = 0 # establezo la pos del lado superior en 0

    def disparar(self):
        # creo un objeto disparo y le paso como parámetro el centro del jugador y su borde superior
        bala = Disparo(self.rect.centerx, self.rect.top + 20)
        balas.add(bala)

    def disparar_alas(self):
        # creo un objeto disparo y le paso como parámetro el centro del jugador y su borde superior
        balaDerecha = Disparo(self.rect.centerx + 20, self.rect.top + 40)
        balas.add(balaDerecha)

        balaIzquierda = Disparo(self.rect.centerx - 20, self.rect.top + 40)
        balas.add(balaIzquierda)


class Enemigo(pygame.sprite.Sprite):
    # crea los objetos enemigos

    def __init__(self):
        super().__init__()

        # cargo la imagen
        self.image = pygame.image.load("recursos/juego_spaceShip/enemy.png")

        # la redimensiono
        self.image = pygame.transform.scale(self.image, (70, 35))

        # la convierto para optimizarla
        self.image.convert()

        # obtengo el rectángulo que rodea la imagen
        self.rect = self.image.get_rect()

        # -------------- APARICIÓN EN POSICIÓN ALEATORIA --------------
        # les resto el ancho para que no se salga del borde de la ventana
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)

        # velocidad del enemigo
        self.posicion_x = random.randrange(1,10)
        self.posicion_y = random.randrange(1,10)

    def update(self):
        # Actualizo la posición (velocidad) del enemigo
        self.rect.x += self.posicion_x
        self.rect.y += self.posicion_y

       # ------------------ MARGENES DE MOVIMIENTO ----------------------

        # al llegar a los bordes derecho o izquierdo
        if self.rect.right > ANCHO:
            self.posicion_x -= 1  # invierto la dirección en x
        if self.rect.left < 0:
            self.posicion_x += 1
        # al llegar a los bordes inferior o superior
        if self.rect.bottom > ALTO:
            self.posicion_y -= 1  # invierto la dirección en y
        if self.rect.top < 0:
            self.posicion_y += 1

class Disparo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("recursos/juego_spaceShip/disparo.png").convert()
        self.image.set_colorkey(NEGRO) # elimino fondo negro

        # redimensiono la imagen porque la original es muy grande
        self.image = pygame.transform.scale(self.image, (5, 15))

        # obtengo el rectángulo de la imagen
        self.rect = self.image.get_rect()

        # ubico el lado inferior del disparo de acuerdo a la y recibida como parámetro
        self.rect.bottom = y
        # centro el disparo de acuerdo a la x recibida como parámetro
        self.rect.centerx = x

    def update(self):
        self.rect.y -= 20 # velocidad del disparo (incremento hacia arriba)

        # si el disparo sale por el lado superior de la pantalla, se elimina
        if self.rect.bottom < 0:
            self.kill()




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

enemigos = pygame.sprite.Group()

balas = pygame.sprite.Group()


# -------------- ENEMIGOS
# los ubico de primeras para que el jugador quede en la capa superior

# rango de 0 a 5 (+1 es para que siempre aparezca por lo menos 1 enemigo)
"""for i in range(random.randrange(4) + 1):
    enemigo = Enemigo()
    enemigos.add(enemigo)"""

enemigo = Enemigo()
enemigos.add(enemigo)

# ------------- JUGADOR

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

    pantalla.blit(fondo, (0,0))

    # Actualizo el estado de cada sprite en el juego
    sprites.update()
    enemigos.update()
    balas.update()

    # Colisiones (el objeto que provoca la colisión, grupo de sprites colisionados)
    # False es para que no se elimine el objeto enemigo
    colision = pygame.sprite.spritecollide(jugador, enemigos, False)

    # Si se produce una colisión
    if colision:
        # el enemigo se convierte en una bola de fuego
        enemigo.image = pygame.image.load("recursos/juego_spaceShip/bolaFuego.png").convert()
        enemigo.image.set_colorkey(NEGRO)  # elimino fondo negro

        # redimensiono la imagen porque la original es muy grande (640, 320)
        enemigo.image = pygame.transform.scale(enemigo.image, (50, 50))

        # caerá por la pantalla
        enemigo.posicion_y += 7;

    # Cuando haya caído hasta el final, se elimina
    elif enemigo.rect.top > ALTO:
        enemigo.kill()


    # Dibujo los sprites en la pantalla, con el método draw del grupo de sprites
    sprites.draw(pantalla)
    enemigos.draw(pantalla)
    balas.draw(pantalla)


    # Actualizo la ventana con los cambios realizados
    pygame.display.flip()

# Cierro todos los módulos Pygame que había inicializado antes
""" NOTA: Si no se llama a pygame.quit(), se pueden producir errores o 
conflictos en el sistema y el programa puede no cerrarse adecuadamente."""
pygame.quit()
