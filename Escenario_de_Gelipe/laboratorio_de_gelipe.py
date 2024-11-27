# creado por:
# - Alvaro Jesus Castro Pizaña
# - Diego Argel Naverrete GodInes

# Este es nuestro fondo de un laboratorio donde vive nuestro querido "Gelipe"

from manim import *

class FondoLaboratorio(VGroup):
    """Clase para crear el fondo completo del laboratorio."""
    @staticmethod
    def crear_fondo():
        """Crea y devuelve un grupo de elementos que forman el fondo completo."""
        elementos = VGroup()

        # Crear el piso
        tile_size = 0.5
        num_tiles_x = int(config.frame_width / tile_size) + 10
        num_tiles_y = 6
        tiles = VGroup()
        for i in range(num_tiles_x):
            for j in range(num_tiles_y):
                color = BLUE if (i + j) % 2 == 0 else WHITE
                tile = Square(side_length=tile_size).set_fill(color, opacity=1)
                tile.set_stroke(GRAY, width=0.5)
                tile.move_to(np.array([
                    i * tile_size - config.frame_width / 2 + tile_size / 2,
                    j * tile_size - config.frame_height / 2 + tile_size / 2 - 1,
                    0
                ]))
                tiles.add(tile)
        # Aplicar perspectiva inclinada
        perspective_matrix = [[1, 0.5, 0], [0, 1, 0], [0, 0, 1]]
        tiles.apply_matrix(perspective_matrix)
        elementos.add(tiles)

        # Crear la pared
        pared = Rectangle(width=config.frame_width, height=5.5).set_fill(GRAY, opacity=0.8)
        pared.to_edge(UP)
        elementos.add(pared)

        # Crear la ventana
        ventana = Rectangle(width=3, height=1.5).set_fill(WHITE, opacity=0.5)
        ventana.to_edge(UP).shift(DOWN * 0.5)
        lineas_verticales = VGroup(
            Line(ventana.get_top(), ventana.get_bottom()).shift(LEFT * 1),
            Line(ventana.get_top(), ventana.get_bottom()).shift(RIGHT * 1)
        )
        lineas_horizontales = VGroup(
            Line(ventana.get_left(), ventana.get_right()).shift(UP * 0.5),
            Line(ventana.get_left(), ventana.get_right()).shift(DOWN * 0.5)
        )
        elementos.add(ventana, lineas_verticales, lineas_horizontales)

        # Crear el librero
        estante_principal = Rectangle(width=1.2, height=3.5).set_fill(DARK_BROWN, opacity=1)
        estante_principal.to_edge(LEFT).shift(DOWN * 0.5)
        elementos.add(estante_principal)

        # Crear los estantes
        for i in range(5):
            estante = Line(start=LEFT, end=RIGHT, color=WHITE, stroke_width=4).set_length(1.1)
            estante.move_to(estante_principal.get_top() + DOWN * (0.3 + 0.6 * i))
            elementos.add(estante)

        # Crear libros
        colores = [RED, BLUE, GREEN, YELLOW]
        for i in range(4):
            for j in range(3):
                libro = Rectangle(width=0.15, height=0.5).set_fill(colores[j % len(colores)], opacity=1)
                libro.move_to(estante_principal.get_top() + DOWN * (0.6 * (i + 1)) + RIGHT * (0.35 * (j - 1)))
                elementos.add(libro)

        # Crear el escritorio
        escritorio = Rectangle(width=3, height=0.4).set_fill(DARK_BROWN, opacity=1)
        escritorio.move_to(DOWN * 1.5 + RIGHT * 5)
        elementos.add(escritorio)

        # Crear patas del escritorio
        pata_izquierda = Rectangle(width=0.3, height=1).set_fill(DARK_BROWN, opacity=1)
        pata_izquierda.move_to(DOWN * 2 + RIGHT * 4.2)
        pata_derecha = Rectangle(width=0.3, height=1).set_fill(DARK_BROWN, opacity=1)
        pata_derecha.move_to(DOWN * 2 + RIGHT * 5.8)
        elementos.add(pata_izquierda, pata_derecha)

        # Crear monitor
        monitor = Rectangle(width=1.2, height=0.8).set_fill(BLUE_E, opacity=0.9)
        monitor.move_to(escritorio.get_top() + UP * 0.6)
        base_monitor = Rectangle(width=0.2, height=0.3).set_fill(GRAY, opacity=1)
        base_monitor.next_to(monitor, DOWN, buff=0.05)
        elementos.add(monitor, base_monitor)

        return elementos



# ejemplo de como debe usarse
# en otro archivo debe añadirse laboratorio_de_gelipe y la clase
# despues debemos crear un obj y añadirlo directamente

# from manim import *
# from laboratorio_de_gelipe import FondoLaboratorio

# class EscenaConFondo(Scene):
#     def construct(self):
#         # Crear el fondo del laboratorio
#         fondo = FondoLaboratorio.crear_fondo()
        
#         # Añadir el fondo a la escena
#         self.add(fondo)

#         # Añadir más objetos o animaciones
#         texto = Text("Laboratorio en construcción").to_edge(UP)
#         self.add(texto)

#         self.wait(5)
