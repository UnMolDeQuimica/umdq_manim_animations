from manim import *

COLOR_0 = "#24283B"
COLOR_A = "#F7768E"
COLOR_B = "#9ECE6A"
COLOR_C = "#E0AF68"
COLOR_D = "#7AA2F7"
COLOR_E = "#BB9AF7"
COLOR_F = "#7DCFFF"
COLOR_GRAY = "#8B93B5"

config.background_color = COLOR_0

class Test(Scene):
    def construct(self):
        dots = [Square().move_to([i, 0, 0]) for i in range(-3,3)]
        
        self.play(
            LaggedStart(*[Create(dot) for dot in dots], lag_ratio=0.5)
        )
    