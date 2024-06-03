from manim import *
from manim_chemistry import * 
class PhosphorusAllotropesPropertiesScene(Scene):
    def construct(self):
        black_p_title = Text("Fósforo Negro").set_color(GRAY_C).to_corner(LEFT+UP)
        white_p_title = Text("Fósforo Blanco").set_color(WHITE).to_corner(LEFT+UP)
        red_p_title = Text("Fósforo Rojo").set_color(RED).to_corner(LEFT+UP)
        violet_p_title = Text("Fósforo Violeta").set_color(PURPLE).to_corner(LEFT+UP)
        
        
        black_p_frame = MElementObject(15, 31, "Fósforo", "P", fill_colors=(GRAY_E, GRAY_C, GRAY_C, GRAY_E,)).next_to(black_p_title, DOWN)
        white_p_frame = MElementObject(15, 31, "Fósforo", "P", fill_colors=(GRAY_C, WHITE, WHITE, GRAY_C,)).next_to(white_p_title, DOWN)
        red_p_frame = MElementObject(15, 31, "Fósforo", "P", fill_colors=(RED_E, RED_A, RED_B, RED_D)).next_to(red_p_title, DOWN)
        violet_p_frame = MElementObject(15, 31, "Fósforo", "P", fill_colors=(PURPLE, PURPLE_A, PURPLE_B, PURPLE_E)).next_to(violet_p_title, DOWN)
        
        black_p_properties = Paragraph(
            *[
                "- Es la forma más estable de fósforo.",
                "- Es poco reactivo, incluso a altas presiones y temperaturas.",
                "- Es de estructura variable, pero por lo general se organiza en \n     capas ligeramente arrugadas formando pirámides trigonales.",
                "- Se están desarrollando aplicaciones en biomedicina como biosensor, terapia \n contra el cáncer, administración dirigida de medicamentos entre muchas otras"
            ],
            alignment="left"
        ).set_color(GRAY_C).scale(0.5).to_corner(LEFT+DOWN)
        
        white_p_properties = Paragraph(
            *[
                "- Sólido blanco de textura cerosa obtenido tras calentar fósforo negro",
                "- Su estructura consta de 4 átomos de fósforo formando tetraédros, que luego \n    se asocian entre sí de muy variadas maneras.",
                "- Es muy tóxico y extremadamente reactivo, llegando a ser inflamarse a apenas 50 ºC.",
                "- Aunque se usa como precursor de fertilizantes, es tristemente célebre por su \n      uso militar en forma de bombas de fósforo ampliamente usadas en la SGM."
            ],
            alignment="left"
        ).set_color(WHITE).scale(0.5).to_corner(LEFT+DOWN)
        
        red_p_properties = Paragraph(
            *[
                "- Se obtiene calentando fósforo blanco a 27 ºC en atmósfera inerte.",
                "- Cuando forma cristales, los átomos se organizan en forma \n       de cadenas de tetraédros poco regulares.",
                "- Es algo más reactivo que el fósforo negro aunque no tanto \n     como el blanco. Además, no es tóxico.",
                "- En la serie Breaking Bad se utiliza como reactivo en la \n       síntesis de metamfetamina. \n Algún día os contaré que pinta ahí si no hay fósforo en la molécula de metamfetamina."
            ],
            alignment="left"
        ).set_color(RED).scale(0.5).to_corner(LEFT+DOWN)
        
        violet_p_properties = Paragraph(
            *[
                "- Se le conoce también como fósforo de Hittorf, \n     en honor al señor que lo sintetizó en 1865.",
                "- Es una forma especial de fósforo rojo obtenida por \n    sublimación de este en presencia de yodo.",
                "- Su estructura es similar a la del fósforo rojo, \n   formando cadenas paralelas unidas por algunos átomos de P",
                "- Su aplicación en optoelectrónica está aún en desarrollo, pero parece prometedor."
            ],
            alignment="left",
            line_spacing=1
        ).set_color(PURPLE).scale(0.5).to_corner(LEFT+DOWN)
        
        self.wait()
        self.play(
            FadeIn(black_p_title),
            FadeIn(black_p_frame),
            FadeIn(black_p_properties),
        )
        self.wait(5)
        self.play(
            ReplacementTransform(black_p_title, white_p_title),
            ReplacementTransform(black_p_frame, white_p_frame),
            ReplacementTransform(black_p_properties, white_p_properties),
        )
        self.wait(5)
        self.play(
            ReplacementTransform(white_p_title, red_p_title),
            ReplacementTransform(white_p_frame, red_p_frame),
            ReplacementTransform(white_p_properties, red_p_properties),
        )
        self.wait(5)
        self.play(
            ReplacementTransform(red_p_title, violet_p_title),
            ReplacementTransform(red_p_frame, violet_p_frame),
            ReplacementTransform(red_p_properties, violet_p_properties),
        )
        self.wait(5)
        