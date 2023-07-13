from manim import *
from manim_chemistry import ThreeDMolecule
from random import randint

COLOR_0 = "#24283B"
COLOR_A = "#F7768E"
COLOR_B = "#9ECE6A"
COLOR_C = "#E0AF68"
COLOR_D = "#7AA2F7"
COLOR_E = "#BB9AF7"
COLOR_F = "#7DCFFF"
COLOR_GRAY = "#8B93B5"
SKIN_COLOR_1 = "#FCE2C4"
SKIN_COLOR_2 = "##FCC4C4"
SKIN_COLOR_3 = "#FAA0A0"

#config.background_color = COLOR_0
"""
¡Alto el carro! Si la energía de los fotones es absorbida por la molécula y luego liberada en forma de otro fotón con la misma energía, al final la RUV nos alcanza igualmente, ¿verdad?

Bueno, ese es uno de los mecanismos de pérdida de energía, pero hay más. Por ejemplo, existe la fotofragmentación: La molécula utiliza la energía absorbida para romperse.
Otros seguro que te suenan, como la fluorescencia que puedes observar en algunos subrayadores; 
o la fosforescencia, utilizada habitualmente en las señales de salida de emergencia para que sean visibles cuando no haya luz.

La mayoría de fotoprotectores utiliza un mecanismo conocido como relajación vibracional, consistente en disipar la energía absorbida en forma de energía térmica.
"""

config.background_color = COLOR_0

class Photoreactions(Scene):
    def photon_collision(self, dot, final_position, color=None):
        target_dot = dot.copy().scale(2).set_opacity(0).move_to(final_position)
        if color:
            target_dot.set_color(color)
            
        move = ApplyMethod(dot.move_to, final_position)
        return Succession(FadeIn(dot), move, Transform(dot, target_dot))
    
    def construct(self):
        photons_quantity = 100
        photoprotector = Rectangle(height=0.5, width=15, fill_opacity=1)
        skin = Rectangle(height=5, width=15, fill_opacity=1, fill_color=color_gradient([GOLD_A, RED_A, RED_B],3), sheen_direction=DOWN).shift(2.5*DOWN)
        self.add(skin, photoprotector)
        photon_base = Dot(color=YELLOW).move_to([0, 10, 0])
        photons_list = [photon_base.copy().shift([randint(-6, 6), 0, 0])for i in range(photons_quantity)]
        photons_list2 = [photon_base.copy().shift([randint(-6, 6), -10, 0])for i in range(photons_quantity)]
        
        self.wait()
        self.play(
            AnimationGroup(
                LaggedStart(*[self.photon_collision(photon, [randint(-800, 800)/100, 0, 0]) for photon in photons_list], lag_ratio=0.02),
                LaggedStart(*[self.photon_collision(photon, [randint(-800, 800)/100, randint(5, 30)/-10, 0], color=RED) for photon in photons_list2], lag_ratio=0.02),
                lag_ratio=0.8
            )   
        )
        
        self.play(
            skin.animate.set_color(color_gradient([GOLD_E, RED_C, RED_E],3)),
            run_time=3
        )
        
        
class Avobenzone3D(ThreeDScene):
    def construct(self):
        av = ThreeDMolecule.from_mol_file("molecules/avobenzone_3d.mol", "Elementos.csv").scale(0.75)
        self.add(av)