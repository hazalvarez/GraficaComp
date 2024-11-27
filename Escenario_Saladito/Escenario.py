from manim import *

class Cocina(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        COLOR_PARED = ORANGE
        COLOR_PISO = RED
        COLOR_LAMPARA = YELLOW
        COLOR_FRENO = GREY
        
        self.pared = Rectangle(width=30, height=15, color=COLOR_PARED, fill_color=COLOR_PARED, fill_opacity=1)
        self.pared.shift(UP * 7.5)
        
        self.piso = Rectangle(width=30, height=7.5, color=COLOR_PISO, fill_color=COLOR_PISO, fill_opacity=1)
        self.piso.shift(DOWN * 3.75)
        
        self.lampara = Ellipse(width=6, height=2, color=COLOR_LAMPARA, fill_color=COLOR_LAMPARA, fill_opacity=1)
        self.lampara.shift(UP * 10)
        
        self.fregadero = Rectangle(width=5, height=2, color=COLOR_FRENO, fill_color=COLOR_FRENO, fill_opacity=1)
        self.fregadero.shift(DOWN * 1.5 + LEFT * 6.5)
        
        self.add(self.pared, self.piso, self.lampara, self.fregadero)


class Ventanas(VGroup):
    def __init__(self, posiciones, color=BLUE, marco_color=GREY, **kwargs):
        super().__init__(**kwargs)
        
        self.ventanas = VGroup()
        for pos in posiciones:
            marco = Rectangle(width=4.2, height=3.2, color=marco_color, fill_color=marco_color, fill_opacity=1)
            marco.shift(pos)
            
            ventana = Rectangle(width=4, height=3, color=color, fill_color=color, fill_opacity=1)
            ventana.shift(pos)
            
            linea_vertical = Line(UP * 1.5, DOWN * 1.5, color=BLACK, stroke_width=3)
            linea_vertical.move_to(pos)
            linea_vertical.shift(RIGHT * 0)

            linea_horizontal = Line(LEFT * 2, RIGHT * 2, color=BLACK, stroke_width=3)
            linea_horizontal.move_to(pos)
            linea_horizontal.shift(UP * 0)

            self.ventanas.add(marco, ventana, linea_vertical, linea_horizontal)

        self.add(self.ventanas)

class Piso(Rectangle):
    def __init__(self, **kwargs):
        super().__init__(width=100, height=2, fill_color=GRAY, fill_opacity=1, **kwargs)
        self.shift(DOWN * 3)

class Mancha(Ellipse):
    def __init__(self, shift_x, shift_y, **kwargs):
        super().__init__(width=4.0, height=0.5, color=GREEN, fill_opacity=1, **kwargs)
        self.shift(RIGHT * shift_x + DOWN * shift_y)

class Personaje:
    def __init__(self, x_offset=0, y_offset=0):
        # Crear el cuerpo del personaje (rombo verde)
        self.rombo_verde = Polygon(
            LEFT, UP, RIGHT, DOWN,  
            color="#006400",        
            fill_color="#006400",   
            fill_opacity=1
        )
        self.rombo_verde.shift((DOWN + 0.5) + (RIGHT * 4 + x_offset))

        # Crear los ojos
        self.ojo1 = Ellipse(width=0.2, height=0.2, color=BLACK, fill_opacity=1)
        self.ojo2 = Ellipse(width=0.2, height=0.2, color=BLACK, fill_opacity=1)
        self.ojo1.shift((RIGHT * 4) + (DOWN + 0.7) + RIGHT * x_offset)
        self.ojo2.shift((RIGHT * 3.5) + (DOWN + 0.7) + RIGHT * x_offset)

        # Crear la boca
        self.boca = Ellipse(width=0.3, height=0.5, color=GREEN, fill_opacity=1)
        self.boca.shift((RIGHT * 4.2) + (DOWN + 0.3) + RIGHT * x_offset)

        # Crear las manos
        self.mano1 = Rectangle(width=0.8, height=0.1, color=BLACK, fill_opacity=1)
        self.mano2 = Rectangle(width=0.8, height=0.1, color=BLACK, fill_opacity=1)
        self.mano1.shift(RIGHT * 3.5 + DOWN * 0.7 + RIGHT * x_offset)
        self.mano2.shift(RIGHT * 5.5 + DOWN * 0.7 + RIGHT * x_offset)

        # Crear los pies
        self.pie1 = Rectangle(width=1.4, height=0.1, color=BLACK, fill_opacity=1)
        self.pie2 = Rectangle(width=1.4, height=0.1, color=BLACK, fill_opacity=1)
        self.pie1.shift(RIGHT * 4.2 + DOWN * 1.4 + RIGHT * x_offset)
        self.pie2.shift(RIGHT * 4.8 + DOWN * 1.4 + RIGHT * x_offset)

        # Rotar los pies
        self.pie1.rotate(PI / 2)
        self.pie2.rotate(PI / 2)
        
        self.personaje_group = VGroup(self.mano1, self.mano2, self.pie1, self.pie2, self.rombo_verde,self.ojo1, self.ojo2, self.boca,)

    def get_elementos(self):
        return self.personaje_group


class Escenario(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        
        #Fondo de la cocina
        cocina = Cocina()
        self.add(cocina) 
        
        
        
        #Ventanas 
        posiciones_ventanas = [UP * 1 + LEFT * 2.5, UP * 1 + RIGHT * 2.5]
        ventanas = Ventanas(posiciones_ventanas)
        self.add(ventanas)
        
        
        
        # Piso
        piso = Piso()
        self.add(piso)
        
        # Manchas
        manchas = [Mancha(6.5, 2.5), Mancha(2, 3), Mancha(-3, 2.5)]
        self.add(*manchas)

        #Personajes
        personaje1 = Personaje()  
        personaje2 = Personaje()  
        personaje3 = Personaje()  
         
        personaje2.get_elementos().shift(LEFT * 6)  
        personaje3.get_elementos().shift(LEFT * 9) 
        
        self.add(personaje1.get_elementos())
        self.add(personaje2.get_elementos())
        self.add(personaje3.get_elementos())

        