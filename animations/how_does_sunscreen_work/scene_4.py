from manim import *
from manim_chemistry import *
from manim.utils.rate_functions import ease_in_out_sine

COLOR_0 = "#24283B"
COLOR_A = "#F7768E"
COLOR_B = "#9ECE6A"
COLOR_C = "#E0AF68"
COLOR_D = "#7AA2F7"
COLOR_E = "#BB9AF7"
COLOR_F = "#7DCFFF"
COLOR_GRAY = "#8B93B5"

config.background_color = COLOR_0

class AtomicOrbitals(Scene):
    def construct(self):
        bohr_atom = BohrAtom(e = 6, p = 6, n=6, level=3, orbit_color=COLOR_GRAY, neutron_color=COLOR_GRAY, proton_color=COLOR_A, electron_color=COLOR_F)
        
        electrons = bohr_atom.get_electrons()
        moving_electron = electrons[1][1]
        photon = Dot(color=YELLOW).scale(0.5).move_to([-12, 6, 0])
        
        trace = TracedPath(photon.get_start, stroke_color=YELLOW, dissipating_time=0.5)
        self.add(photon, trace)
        
        self.add_mobjects_from_animations
        self.play(
            FadeIn(bohr_atom),
            run_time=3
        )
        self.play(Rotate(electrons, -0.1), run_time=0.5)
        self.play(Rotate(electrons, 4*PI+0.1), run_time=8, rate_func=ease_in_out_sine)
        
        
        self.wait()

        self.play(photon.animate.move_to(moving_electron.get_center()))
        self.play(Flash(moving_electron), Indicate(moving_electron), FadeOut(photon))
        self.play(moving_electron.animate.shift(UP))
        self.remove(trace)
        self.wait()
        
        photon.move_to(moving_electron.get_center())
        self.play(Flash(moving_electron), Indicate(moving_electron), FadeIn(photon))
        new_trace = TracedPath(photon.get_start, stroke_color=YELLOW, dissipating_time=0.5)
        self.add(new_trace)
        self.play(photon.animate.move_to([10, 6, 0]), moving_electron.animate.shift(DOWN))
        
        self.wait()