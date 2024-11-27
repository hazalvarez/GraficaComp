from manim import *

# Clase para los árboles
class Arbol:
    def __init__(self, posicion_x):
        self.posicion_x = posicion_x
        self.tronco = None
        self.copa_1 = None
        self.copa_2 = None
        self.copa_3 = None

    def crear_arbol(self):
        # Tronco del árbol
        self.tronco = Rectangle(width=0.3, height=1, color=DARK_BROWN, fill_opacity=1)
        self.tronco.set_stroke(color=BLACK, width=2)
        self.tronco.shift(DOWN * 1 + self.posicion_x)  # Colocar el tronco en la posición indicada

        # Copa del árbol (tres óvalos verdes)
        self.copa_1 = Ellipse(width=1, height=0.6, color=GREEN, fill_opacity=1).next_to(self.tronco, UP, buff=0)
        self.copa_2 = Ellipse(width=1.2, height=0.7, color=GREEN, fill_opacity=1).next_to(self.copa_1, UP * 0.3)
        self.copa_3 = Ellipse(width=0.8, height=0.5, color=GREEN, fill_opacity=1).next_to(self.copa_2, UP * 0.2)

    def dibujar(self, escena):
        # Añadir cada parte del árbol a la escena
        escena.add(self.tronco, self.copa_1, self.copa_2, self.copa_3)

# Clase para la luna
class Luna:
    def __init__(self):
        self.luna = None

    def crear_luna(self):
        # Crear la luna en la esquina superior derecha
        self.luna = Circle(radius=0.5, color=WHITE, fill_opacity=1)
        self.luna.set_stroke(color=WHITE, width=2)
        self.luna.to_corner(UP + RIGHT)  # Posicionar la luna en la esquina superior derecha

    def dibujar(self, escena):
        # Añadir la luna a la escena
        escena.add(self.luna)

# Clase para el pasto
class Pasto:
    def __init__(self):
        self.pasto = None

    def crear_pasto(self):
        # Crear el pasto en la parte inferior de la escena
        self.pasto = Rectangle(width=config.frame_width, height=2, color=GREEN, fill_opacity=1)
        self.pasto.shift(DOWN * 2.5)  # Colocar el pasto en la parte inferior de la pantalla

    def dibujar(self, escena):
        # Añadir el pasto a la escena
        escena.add(self.pasto)

# Clase principal de la escena
class NocheScene(Scene):
    def construct(self):
        # Crear el cielo oscuro como fondo
        cielo = Rectangle(width=config.frame_width, height=config.frame_height, color=DARK_BLUE, fill_opacity=1)
        self.add(cielo)  # Añadir el cielo oscuro al fondo

        # Crear el pasto
        pasto = Pasto()
        pasto.crear_pasto()
        pasto.dibujar(self)

        # Crear y dibujar los árboles
        posiciones_arboles = [LEFT * 3, LEFT * 1, RIGHT * 1.5, RIGHT * 3.5]
        arboles = [Arbol(pos) for pos in posiciones_arboles]
        for arbol in arboles:
            arbol.crear_arbol()
            arbol.dibujar(self)

        # Crear y dibujar la luna
        luna = Luna()
        luna.crear_luna()
        luna.dibujar(self)

        # Pausar para mostrar la escena
        self.wait(2)

# Crear la escena
""""
scene = NocheScene()
scene.render()"""
