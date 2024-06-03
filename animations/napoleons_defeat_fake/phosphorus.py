from manim import *
from manim_chemistry import *

class PhosphorusCrystals(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=45*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        
        black_p = ThreeDMolecule.from_mol_file(filename="BlackP.mol", source_csv="Elementos.csv").scale(0.3)
        white_p = ThreeDMolecule.from_mol_file(filename="WhiteP.mol", source_csv="Elementos.csv").set_color(WHITE).scale(0.3)
        red_p = ThreeDMolecule.from_mol_file(filename="RedP.mol", source_csv="Elementos.csv").set_color(RED).rotate(PI/2).scale(0.3)
        violet_p = ThreeDMolecule.from_mol_file(filename="VioletP.mol", source_csv="Elementos.csv").set_color(PURPLE).rotate(PI/2).scale(0.3)
        
        self.wait()
        self.play(FadeIn(black_p))
        self.wait(5)
        self.play(ReplacementTransform(black_p, white_p))
        self.wait(5)
        self.play(ReplacementTransform(white_p, red_p))
        self.wait(5)
        self.play(ReplacementTransform(red_p, violet_p))
        self.wait(5)
        