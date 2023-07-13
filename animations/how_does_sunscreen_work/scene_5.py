from manim import *
from manim_chemistry import *
import numpy as np
from manim.mobject.opengl.opengl_surface import OpenGLSurface

class OpenGLEllipsoid(OpenGLSurface):
    def __init__(
        self,
        center=ORIGIN,
        **kwargs,
    ):
        super().__init__(
            self.uv_func,
            u_range=(0, TAU),
            v_range=(0, PI),
            **kwargs,
        )

        self.move_to(center)

    def uv_func(self, u, v):
        return np.array(
            [1.5 * np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), -np.cos(v)],
        )
        
COLOR_0 = "#24283B"
config.background_color = COLOR_0

class MolecularOrbitals(ThreeDScene):
    def construct(self):
        h2_atoms_dict = {1: {'coords': np.array([ 9.6625, -3.4452,  0.    ]), 'element': 'H', 'bond_to': {2: 'H'}}, 2: {'coords': np.array([11.6495, -3.4452,  0.    ]), 'element': 'H', 'bond_to': {1: 'H'}}}
        h2_bonds_dict = {1: [{'to': 2, 'type': '1', 'stereo': 0, 'topology': 0, 'reacting_center_status': 0}]}
        
        
        h2_2d = MMoleculeObject(h2_atoms_dict, h2_bonds_dict)
        h2_3d = ThreeDMolecule(h2_atoms_dict, h2_bonds_dict, source_csv="Elementos.csv")
        
        sigma_bonding = OpenGLEllipsoid().set_color(RED)
        sigma_antibonding = Orbital(l=1, m=1).scale(1.5)
        h2_bond = Line([-0.8, 0, 0], [0.8, 0, 0])
        
        b_carotene = ThreeDMolecule.from_mol_file("molecules/b_carotene.mol", source_csv="Elementos.csv").scale(0.5)
        self.play(FadeIn(h2_2d), FadeIn(h2_bond))
        self.wait()
        self.play(
            FadeOut(h2_2d),
            FadeOut(h2_bond),
            FadeIn(h2_3d)
        )
        
        self.wait(2)
        
        self.play(FadeIn(sigma_bonding))
        
        self.wait(2)
        
        self.play(ReplacementTransform(sigma_bonding, sigma_antibonding), run_time=2)
        
        
        self.wait(2)
        
        self.play(FadeOut(sigma_antibonding), FadeOut(h2_3d), run_time=2)
        
        self.wait(0.5)
        
        # 14.5 seconds
        
        self.play(Create(b_carotene), run_time=3)
        
        orbital_base = Orbital(l=1, m=0).scale(0.5)
        orbital_1 = orbital_base.copy().move_to([-0.2, -0.05, 0])
        orbital_2 = orbital_base.copy().move_to([-0.8, 0.1, 0])
        orbital_3 = orbital_base.copy().move_to([-1.3, 0.3, 0])
        orbital_4 = orbital_base.copy().move_to([-1.9, 0, 0])
        orbital_5 = orbital_base.copy().move_to([-2.4, -0.3, 0])
        orbital_6 = orbital_base.copy().move_to([-3, -0.1, 0])
        orbital_7 = orbital_base.copy().move_to([-3.55, -0.4, 0])
        orbital_8 = orbital_base.copy().move_to([-4.1, -0.1, 0])
        orbital_9 = orbital_base.copy().move_to([-4.65, -0.3, 0])
        orbital_10 = orbital_base.copy().move_to([-5.2, 0, 0])
        orbital_11 = orbital_base.copy().move_to([-5.3, 0.55, 0])
        orbital_12 = orbital_base.copy().move_to([0.25, 0.25, 0])
        orbital_13 = orbital_base.copy().move_to([0.85, 0.15, 0])
        orbital_14 = orbital_base.copy().move_to([1.3, 0.45, 0])
        orbital_15 = orbital_base.copy().move_to([1.9, 0.2, 0])
        orbital_16 = orbital_base.copy().move_to([2.4, 0.45, 0])
        orbital_17 = orbital_base.copy().move_to([3, 0.15, 0])
        orbital_18 = orbital_base.copy().move_to([3.5, 0.4, 0])
        orbital_19 = orbital_base.copy().move_to([4.05, 0.05, 0])
        orbital_20 = orbital_base.copy().move_to([4.6, 0.25, 0])
        orbital_21 = orbital_base.copy().move_to([5.12, 0.15, 0])
        orbital_22 = orbital_base.copy().move_to([5.1, -0.7, 0])
        
        self.wait(2)
        
        self.play(
            FadeIn(orbital_1),
            FadeIn(orbital_2),
            FadeIn(orbital_3),
            FadeIn(orbital_4),
            FadeIn(orbital_5),
            FadeIn(orbital_6),
            FadeIn(orbital_7),
            FadeIn(orbital_8),
            FadeIn(orbital_9),
            FadeIn(orbital_10),
            FadeIn(orbital_11),
            FadeIn(orbital_12),
            FadeIn(orbital_13),
            FadeIn(orbital_14),
            FadeIn(orbital_15),
            FadeIn(orbital_16),
            FadeIn(orbital_17),
            FadeIn(orbital_18),
            FadeIn(orbital_19),
            FadeIn(orbital_20),
            FadeIn(orbital_21),
            FadeIn(orbital_22),
            run_time=3
        )

        self.wait()
        
        self.move_camera(phi=90 * DEGREES, run_time = 2)
        
        self.wait()
        
        self.move_camera(phi=0, run_time=2)
        
        self.wait()
        
        self.play(
            FadeOut(b_carotene),
            FadeOut(orbital_1),
            FadeOut(orbital_2),
            FadeOut(orbital_3),
            FadeOut(orbital_4),
            FadeOut(orbital_5),
            FadeOut(orbital_6),
            FadeOut(orbital_7),
            FadeOut(orbital_8),
            FadeOut(orbital_9),
            FadeOut(orbital_10),
            FadeOut(orbital_11),
            FadeOut(orbital_12),
            FadeOut(orbital_13),
            FadeOut(orbital_14),
            FadeOut(orbital_15),
            FadeOut(orbital_16),
            FadeOut(orbital_17),
            FadeOut(orbital_18),
            FadeOut(orbital_19),
            FadeOut(orbital_20),
            FadeOut(orbital_21),
            FadeOut(orbital_22)
        )
        
        # 10 seconds more, 30.5
        avobenzone_3d = ThreeDMolecule.from_mol_file("molecules/avobenzone_3d.mol", source_csv="Elementos.csv").rotate(-30*DEGREES).scale(0.75).shift(DOWN)
        
        self.wait()
        
        self.play(FadeIn(avobenzone_3d), run_time=2)
        
        av_orbital_1 = orbital_base.copy().move_to([-1, 0.8, 0])
        av_orbital_2 = orbital_base.copy().move_to([-1.95, 0.25, 0])
        av_orbital_3 = orbital_base.copy().move_to([-2.85, 0.8, 0])
        av_orbital_4 = orbital_base.copy().move_to([-3.8, 0.25, 0])
        av_orbital_5 = orbital_base.copy().move_to([-1.95, -0.8, 0])
        av_orbital_6 = orbital_base.copy().move_to([-2.85, -1.3, 0])
        av_orbital_7 = orbital_base.copy().move_to([-3.8, -0.8, 0])
        av_orbital_8 = orbital_base.copy().move_to([0.9, 0.8, 0])
        av_orbital_9 = orbital_base.copy().move_to([1.9, 0.25, 0])
        av_orbital_10 = orbital_base.copy().move_to([2.8, 0.8, 0])
        av_orbital_11 = orbital_base.copy().move_to([3.75, 0.25, 0])
        av_orbital_12 = orbital_base.copy().move_to([1.9, -0.8, 0])
        av_orbital_13 = orbital_base.copy().move_to([2.8, -1.3, 0])
        av_orbital_14 = orbital_base.copy().move_to([3.75, -0.8, 0])
        
        self.wait()
        
        self.play(
            FadeIn(av_orbital_1),
            FadeIn(av_orbital_2),
            FadeIn(av_orbital_3),
            FadeIn(av_orbital_4),
            FadeIn(av_orbital_5),
            FadeIn(av_orbital_6),
            FadeIn(av_orbital_7),
            FadeIn(av_orbital_8),
            FadeIn(av_orbital_9),
            FadeIn(av_orbital_10),
            FadeIn(av_orbital_11),
            FadeIn(av_orbital_12),
            FadeIn(av_orbital_13),
            FadeIn(av_orbital_14),
            run_time=2
        )
        
        self.wait()
        
        self.move_camera(phi=90 * DEGREES, run_time=1.5)
        
        self.wait()
        
        self.move_camera(phi=0, run_time=1.5)
        # 12 seconds more, 41.5
        
        self.wait(2)
        
        