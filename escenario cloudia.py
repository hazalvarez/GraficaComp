from manim import *

class NightCityScene(Scene):
    def construct(self):
        # Fondo nocturno
        sky = Rectangle(color=BLACK, fill_opacity=1, width=14, height=8)
        self.add(sky)

        # Creando edificios
        buildings = VGroup()
        building_heights = [3, 4, 2.5, 3.5, 4.5, 3.8, 2.2]
        for i, height in enumerate(building_heights):
            building = Rectangle(width=1.2, height=height, color=GREY, fill_opacity=1)
            building.set_fill(DARK_GREY)
            building.move_to(LEFT * (5 - i * 1.5) + DOWN * (4 - height / 2))
            
            # Ventanas
            for y in range(int(-height // 0.6), int(height // 0.6)):
                for x in range(-2, 3):  # Ajuste de densidad de ventanas
                    window = Square(side_length=0.2, color=YELLOW, fill_opacity=0.8)
                    window.set_fill(YELLOW)
                    window.move_to(building.get_center() + UP * y * 0.5 + RIGHT * x * 0.4)
                    building.add(window)
            buildings.add(building)

        self.add(buildings)

        # Luna llena
        moon = Circle(radius=0.6, color=WHITE, fill_opacity=1)
        moon.set_fill(WHITE)
        moon.move_to(UP * 2 + RIGHT * 4)
        self.add(moon)

        # Estrellas que parpadean
        stars = VGroup()
        for _ in range(20):
            star = Dot(color=WHITE)
            star.move_to(
                np.array([
                    np.random.uniform(-6, 6),  # Posición X
                    np.random.uniform(-2, 3),  # Posición Y
                    0                          # Posición Z
                ])
            )
            stars.add(star)

        self.add(stars)

        # Animaciones
        self.play(FadeIn(sky, buildings, moon))

        # Movimiento parpadeante de estrellas
        def flicker_stars():
            animations = [
                star.animate.set_fill(opacity=np.random.uniform(0.3, 1.0))
                for star in stars
            ]
            return LaggedStart(*animations, lag_ratio=0.1)

        # Repetir parpadeo
        for _ in range(5):  # Puedes ajustar el número de ciclos
            self.play(flicker_stars(), run_time=2)

        # Finalización
        self.wait(2)

