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
class SunData(Scene):
    def construct(self):
        data = pd.read_csv("solar_radiation.csv")
        wavelenght = data["lambda"].to_numpy()
        etr_solar = data["etr"].to_numpy()
        direct_solar = data["direct"].to_numpy()
        
        
        big_axis = Axes(
            x_range = (100, 4000, 300),
            x_axis_config={"include_numbers": True, "font_size": 15},
            y_range=(0,2.5),
            tips=False,
            color=COLOR_GRAY
        )
        big_axis2 = big_axis.copy()
        small_axis = Axes(
            x_range=(100, 750, 50),
            x_axis_config={"include_numbers": True, "font_size": 15},
            y_range=(0,2.5),
            tips=False,
            color=COLOR_GRAY
        )
        uv_axis = Axes(
            x_range=(100, 400, 20),
            x_axis_config={"include_numbers": True, "font_size": 15},
            y_range=(0,1.5),
            tips=False,
            color=COLOR_GRAY
        )
        
        etr_data = big_axis.plot_line_graph(
            x_values=wavelenght,
            y_values=etr_solar,
            line_color=COLOR_C,
            stroke_width=1
         )["line_graph"]
        
        etr_data2 = etr_data.copy()
        etr_data_small = small_axis.plot_line_graph(
            x_values=wavelenght,
            y_values=etr_solar,
            line_color=COLOR_C,
            stroke_width=1
        )["line_graph"]
        
        direct_uv_data = uv_axis.plot_line_graph(
            x_values=wavelenght,
            y_values=etr_solar,
            line_color=COLOR_C,
            stroke_width=1
            
        )["line_graph"]
        
        direct_solar_data = big_axis2.plot_line_graph(
            x_values=wavelenght,
            y_values=direct_solar,
            line_color=COLOR_D,
            stroke_width=1
        )["line_graph"]
        
        self.wait()
        
        self.play(Create(big_axis), run_time=2)
        self.play(Create(etr_data), run_time=5)
        
        self.wait(0.5)
        

        def get_intersection_updater(no_added_mob, background, gradient, gradient_index):
            def updater(added_mob):
                added_mob.become(Intersection(no_added_mob, background, sheen_direction=RIGHT, fill_opacity=0.5, stroke_width=0).set_color(color_gradient(gradient, gradient_index)))
            return updater
        
        infrared_region = Rectangle(width=10.15, height=6).shift(0.93*RIGHT)
        infrared_mask = Square().scale(10).set_opacity(0).next_to(infrared_region, LEFT, buff=0)
        infrared_rectangle = VMobject().add_updater(get_intersection_updater(infrared_region, infrared_mask, [RED, RED_C, RED_B, RED_A], 4))
        
        self.add(infrared_rectangle)
        self.play(infrared_mask.animate.shift(infrared_region.get_width()*RIGHT), run_time=3)
        
        self.wait(0.5)
        self.play(infrared_mask.animate.shift((infrared_region.get_width()+1)*LEFT), run_time=2)
        
        self.wait(0.5)
        
        
        self.play(
           ReplacementTransform(big_axis, small_axis),
           ReplacementTransform(etr_data, etr_data_small),
           run_time=1.5
        )
        
        self.wait(0.5)
        
        visible_region = Rectangle(width=7.2, height=6).shift(1.2*RIGHT)
        visible_mask = Square().scale(10).set_opacity(0).next_to(visible_region, LEFT, buff=0)
        visible_rectangle = VMobject().add_updater(get_intersection_updater(visible_region, visible_mask, [PURPLE, BLUE, TEAL, GREEN, YELLOW, ORANGE, RED], 4))
        
        
        self.add(visible_rectangle)
        self.play(visible_mask.animate.shift(visible_region.get_width()*RIGHT), run_time=3)
        
        self.wait(0.5)
        self.play(visible_mask.animate.shift((visible_region.get_width()+1)*LEFT), run_time=2)
        
        self.wait(0.5)
        
        self.play(
            ReplacementTransform(small_axis, uv_axis),
            ReplacementTransform(etr_data_small, direct_uv_data),
            run_time=1.5
        )
        
        self.wait(0.5)
        
        uv_region = Rectangle(width=12, height=6)
        uv_mask = Square().scale(10).set_opacity(0).next_to(uv_region, LEFT, buff=0)
        uv_rectangle = VMobject().add_updater(get_intersection_updater(uv_region, uv_mask, [BLACK, PURPLE_E, PURPLE_D, PURPLE_C], 4))
        
        self.add(uv_rectangle)
        self.play(uv_mask.animate.shift(uv_region.get_width()*RIGHT), run_time=2)
        
        self.wait(0.5)
        
        uva_rectangle = Rectangle(width=3.2, height=6).shift(4.4*RIGHT)
        uvb_rectangle = Rectangle(width=1.6, height=6).shift(2*RIGHT)
        uvc_rectangle = Rectangle(width=7.2, height=6).shift(2.4*LEFT)
        
        uva_inter = Intersection(direct_uv_data, uva_rectangle, fill_opacity=1, stroke_width=0, color=PURPLE_A)
        uvb_inter = Intersection(direct_uv_data, uvb_rectangle, fill_opacity=1, stroke_width=0, color=PURPLE_C)
        uvc_inter = Intersection(direct_uv_data, uvc_rectangle, fill_opacity=1, stroke_width=0, color=PURPLE_E)
        
        uva = Text("UVA", stroke_color=COLOR_0, stroke_width=1, fill_opacity=1, fill_color=LIGHT_PINK).scale(0.8).move_to([4.5, -2, 0])
        uvb = Text("UVB", stroke_color=COLOR_0, stroke_width=1, fill_opacity=1, fill_color=LIGHT_PINK).scale(0.8).move_to([2.1, -2, 0])
        uvc = Text("UVC", stroke_color=COLOR_0, stroke_width=1, fill_opacity=1, fill_color=LIGHT_PINK).scale(0.8).move_to([-0.5, -2, 0])
        
        self.wait(2)
        self.play(
            FadeIn(uva_inter),
            FadeIn(uva)
        )
        
        self.wait(2)
        
        self.play(
            FadeIn(uvb_inter),
            FadeIn(uvb)
        )
        
        self.wait(2)
        
        self.play(
            FadeIn(uvc_inter),
            FadeIn(uvc)
        )

        self.wait(2)
        
        self.play(
            FadeOut(uva),
            FadeOut(uvb),
            FadeOut(uvc),
        )
        self.play(
            FadeOut(uva_inter),
            FadeOut(uvb_inter),
            FadeOut(uvc_inter),
        )
        
        self.play(uv_mask.animate.shift((uv_region.get_width()+1)*LEFT), run_time=1.5)
        self.wait()
        
        self.play(
            ReplacementTransform(uv_axis, big_axis2),
            ReplacementTransform(direct_uv_data, etr_data2),
            run_time=1.5
        )
        
        self.play(Create(direct_solar_data), run_time=1.5)
        
        
        atmosphere_radiation = Text("Radiación que llega a las capas altas de la atmósfera", color=COLOR_C, font="Reem Kufi").scale(0.65).move_to([2, 2, 0])
        surphace_radiation = Text("Radiación que llega a la superficie terrestre", color=COLOR_D, font="Reem Kufi").scale(0.65).move_to([1.1, 1, 0])
        
        self.wait()
        self.play(
            FadeIn(atmosphere_radiation),
            FadeIn(surphace_radiation),
        )
        self.wait(15)
        
        self.play(
            FadeOut(Group(*self.mobjects))
        )
        
        self.wait(2)