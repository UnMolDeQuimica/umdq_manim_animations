from manim import *
from manim_chemistry import *       
from manim.mobject.opengl.opengl_mobject import OpenGLGroup

class GraphiteTransform(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=45*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        
        graphite = ThreeDMolecule.from_mol_file("graphite.mol", "Elementos.csv").scale(0.5).rotate(PI/2.5, axis=[-1, 0, 0])
        diamond = ThreeDMolecule.from_mol_file("diamond.mol", "Elementos.csv").scale(0.5).rotate(PI/2.5)

        
        self.play(FadeIn(graphite))
        
        self.wait()
        
        self.play(
            ReplacementTransform(graphite, diamond),
            run_time=5
        )
                
        self.wait(5)
        
        
class GraphiteStructure(ThreeDScene):
    def construct(self):
        graphite = ThreeDMolecule.from_mol_file("graphite_sheet.mol", "Elementos.csv").scale(0.5)
        self.wait()
        self.play(FadeIn(graphite))
        self.wait(3)
        self.play(
            LaggedStartMap(
                Indicate,
                graphite.copy().atoms.submobjects,
                scale_factor=1.1,
                lag_ratio=0.1,
                func_rate=there_and_back
            ),
            LaggedStartMap(
                Indicate,
                graphite.copy().bonds.submobjects,
                scale_factor=1.1,
                lag_ratio=0.1,
                func_rate=there_and_back
            ),
            run_time=6
        )
        self.wait(3)
        
        
class DiamondStructure(ThreeDScene):
    def construct(self):
        diamond = ThreeDMolecule.from_mol_file("diamond.mol", "Elementos.csv").scale(0.5).rotate(PI/2, axis=[0.25, 1, 0])
        self.wait(2)
        self.play(FadeIn(diamond))
        self.wait()
        self.play(
            LaggedStartMap(
                Indicate,
                diamond.copy().atoms.submobjects,
                scale_factor=1.1,
                lag_ratio=0.1,
                func_rate=there_and_back
            ),
            LaggedStartMap(
                Indicate,
                diamond.copy().bonds.submobjects,
                scale_factor=1.1,
                lag_ratio=0.1,
                func_rate=there_and_back
            ),
            run_time=6
        )
        self.wait(3)
        

class LaminatedGraphite(Scene):
    def construct(self):
        graphite_sheet_1 = ThreeDMolecule.from_mol_file("graphite_sheet.mol", "Elementos.csv").scale(0.5).rotate(PI/2, axis=LEFT).shift(4*UP+3*RIGHT)
        graphite_sheet_2 = graphite_sheet_1.copy().shift(DOWN)
        graphite_sheet_3 = graphite_sheet_1.copy().shift(2*DOWN)
        graphite_sheet_4 = graphite_sheet_1.copy().shift(3*DOWN)
        graphite_sheet_5 = graphite_sheet_1.copy().shift(4*DOWN)
        graphite_sheet_6 = graphite_sheet_1.copy().shift(5*DOWN)
        
        self.wait()
        self.play(
           FadeIn(graphite_sheet_1),
           FadeIn(graphite_sheet_2),
           FadeIn(graphite_sheet_3),
           FadeIn(graphite_sheet_4),
           FadeIn(graphite_sheet_5),
           FadeIn(graphite_sheet_6),
        )
        self.wait()
        self.play(
           graphite_sheet_6.animate.shift(7.5*LEFT),
           graphite_sheet_5.animate.shift(DOWN),
           graphite_sheet_4.animate.shift(DOWN),
           graphite_sheet_3.animate.shift(DOWN),
           graphite_sheet_2.animate.shift(DOWN),
           graphite_sheet_1.animate.shift(DOWN),
           run_time=2
        )
        self.wait(0.5)
        self.play(
           graphite_sheet_6.animate.shift(7.5*LEFT),
           graphite_sheet_5.animate.shift(7.5*LEFT),
           graphite_sheet_4.animate.shift(DOWN),
           graphite_sheet_3.animate.shift(DOWN),
           graphite_sheet_2.animate.shift(DOWN),
           graphite_sheet_1.animate.shift(DOWN),
           run_time=2
        )
        self.wait(0.5)
        self.play(
           graphite_sheet_6.animate.shift(7.5*LEFT),
           graphite_sheet_5.animate.shift(7.5*LEFT),
           graphite_sheet_4.animate.shift(7.5*LEFT),
           graphite_sheet_3.animate.shift(DOWN),
           graphite_sheet_2.animate.shift(DOWN),
           graphite_sheet_1.animate.shift(DOWN),
           run_time=2
        )
        self.wait(0.5)
        self.play(
           graphite_sheet_6.animate.shift(7.5*LEFT),
           graphite_sheet_5.animate.shift(7.5*LEFT),
           graphite_sheet_4.animate.shift(7.5*LEFT),
           graphite_sheet_3.animate.shift(7.5*LEFT),
           graphite_sheet_2.animate.shift(DOWN),
           graphite_sheet_1.animate.shift(DOWN),
           run_time=2
        )
        self.wait(0.5)
        self.play(
           graphite_sheet_6.animate.shift(7.5*LEFT),
           graphite_sheet_5.animate.shift(7.5*LEFT),
           graphite_sheet_4.animate.shift(7.5*LEFT),
           graphite_sheet_3.animate.shift(7.5*LEFT),
           graphite_sheet_2.animate.shift(7.5*LEFT),
           graphite_sheet_1.animate.shift(DOWN),
           run_time=2
        )
        self.wait(0.5)
        self.play(
           graphite_sheet_6.animate.shift(7.5*LEFT),
           graphite_sheet_5.animate.shift(7.5*LEFT),
           graphite_sheet_4.animate.shift(7.5*LEFT),
           graphite_sheet_3.animate.shift(7.5*LEFT),
           graphite_sheet_2.animate.shift(7.5*LEFT),
           graphite_sheet_1.animate.shift(7.5*LEFT),
           run_time=2
        )
        self.wait()
        
        
class DiamondTransform(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=45*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        
        graphite = ThreeDMolecule.from_mol_file("graphite.mol", "Elementos.csv").scale(0.5).rotate(PI/2.5, axis=[-1, 0, 0])
        diamond = ThreeDMolecule.from_mol_file("diamond.mol", "Elementos.csv").scale(0.5).rotate(PI/2.5)

        
        self.play(FadeIn(diamond))
        
        self.wait()
        
        self.play(
            ReplacementTransform(diamond, graphite),
            run_time=15
        )
                
        self.wait(2)
        
class PropertiesTable(Scene):
    def construct(self):
        """
        Properties list:
        - color
        - transparencia
        - Conductividad eléctrica
        - densidad
        - Estabilidad a temperatura ambiente
        
        """
        diamond_properties = [
            "Incoloro, amarillento o azulado,\n entre otras variedades",
            "Transparente",
            "Aislante eléctrico",
            "Frágil",
            "3.5 g/cm3",
            "Metaestable"
        ]
        
        graphite_properties = [
            "Negro o gris oscuro",
            "Opaco",
            "Conductor eléctrico",
            "Posée cierta flexibilidad",
            "2.09 g/cm3",
            "Estable"
        ]
        properties = list(zip(diamond_properties, graphite_properties))
        
        row_labels = [
            Text("Color"),
            Text("Transparencia"),
            Text("Conductividad eléctrica"),
            Text("Tenacidad"),
            Text("Densidad"),
            Text("Estabilidad"),
        ]
        
        column_labels = [
            Text("Diamante"),
            Text("Grafito"),
        ]
        

        
        table = Table(
            properties,
            row_labels=row_labels,
            col_labels=column_labels,
            top_left_entry=Text("Propiedad"),
            include_outer_lines=True,
            entries_background_color=RED
        ).scale(0.5)
        
        self.wait()
        self.play(Write(table), run_time = 4)
        self.wait()