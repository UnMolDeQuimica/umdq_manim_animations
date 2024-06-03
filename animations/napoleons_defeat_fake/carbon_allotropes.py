from manim import *
from manim_chemistry import *

class NanotubesSpinning(ThreeDScene):
    def construct(self):
        self.begin_ambient_camera_rotation(rate=0.2)
        self.set_camera_orientation(phi=75*DEGREES, theta=45*DEGREES)
        
        nanotubes = ThreeDMolecule.from_mol_file("carbon_nanotube.mol", "Elementos.csv").rotate(PI/2).scale(0.1)
        
        self.wait()
        
        self.play(FadeIn(nanotubes))
        self.wait(15)
        
class FullereneSpinning(ThreeDScene):
    def construct(self):
        self.begin_ambient_camera_rotation(rate=0.2)
        self.set_camera_orientation(phi=75*DEGREES, theta=45*DEGREES)
        
        fullerene = ThreeDMolecule.from_mol_file("fullerene.mol", "Elementos.csv").scale(0.9)
        self.wait()
        self.play(FadeIn(fullerene))
        self.wait(15)