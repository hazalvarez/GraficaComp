from manim import *

class Brick(Rectangle):
    def __init__(self, width=0.5, height=0.25, color=GRAY, **kwargs):
        # Crear un ladrillo con un borde visible y un relleno gris
        super().__init__(
            width=width,
            height=height,
            color=color,
            fill_color=color,
            fill_opacity=1,
            **kwargs
        )

class BrickWall(VGroup):
    def __init__(self, wall_width, wall_height, brick_width=0.5, brick_height=0.25, spacing=0.05, **kwargs):
        super().__init__(**kwargs)

        # Número de filas y columnas para llenar la pantalla
        num_rows = int(wall_height / (brick_height + spacing)) + 1
        num_cols = int(wall_width / (brick_width + spacing)) + 2

        for row in range(num_rows):
            # Alternar el desplazamiento en cada fila para el patrón de ladrillos
            offset = (brick_width + spacing) / 2 if row % 2 == 1 else 0
            
            for col in range(num_cols):
                # Crear un ladrillo y agregar espacio entre ellos
                brick = Brick(width=brick_width, height=brick_height)
                
                # Posicionar el ladrillo en la columna y fila con el offset
                brick.shift(RIGHT * (col * (brick_width + spacing) - wall_width / 2 + offset) + 
                            UP * (wall_height / 2 - row * (brick_height + spacing)))
                
                # Añadir cada ladrillo a la pared
                self.add(brick)

class BrickWallScene(Scene):
    def construct(self):
        # Crear la pared de ladrillos con espacio entre los ladrillos
        wall = BrickWall(wall_width=config.frame_width, wall_height=config.frame_height)
        
        # Añadir la pared a la escena
        self.add(wall)
        self.wait(2)  # Pausa para visualizar la pared
