from manim import *

class Fondo(Scene):
    def construct(self):
        self.camera.background_color = "#e59edd"
        
        # Crear componentes
        base_rectangle = BaseRectangle()
        upper_rectangles = Romboides()
        additional_structures = ñaca()

        # Agregar componentes a la escena
        self.add(base_rectangle, upper_rectangles, additional_structures)
        self.wait(5)

class BaseRectangle(VGroup):
    def __init__(self):
        super().__init__()
        main_rectangle = Rectangle(width=4, height=2, color="#6b4723", fill_opacity=1.0)
        main_rectangle.to_corner(UP + LEFT)

        rect1 = Rectangle(width=1.7, height=0.8, color="#83cbeb", fill_opacity=1.0)
        rect1.move_to([-5.6, 3.0, 0])
        rect2 = rect1.copy().move_to([-3.7, 3.0, 0])
        rect3 = rect1.copy().move_to([-5.6, 2.0, 0])
        rect4 = rect1.copy().move_to([-3.7, 2.0, 0])

        self.add(main_rectangle, rect1, rect2, rect3, rect4)

class Romboides(VGroup):
    def __init__(self):
        super().__init__()
        romboide = Polygon(
            [-7, -3.5, 0], [7, -3.5, 0], [5, -2.5, 0], [-5, -2.5, 0], color="#996633", fill_opacity=1.0
        )
        romboide1 = Polygon(
            [-0.6, -3.5, 0], [0.6, -3.5, 0], [0.2, -3, 0], [-0.2, -3, 0], color="#89c2eb", fill_opacity=1.0
        )
        romboide1.move_to([-4, -3, 0])
        romboide2 = Polygon(
            [-0.4, -1.4, 0], [0.4, -1.4, 0], [0.1, -1, 0], [-0.1, -1, 0], color="#156082", fill_opacity=1.0
        )
        romboide2.move_to([-4, -3, 0])

        rectangulo_vertical = Rectangle(width=0.1, height=0.2, color="#bfbfbf", fill_opacity=1.0)
        rectangulo_vertical.next_to(romboide2, UP, buff=0)

        flama = Flama()
        flama.next_to(rectangulo_vertical, UP, buff=0)

        self.add(romboide, romboide1, romboide2, rectangulo_vertical, flama)

class Flama(VGroup):
    def __init__(self):
        super().__init__()
        flama = VGroup(
            CubicBezier(
                start_anchor=[-0.05, 0, 0], start_handle=[0.5, 1, 0], end_handle=[-0.5, 2, 0], end_anchor=[0, 2.5, 0]
            ),
            CubicBezier(
                start_anchor=[-0.05, 0, 0], start_handle=[0.4, 1, 0], end_handle=[-0.4, 1.5, 0], end_anchor=[0, 2.5, 0]
            ),
            CubicBezier(
                start_anchor=[-0.05, 0, 0], start_handle=[0.3, 1.2, 0], end_handle=[-0.3, 1.7, 0], end_anchor=[0, 2.2, 0]
            ),
        )
        flama.scale(0.1)
        for f in flama:
            f.set_color_by_gradient(BLUE, ORANGE, ORANGE)
            f.set_stroke(width=3)
        self.add(*flama)

class ñaca(VGroup):
    def __init__(self):
        super().__init__()
        for x, color1, color2 in [(-2, "#ffff00", "#ffff00"), (-2.5, "#eb29b8", "#eb29b8"), (-3, "#00ffff", "#00ffff")]:
            structure = self.create_structure(x, color1, color2)
            self.add(structure)

    def create_structure(self, x, color1, color2):
        rect = Rectangle(width=0.2, height=1, color="#f2f2f2", fill_opacity=1.0).move_to([x, -2.3, 0])
        sombra = Ellipse(width=0.2, height=0.18, color="#46b1e1", fill_opacity=1.0).next_to(rect, UP, buff=0)
        lower_rect = Rectangle(width=0.2, height=0.5, color=color1, fill_opacity=1.0).move_to([x, -2.56, 0])
        circle = Ellipse(width=0.2, height=0.15, color=color2, fill_opacity=1.0).next_to(rect, DOWN, buff=0)

        return VGroup(rect, sombra, lower_rect, circle)
