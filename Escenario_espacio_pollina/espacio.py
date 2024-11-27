from manim import *

class SpaceScene(Scene):
    def construct(self):
        # Crear el fondo oscuro como el espacio
        espacio = Rectangle(width=config.frame_width, height=config.frame_height, color=BLACK, fill_opacity=1)
        self.add(espacio)  # Añadir el espacio como fondo oscuro

        # Crear estrellas aleatorias
        estrellas = VGroup()
        for _ in range(50):  # Número de estrellas
            estrella = Dot(point=[np.random.uniform(-7, 7), np.random.uniform(-4, 4), 0], radius=0.03, color=WHITE)
            estrellas.add(estrella)
        self.add(estrellas)

        # Crear un planeta en la esquina inferior izquierda
        planeta = Circle(radius=1.5, color=BLUE, fill_opacity=1)
        planeta.set_stroke(color= BLUE_A, width=4)
        planeta.to_corner(DOWN + LEFT)
        self.add(planeta)

        # Añadir anillos al planeta
        anillos = VGroup()
        for i in range(3):
            anillo = Ellipse(width=3 + i * 0.5, height=0.2, color=GREY, fill_opacity=0.2)
            anillo.rotate(45 * DEGREES)
            anillo.move_to(planeta.get_center())
            anillos.add(anillo)
        self.add(anillos)

        # Crear una nave espacial en la esquina superior derecha
        nave = VGroup()
        cuerpo = Polygon([-0.2, 0, 0], [0.2, 0, 0], [0, 0.5, 0], color=GRAY, fill_opacity=1)
        ala_izq = Polygon([-0.3, -0.1, 0], [-0.1, -0.1, 0], [-0.2, -0.4, 0], color=GRAY, fill_opacity=1)
        ala_der = Polygon([0.3, -0.1, 0], [0.1, -0.1, 0], [0.2, -0.4, 0], color=GRAY, fill_opacity=1)
        nave.add(cuerpo, ala_izq, ala_der)
        nave.scale(0.5).to_corner(UP + RIGHT)
        self.add(nave)

        # Mostrar mensaje de "Explorando el Universo"
        mensaje = Text("¡Explorando el Universo!", font_size=36).to_edge(UP)
        self.play(Write(mensaje))
        self.play(FadeOut(mensaje))
        # Pausar para mostrar la escena
        self.wait(2)

# Crear la escena
scene = SpaceScene()
scene.render()
