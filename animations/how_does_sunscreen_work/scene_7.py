import pandas as pd
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
class AbsortionLevels(Scene):
    def construct(self):        
        wavelenghts = pd.read_csv("wavelenghts.csv")
        wl = wavelenghts["wavelenght"]
        avobenzone_data = wavelenghts["avobenzone"]
        octocrylene_data = wavelenghts["octocrylene"]
        ecamsule_data = wavelenghts["ecamsule"]
        all_data = wavelenghts["all"]

        uv_axis = Axes(
            x_range=(290, 400, 10),
            x_axis_config={"include_numbers": True, "font_size": 15},
            y_range=(0, 1200, 200),
            y_axis_config={"include_numbers": True, "font_size": 15},
            tips=False,
            color=COLOR_GRAY
        ).scale(0.9).shift(0.5*DOWN)
        
        uva_rect = Rectangle(height=5.5, width=8, fill_opacity=0.5, stroke_width=0, color=COLOR_E).shift(0.48*DOWN+1.39*RIGHT)
        uvb_rect = Rectangle(height=5.5, width=2.8, fill_opacity=0.5, stroke_width=0, color=COLOR_A).shift(0.48*DOWN+4*LEFT)
        
        uva_text = Text("UVA", font="Reem Kufi", color=COLOR_E).next_to(uva_rect, UP, buff=0.5)
        uvb_text = Text("UVB", font="Reem Kufi", color=COLOR_A).next_to(uvb_rect, UP, buff=0.5)
        avobenzone = uv_axis.plot_line_graph(
            x_values=wl,
            y_values=avobenzone_data,
            line_color=COLOR_D,
            stroke_width=3
        )["line_graph"]
        
        octocrylene = uv_axis.plot_line_graph(
            x_values=wl,
            y_values=octocrylene_data,
            line_color=COLOR_A,
            stroke_width=3
        )["line_graph"]
        
        ecamsule = uv_axis.plot_line_graph(
            x_values=wl,
            y_values=ecamsule_data,
            line_color=COLOR_B,
            stroke_width=3
        )["line_graph"]
        
        all_plot = uv_axis.plot_line_graph(
            x_values=wl,
            y_values=all_data,
            line_color=COLOR_C,
            stroke_width=6
        )["line_graph"]
        
        avobenzone_name = Text("Avobenzona").move_to([-4.5, 3, 0]).set_color(COLOR_D)
        octocrylene_name = Text("Octocrileno").move_to([0, 3, 0]).set_color(COLOR_A)
        ecamsule_name = Text("Ecamsule").move_to([4, 3, 0]).set_color(COLOR_B)
        all_text = Text("Combinación de fotoprotectores").move_to([0, 3, 0]).set_color(COLOR_C)
        
        avobenzone_line = DashedLine(
            [1.45, -3.2, 0],
            [1.45, 1.95, 0],
            color=COLOR_D
        )
        
        octocrylene_line = DashedLine(
            [-4, -3.2, 0],
            [-4, 1.95, 0],
            color=COLOR_A
        )
        
        ecamsule_line = DashedLine(
            [0, -3.2, 0],
            [0, 1.95, 0],
            color=COLOR_B
        )
        
        self.wait()
        self.play(Create(uv_axis), run_time=1.5)
        self.wait()
        self.play(FadeIn(uva_rect), FadeIn(uvb_rect), run_time=1.5)
        self.wait()
        self.play(
            Write(uva_text),
            Write(uvb_text),
            run_time=1.5
        )
        self.wait(2)
        self.play(
            Unwrite(uva_text),
            Unwrite(uvb_text),
        )
        self.wait()
        self.play(Create(avobenzone), Write(avobenzone_name), run_time=2)
        self.wait(1)
        self.play(Create(avobenzone_line), run_time=2)
        self.wait(3.5)
        self.play(Uncreate(avobenzone_line), run_time=2)
        self.wait(3)
        self.play(Create(octocrylene), Write(octocrylene_name), run_time=2)
        self.wait(0.5)
        self.play(Create(octocrylene_line), run_time=2)
        self.wait(2)
        self.play(Uncreate(octocrylene_line), run_time=2)
        self.wait()
        self.play(Create(ecamsule), Write(ecamsule_name), run_time=2)
        self.wait(0.5)
        self.play(Create(ecamsule_line))
        self.wait(2)
        self.play(Uncreate(ecamsule_line))
        self.wait()
        
        self.play(Create(all_plot), run_time=4, rate_func=linear)
        names_group = VGroup(avobenzone_name, octocrylene_name, ecamsule_name)
        
        self.wait()
        self.play(Transform(names_group, all_text))
        
        self.wait(2)
        
        
        
        
