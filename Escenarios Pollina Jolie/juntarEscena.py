from manim import *
from escena import *
from pollo import *
from noche import *

# Clase principal para juntar el escenario y el pollo
class JuntarEscena(Scene):
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

        # Pausar para mostrar el resultado
        self.wait(2)
        escala=0.5
         # Coordenada donde se desea colocar el pollo
        posicion_pollo = 2 * LEFT + 2 * DOWN  # Puedes cambiar esta coordenada según lo necesites

        # Crear el pollo con un tamaño ajustable
        cabeza = Cabeza(escala, posicion=posicion_pollo)
        cabeza.crear()
        cuerpo = Cuerpo(cabeza, escala, posicion=posicion_pollo)
        cuerpo.crear(cabeza)
        alas = Alas(cabeza, escala, posicion=posicion_pollo)
        alas.crear(cabeza)
        patas = Patas(escala, posicion=posicion_pollo)
        patas.crear(cuerpo)
        

        # Dibujar todas las partes del pollo en la escena
        patas.dibujar(self)
        cuerpo.dibujar(self)
        alas.dibujar(self)
        cabeza.dibujar(self)


        # Pausar para mostrar el resultado
        self.wait(2)


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
scene = JuntarEscena()
scene.render()
