from manim import *

class EscenarioConHelios(Scene):
    def construct(self):
        
        
        
        #FONDO
        fondo = Rectangle(width=14, height=8, color=BLACK, fill_opacity=1)
        self.add(fondo)

        # Agregando estrellas (pequeños puntos blancos en diferentes posiciones)
        for _ in range(50):  # Generamos 50 estrellas
            estrella = Dot(
                point=[np.random.uniform(-7, 7), np.random.uniform(-4, 4), 0],
                radius=0.03,
                color=WHITE
            )
            self.add(estrella)

        # Creando un planeta (un círculo grande de color) en la esquina inferior izquierda
        planeta = Circle(radius=1.5, color=BLUE, fill_opacity=0.8).shift(LEFT * 5 + DOWN * 2)
        self.add(planeta)

        # Anillos del planeta (representados por elipses alrededor del planeta)
        anillo1 = Ellipse(width=3, height=0.2, color=GRAY).shift(LEFT * 5 + DOWN * 2).rotate(PI / 6)
        anillo2 = Ellipse(width=3.5, height=0.25, color=LIGHT_GRAY).shift(LEFT * 5 + DOWN * 2).rotate(PI / 6)
        self.add(anillo1, anillo2)

        
        self.play(Create(fondo))
        self.play(Create(estrella))
        self.play(Create(planeta))
        self.play(Uncreate(anillo1), Uncreate(anillo2))

