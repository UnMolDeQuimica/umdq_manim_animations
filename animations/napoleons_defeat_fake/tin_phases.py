from manim import *
from manim_chemistry import *

class TinPhases(ThreeDScene):
    def construct(self):
        self.begin_ambient_camera_rotation(rate=0.2)
        self.set_camera_orientation(phi=75*DEGREES, theta=45*DEGREES)
        alpha_tin = ThreeDMolecule.from_mol_file("alpha_tin.mol", "Elementos.csv").scale(0.35).set_color(WHITE)
        beta_tin = ThreeDMolecule.from_mol_file("beta_tin.mol", "Elementos.csv").scale(0.35).set_color(GRAY_B)
        self.wait()
        self.play(FadeIn(beta_tin))
        self.wait(7)
        self.play(ReplacementTransform(beta_tin, alpha_tin), run_time=4)
        self.wait(7)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75*DEGREES, theta=360*DEGREES)

        self.wait()

class AlphaTinSpinning(ThreeDScene):
    def construct(self):
        self.begin_ambient_camera_rotation(rate=0.2)
        self.set_camera_orientation(phi=75*DEGREES, theta=360*DEGREES)
        alpha_tin = ThreeDMolecule.from_mol_file("alpha_tin.mol", "Elementos.csv").scale(0.35).set_color(WHITE)
        self.add(alpha_tin)
    
        self.wait(15)
        
        
class BetaTinSpinning(ThreeDScene):
    def construct(self):
        self.begin_ambient_camera_rotation(rate=0.2)
        self.set_camera_orientation(phi=75*DEGREES, theta=360*DEGREES)
        beta_tin = ThreeDMolecule.from_mol_file("beta_tin.mol", "Elementos.csv").scale(0.35).set_color(GRAY_B)
        self.add(beta_tin)
    
        self.wait(15)

        
class BetaToAlphaScene(Scene):
    def construct(self):
        beta = Text("Estaño Beta")
        alpha = Text("Estaño Alfa")
        self.wait()
        self.play(FadeIn(beta))
        #self.wait(7)
        #self.play(ReplacementTransform(beta, alpha), run_time=4)
        #self.wait(7)