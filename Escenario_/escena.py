from manim import *

class DaytimeScene(Scene):
    def construct(self):
        # Crear el cielo como fondo
        cielo = Rectangle(width=config.frame_width, height=config.frame_height, color=BLUE, fill_opacity=1)
        self.add(cielo)  # Añadir el cielo al fondo

        # Crear el pasto en la parte inferior de la escena
        pasto = Rectangle(width=config.frame_width, height=2, color=GREEN, fill_opacity=1)
        pasto.shift(DOWN * 2.5)  # Colocar el pasto en la parte inferior de la pantalla
        self.add(pasto)

        # Crear el sol en la esquina superior derecha
        sol = Circle(radius=0.5, color=YELLOW, fill_opacity=1)
        sol.set_stroke(color=YELLOW, width=2)
        sol.to_corner(UP + RIGHT)  # Posicionar el sol en la esquina superior derecha
        self.add(sol)
        
        # Crear rayos del sol
        rayos = VGroup()
        for angle in range(0, 360, 45):  # Añadir rayos cada 45 grados
            rayo = Rectangle(width=0.1, height=0.7, color=YELLOW, fill_opacity=1)
            rayo.set_stroke(color=YELLOW, width=1)
            rayo.move_to(sol.get_center())  # Mover rayo al centro del sol
            rayo.shift(UP * 0.9)  # Posicionar un poco fuera del sol
            rayo.rotate(angle * DEGREES, about_point=sol.get_center())  # Rotar alrededor del centro del sol
            rayos.add(rayo)

        self.add(rayos)  # Añadir los rayos a la escena

        # Función para crear un árbol
        def crear_arbol(posicion_x):
            # Tronco del árbol
            tronco = Rectangle(width=0.3, height=1, color=DARK_BROWN, fill_opacity=1)
            tronco.set_stroke(color=BLACK, width=2)
            tronco.shift(DOWN * 1 + posicion_x)  # Colocar el tronco en la posición indicada

            # Copa del árbol (tres óvalos verdes)
            copa_1 = Ellipse(width=1, height=0.6, color=GREEN, fill_opacity=1).next_to(tronco, UP, buff=0)
            copa_2 = Ellipse(width=1.2, height=0.7, color=GREEN, fill_opacity=1).next_to(copa_1, UP * 0.3)
            copa_3 = Ellipse(width=0.8, height=0.5, color=GREEN, fill_opacity=1).next_to(copa_2, UP * 0.2)

            # Añadir cada parte del árbol a la escena
            self.add(tronco, copa_1, copa_2, copa_3)


      
        # Crear múltiples árboles en diferentes posiciones
        posiciones_arboles = [LEFT * 3, LEFT * 1, RIGHT * 1.5, RIGHT * 3.5]
        for pos in posiciones_arboles:
            crear_arbol(pos)

        # Mostrar mensaje de bienvenida en el centro
        mensaje = Text("¡Bienvenidos a un día soleado en Chi-apas!", font_size=36).to_edge(UP)
        self.play(Write(mensaje))
        self.play(FadeOut(mensaje))
        # Pausar para mostrar la escena
        self.wait(2)

# Crear la escena
scene = DaytimeScene()
scene.render()
