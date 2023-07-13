from manim import *
from manim_chemistry import *

COLOR_0 = "#24283B"
COLOR_A = "#F7768E"
COLOR_B = "#9ECE6A"
COLOR_C = "#E0AF68"
COLOR_D = "#7AA2F7"
COLOR_E = "#BB9AF7"
COLOR_F = "#7DCFFF"
COLOR_GRAY = "#8B93B5"

config.background_color = COLOR_0
class VitaminD(Scene):
    def construct(self):        
        vitamin_d = MMoleculeObject.from_mol_file("molecules/vitamin_d.mol").set_color(COLOR_C)
        # Clean a bit the molecule
        vitamin_d[1][24].shift(0.3*UP)
        vitamin_d[1][10].scale(0.85).shift(0.05*UP)
        vitamin_d[0][29].shift(0.1*(UP+RIGHT))
        
        
        self.wait(3)
        self.play(Write(vitamin_d), run_time=3)
        self.wait(2)