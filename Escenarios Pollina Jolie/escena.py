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
        self.tronco = Rectangle(width=0.5, height=2, color=DARK_BROWN, fill_opacity=1)
        self.tronco.set_stroke(color=BLACK, width=2)
        self.tronco.shift(DOWN * 1 + self.posicion_x)  # Colocar el tronco en la posición indicada

        # Copa del árbol (tres óvalos verdes)
        self.copa_1 = Ellipse(width=1, height=1.3, color=GREEN, fill_opacity=1).next_to(self.tronco.get_center(), UP*0.005, buff=0)
        self.copa_2 = Ellipse(width=1.8, height=1.5, color=GREEN, fill_opacity=1).next_to(self.copa_1.get_center(), UP * 0.1)
        self.copa_3 = Ellipse(width=1.2, height=1, color=GREEN, fill_opacity=1).next_to(self.copa_2.get_center(), UP * 0.1)

    def dibujar(self, escena):
        # Añadir cada parte del árbol a la escena
        escena.add(self.tronco, self.copa_1, self.copa_2, self.copa_3)

# Clase para el sol
class Sol:
    def __init__(self):
        self.sol = None

    def crear_sol(self):
        # Crear el sol en la esquina superior derecha
        self.sol = Circle(radius=0.5, color=YELLOW, fill_opacity=1)
        self.sol.set_stroke(color=YELLOW, width=2)
        self.sol.to_corner(UP + RIGHT)  # Posicionar el sol en la esquina superior derecha

    def dibujar(self, escena):
        # Añadir el sol a la escena
        escena.add(self.sol)

    def animar_sol(self):
        # Animar el movimiento del sol
        return self.sol.animate.shift(UP + LEFT * 1)

# Clase para las nubes
class Nube:
    def __init__(self, posicion_x):
        self.posicion_x = posicion_x
        self.nube = None

    def crear_nube(self):
        # Crear una nube
        self.nube = Ellipse(width=3, height=1, color=WHITE, fill_opacity=0.7)
        self.nube.shift(UP * 2 + LEFT * 0.5 + RIGHT * self.posicion_x)

    def dibujar(self, escena):
        # Añadir la nube a la escena
        escena.add(self.nube)

    def animar_nube(self):
        # Animar la nube para que se desplace
        return self.nube.animate.shift(LEFT * 10)

# Clase principal de la escena
class DaytimeScene(Scene):
    def construct(self):
        # Crear el cielo como fondo
        cielo = Rectangle(width=config.frame_width, height=config.frame_height, color=BLUE, fill_opacity=1)
        self.add(cielo)  # Añadir el cielo al fondo

        # Crear el pasto en la parte inferior de la escena
        pasto = Rectangle(width=config.frame_width, height=3, color=GREEN, fill_opacity=1)
        pasto.shift(DOWN * 2.5)  # Colocar el pasto en la parte inferior de la pantalla
        self.add(pasto)

        # Crear y dibujar los árboles
        posiciones_arboles = [LEFT * 3, LEFT * 1, RIGHT * 1.5, RIGHT * 3.5]
        arboles = [Arbol(pos) for pos in posiciones_arboles]
        for arbol in arboles:
            arbol.crear_arbol()
            arbol.dibujar(self)

        # Crear y dibujar el sol
        sol = Sol()
        sol.crear_sol()
        sol.dibujar(self)

        # Animar el sol
        self.play(sol.animar_sol())

        # Crear y dibujar las nubes
        nubes = [Nube(i * 4) for i in range(3)]
        for nube in nubes:
            nube.crear_nube()
            nube.dibujar(self)

        # Animar las nubes
        self.play(*[nube.animar_nube() for nube in nubes])

        # Pausar para mostrar la escena
        self.wait(2)

# Crear la escena
#scene = DaytimeScene()
#scene.render()
