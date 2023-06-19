from manim import *
from manim_chemistry import *

COLOR_0 = "#24283B"
COLOR_A = "#F7768E"
COLOR_B = "#9ECE6A"
COLOR_C = "#E0AF68"
COLOR_D = "#7AA2F7"
COLOR_E = "#BB9AF7"
COLOR_F = "#7DCFFF"
COLOR_GRAY = "#8B93B5"

config.background_color = COLOR_0

class Photoprotectors(Scene):
    def construct(self):
        organic_traditional = MarkupText("<span underline='double'>Orgánicos tradicionales</span>").scale(0.5).shift(3.5*UP)
        traditional_rectangle = Rectangle(width=13.7, height=5.5, stroke_width=3).shift(1.1*UP)
        
        organic_particulated = MarkupText("<span underline='double'>Orgánicos particulados</span>").scale(0.5).shift(2*DOWN)
        organic_polimeric = MarkupText("<span underline='double'>Orgánicos poliméricos</span>").scale(0.5).shift(2*DOWN+5*LEFT)
        inorganic_particulated = MarkupText("<span underline='double'>Inorgánicos particulados</span>").scale(0.5).shift(2*DOWN+4.8*RIGHT)
        
        # Organic traditional
        benzylidene_camphor = MMoleculeObject.from_mol_file("molecules/t_benzylidene_camphor.mol").rotate_bond([15]).scale(0.15).set_style(stroke_width=1).move_to([-6.1,3.2,0])
        amiloxate = MMoleculeObject.from_mol_file("molecules/amiloxate.mol").rotate_bond(2).scale(0.15).set_style(stroke_width=1).move_to([-5.5, 2.5, 0])
        avobenzone = MMoleculeObject.from_mol_file("molecules/avobenzone.mol").scale(0.15).rotate_bond([2, 14]).set_style(stroke_width=1).move_to([-4.3,3.2,0])
        bemotrizinol = MMoleculeObject.from_mol_file("molecules/bemotrizinol.mol").scale(0.15).rotate_bond([2, 14]).set_style(stroke_width=1).move_to([-5.2, 1.5, 0]).rotate_bond([10, 16, 23, 36, 41])
        benzophenone3 = MMoleculeObject.from_mol_file("molecules/benzophenone3.mol").scale(0.15).rotate_bond([3, 10]).set_style(stroke_width=1).move_to([-3, 3.3, 0])
        benzophenone4 = MMoleculeObject.from_mol_file("molecules/benzophenone4.mol").scale(0.15).rotate_bond([3, 10]).set_style(stroke_width=1).move_to([-3, 2.4, 0])
        benzophenone5 = MMoleculeObject.from_mol_file("molecules/benzophenone5.mol").scale(0.15).rotate_bond([3, 10]).set_style(stroke_width=1).move_to([-1.5, 2.5, 0])
        benzophenone5[1][22].set_opacity(0)
        benzotriazolyl_tetramethylbutylphenol = MMoleculeObject.from_mol_file("molecules/benzotriazolyl_tetramethylbutylphenol.mol").scale(0.15).rotate_bond(21).set_style(stroke_width=1).move_to([0, 2.3, 0])
        benzylidene_camphor_sulfonic_acid = MMoleculeObject.from_mol_file("molecules/benzylidene_camphor_sulfonic_acid.mol").scale(0.15).rotate_bond([14, 18]).set_style(stroke_width=1).move_to([-1.2, 1.5, 0])
        bisdisulizole_disodium = MMoleculeObject.from_mol_file("molecules/bisdisulizole_disodium.mol").scale(0.15).rotate_bond([3, 22, 29]).set_style(stroke_width=1).move_to([3.6, 3.2, 0])
        bisdisulizole_disodium[1][44:46].set_opacity(0)
        dimethylaminobenzoate = MMoleculeObject.from_mol_file("molecules/dimethylaminobenzoate.mol").scale(0.15).rotate_bond(2).set_style(stroke_width=1).move_to([-4.2, 2.4, 0])
        drometrizole_trisiloxane = MMoleculeObject.from_mol_file("molecules/drometrizole_trisiloxane.mol").scale(0.15).rotate_bond([2, 18]).set_style(stroke_width=1).move_to([1.6, 2.5, 0])
        ethylhexyl_salicylate = MMoleculeObject.from_mol_file("molecules/ethylhexyl_salicylate.mol").scale(0.15).rotate_bond(2).set_style(stroke_width=1).move_to([-4.3, 0, 0])
        ethylhexyl_triazone = MMoleculeObject.from_mol_file("molecules/ethylhexyl_triazone.mol").scale(0.15).set_style(stroke_width=1).rotate_bond([11, 30, 39]).move_to([1.6, 1.2, 0])
        homosalate = MMoleculeObject.from_mol_file("molecules/homosalate.mol").scale(0.15).rotate_bond([1, 6]).set_style(stroke_width=1).move_to([-2.4, 1.7, 0])
        iscotrizinol = MMoleculeObject.from_mol_file("molecules/iscotrizinol.mol").scale(0.15).rotate_bond([46, 47, 53]).set_style(stroke_width=1).move_to([5, 0.85, 0])
        methylbenzylidene_camphor = MMoleculeObject.from_mol_file("molecules/methylbenzylidene_camphor.mol").scale(0.15).rotate_bond(15).set_style(stroke_width=1).move_to([0, 1, 0])
        octinoxate = MMoleculeObject.from_mol_file("molecules/octinoxate.mol").scale(0.15).rotate_bond(2).set_style(stroke_width=1).move_to([-1, 0.25, 0])
        octocrylene = MMoleculeObject.from_mol_file("molecules/octocrylene.mol").scale(0.15).rotate_bond([8, 16]).set_style(stroke_width=1).move_to([-6.2, 0.2, 0])
        PABA = MMoleculeObject.from_mol_file("molecules/PABA.mol").scale(0.15).rotate_bond(2).set_style(stroke_width=1).move_to([-6.3, 2.1, 0])
        PABA[0][7].shift(0.4*RIGHT)
        PEG_25_PABA = MMoleculeObject.from_mol_file("molecules/PEG_25_PABA.mol").scale(0.15).set_style(stroke_width=1).rotate_bond(2).move_to([-2.75, 0.2, 0])
        PEG_25_PABA[0][25].shift(0.3*RIGHT)
        PEG_25_PABA[0][19].shift(0.3*RIGHT)
        phenyl_trimethylammonium_methylsulphate = MMoleculeObject.from_mol_file("molecules/phenyl_trimethylammonium_methylsulphate.mol").rotate_bond([14, 18]).set_style(stroke_width=1).scale(0.15).move_to([-5.75, -1.1, 0])  # Intentar añadir cargas
        phenyl_trimethylammonium_methylsulphate[0][27][0][1].set_opacity(0)
        phenyl_trimethylammonium_methylsulphate[0][27][0].shift(0.075*RIGHT)
        phenylbenzimidazole_sulphonic_acid = MMoleculeObject.from_mol_file("molecules/phenylbenzimidazole_sulphonic_acid.mol").set_style(stroke_width=1).scale(0.15).rotate_bond([11, 3]).move_to([0, -0.75, 0])
        rerephthalylidene_dicamphor_sulfonic_acid = MMoleculeObject.from_mol_file("molecules/rerephthalylidene_dicamphor_sulfonic_acid.mol").set_style(stroke_width=1).scale(0.15).rotate_bond(19).move_to([5, -0.85, 0])
        t_benzylidene_camphor = MMoleculeObject.from_mol_file("molecules/t_benzylidene_camphor.mol").set_style(stroke_width=1).rotate_bond(15).scale(0.15).move_to([5.5, 2, 0])
        uvinil_a_plus = MMoleculeObject.from_mol_file("molecules/uvinil_a_plus.mol").set_style(stroke_width=1).scale(0.15).rotate_bond([2, 17]).move_to([2.5, -0.25, 0])
        
        # Organic polimeric (Done)
        polysilicone = Text("Polisilicona-15").shift(3*DOWN+4*LEFT).scale(0.3)
        polyacrylamido_methylbenzylidene_camphor = Text("Poliacrilamido-metilbencilideno-alcanfor").shift(2.5*DOWN+5*LEFT).scale(0.3)
        
        # Organic particulated (Done)
        bisoctrizole = MMoleculeObject.from_mol_file("molecules/bisoctrizole.mol").scale(0.15).shift(3*DOWN).set_style(stroke_width=1).rotate_bond([7, 13, 34, 39, 44])
        
        # Inorganic particulated (Done)
        tio2 = MarkupText("TiO<sub>2</sub>").shift(3*DOWN+4*RIGHT).scale(0.5)
        zno2 = MarkupText("ZnO<sub>2</sub>").shift(2.5*DOWN+6*RIGHT).scale(0.5)

        molecules_list = [
            benzylidene_camphor,
            amiloxate,
            avobenzone,
            bemotrizinol,
            benzophenone3,
            benzophenone4,
            benzophenone5,
            benzotriazolyl_tetramethylbutylphenol,
            benzylidene_camphor_sulfonic_acid,
            bisdisulizole_disodium,
            dimethylaminobenzoate,
            drometrizole_trisiloxane,
            ethylhexyl_salicylate,
            ethylhexyl_triazone,
            homosalate,
            iscotrizinol,
            methylbenzylidene_camphor,
            octinoxate,
            octocrylene,
            PABA,
            PEG_25_PABA,
            phenyl_trimethylammonium_methylsulphate,
            phenylbenzimidazole_sulphonic_acid,
            rerephthalylidene_dicamphor_sulfonic_acid,
            t_benzylidene_camphor,
            uvinil_a_plus,
            polysilicone,
            polyacrylamido_methylbenzylidene_camphor,
            bisoctrizole,
            tio2,
            zno2
        ]
        
        
        self.play(
            FadeIn(organic_traditional),
            FadeIn(organic_particulated),
            FadeIn(organic_polimeric),
            FadeIn(inorganic_particulated)
        )
        
        self.wait()
        
        self.play(LaggedStart(*[Write(molecule) for molecule in molecules_list]), lag_ratio=0.5, run_time=4)
        
        self.wait()
        
        """
            Derivados de PABA
            Cinamatos
            Oxybenzonas
            Salicilatos
            Dibenzoilmetanos
            Triazinas
            Benzotriazoles
            Alcanfores
            Óxidos inorgánicos
        """
        
        pabas = Text("PABAs", color=COLOR_B, font_size=30).move_to([3, 3.5, 0])
        cinamatos = Text("Cinamatos", color=COLOR_E, font_size=30).move_to([5.5, 1.5, 0])
        oxibenzonas = Text("Oxibenzonas", color=COLOR_C, font_size=30).move_to([0.2, 2, 0])
        salicilatos = Text("Salicilatos", color=COLOR_D, font_size=30).move_to([3, 1, 0])
        dibenzoilmetanos = Text("Dibenzoilmetanos", color=COLOR_F, font_size=30).move_to([-0.5, 1.5, 0])
        triazinas = Text("Triazinas", color=GOLD_A, font_size=30).move_to([3, -0.5, 0])
        benzotriazoles = Text("Benzotriazoles", color=TEAL_C, font_size=30).move_to([-5, -0.25, 0])
        alcanfores = Text("Alcanfores", color=COLOR_A, font_size=30).move_to([-5, 0.5, 0])
        inorganicos = Text("Óxidos inorgánicos", color=COLOR_GRAY, font_size=30).move_to([-1.7, -2, 0])
        polímeros = Text("Polímeros", font_size=30).move_to([-2.2, -2.5, 0])
        otros = Text("Otros", color=MAROON_A, font_size=30).move_to([1, 0.5, 0])
        

        
        self.play(
            FadeOut(organic_traditional),
            FadeOut(organic_particulated),
            FadeOut(organic_polimeric),
            FadeOut(inorganic_particulated)
        )
        
        self.wait()
        
        self.play(
            LaggedStart(
                #PABAS #DONE
                PABA.animate.set_color(COLOR_B).move_to([6.5, 3, 0]),
                PEG_25_PABA.animate.set_color(COLOR_B).move_to([5.5, 3, 0]),
                dimethylaminobenzoate.animate.set_color(COLOR_B).move_to([4.5, 3, 0]),

                # Cinamatos #DONE
                amiloxate.animate.set_color(COLOR_E).move_to([5, 0, 0]),
                octinoxate.animate.set_color(COLOR_E).move_to([6, 0, 0]),

                # Salicilatos #DONE
                ethylhexyl_salicylate.animate.set_color(COLOR_D).move_to([2.7, 1.7, 0]),
                homosalate.animate.set_color(COLOR_D).move_to([3, 2.7, 0]),

                #Dibenzoilmetanos #DONE
                avobenzone.animate.set_color(COLOR_F).move_to([-2, 2, 0]),

                # Triazinas #DONE
                ethylhexyl_triazone.animate.set_color(GOLD_A).move_to([5.5, -2.5, 0]),
                iscotrizinol.animate.set_color(GOLD_A).move_to([2, -1.5, 0]),
                bemotrizinol.animate.set_color(GOLD_A).move_to([3, -2.5, 0]),

                # Benzotriazoles #DONE
                bisdisulizole_disodium.animate.set_color(TEAL_C).move_to([-5.5, -1, 0]),
                drometrizole_trisiloxane.animate.set_color(TEAL_C).move_to([-6, -2.25, 0]),
                benzotriazolyl_tetramethylbutylphenol.animate.set_color(TEAL_C).move_to([-4.25, -2.75, 0]),
                phenylbenzimidazole_sulphonic_acid.animate.set_color(TEAL_C).move_to([-6, -3, 0]),

                # Oxibenzonas #DONE
                benzophenone3.animate.set_color(COLOR_C).move_to([0, 2.8, 0]),
                benzophenone4.animate.set_color(COLOR_C).move_to([-1.2, 3.2, 0]),
                benzophenone5.animate.set_color(COLOR_C).move_to([1.2, 3.2, 0]),

                # Alcanfores #DONE
                benzylidene_camphor.animate.set_color(COLOR_A),
                benzylidene_camphor_sulfonic_acid.animate.set_color(COLOR_A).move_to([-5, 3.2, 0]),
                methylbenzylidene_camphor.animate.set_color(COLOR_A).move_to([-4, 3, 0]),
                rerephthalylidene_dicamphor_sulfonic_acid.animate.set_color(COLOR_A).move_to([-5.5, 2, 0]),
                t_benzylidene_camphor.animate.set_color(COLOR_A).move_to([-3.5, 2, 0]),
                phenyl_trimethylammonium_methylsulphate.animate.set_color(COLOR_A).move_to([-6, 1, 0]),

                #Polímeros #DONE
                polysilicone.animate.move_to([-2.5, -3, 0]),
                polyacrylamido_methylbenzylidene_camphor.animate.move_to([-1.2, -3.5, 0]),

                # Inorganic oxides #DONE
                tio2.animate.set_color(COLOR_GRAY).move_to([-1.5, -1.5, 0]),
                zno2.animate.set_color(COLOR_GRAY).move_to([-3, -1.5, 0]),

                # Others #DONE
                octocrylene.animate.set_color(MAROON_A).move_to([-2.5, -0.4, 0]),
                uvinil_a_plus.animate.set_color(MAROON_A).move_to([-0.2, 0, 0]),
                bisoctrizole.animate.set_color(MAROON_A).move_to([-1.5, 0.5, 0]),
                lag_ratio=0.1,
                run_time=4
            )
        )
        
        self.wait()
        
        self.play(
            FadeIn(pabas),
            FadeIn(cinamatos),
            FadeIn(oxibenzonas),
            FadeIn(salicilatos),
            FadeIn(dibenzoilmetanos),
            FadeIn(triazinas),
            FadeIn(benzotriazoles),
            FadeIn(alcanfores),
            FadeIn(inorganicos),
            FadeIn(polímeros),
            FadeIn(otros)
        )
        self.wait()