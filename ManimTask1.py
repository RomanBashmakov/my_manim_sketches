import os
import shutil
from manim import *

# shutil.rmtree('media')
# os.mkdir('media')
shutil.rmtree(os.path.join('media'))
os.mkdir('media')

class ToyExample(Scene):
    def construct(self):
        name = Tex(r"Роман")

        # myTemplate = TexTemplate()
        # myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        # tex = Tex(r"Roman")

        self.play(Create(name)) 
        self.wait(2)

        # text_Task = Text("Задача от ", font_size=96)
        # # self.add(text_Task)

        # text_Arut = Text("Арута", font_size=96)
        # for letter in text_Arut:
        #     letter.set_color(random_bright_color())

        # group = VGroup(text_Task, text_Arut).arrange(RIGHT)
        # self.play(Create(group))

class Zadacha_Ot_Aruta(Scene):
    def construct(self):

        # Задача от инвестора Арута
        text_Task = Text("Задача", font_size=80)
        text_Arut = Text("от инвестора Арута", font_size=80)
        for letter in text_Arut:
            letter.set_color(random_bright_color())
        gTaskArut = VGroup(text_Task, text_Arut).arrange(direction = DOWN)

        self.play(gTaskArut.animate(run_time=1, lag_ratio=0.1).shift(UP * 5))
        self.wait(0.5)

        # Условия задачи
        text_Bylo = Text('Было a = 2000$',t2c={'a = 2000':DARK_BLUE}, font_size=96)
        text_Stalo = Text('Стало A = 40000$',t2c={'A = 40000':RED}, font_size=96)
        text_Vremya = Text('За n = 20 месяцев',t2c={'n = 20':DARK_BROWN}, font_size=96)
        g = VGroup(text_Bylo, text_Stalo, text_Vremya).scale(0.5).arrange(direction = DOWN, aligned_edge = LEFT).next_to(gTaskArut,DOWN * 5).shift(LEFT * 2)

        self.play(Create(g))

        framebox1 = SurroundingRectangle(text_Bylo[0:13], buff = .1)
        framebox2 = SurroundingRectangle(text_Stalo[0:15], buff = .1)
        framebox3 = SurroundingRectangle(text_Vremya[0:23], buff = .1)
        self.play(
            Create(framebox1),
        )
        # self.wait(0.2)
        self.play(ReplacementTransform(framebox1,framebox2))
        # self.wait(0.2)
        self.remove(framebox1)
        self.play(ReplacementTransform(framebox2,framebox3))
        # self.wait(0.2)
        self.remove(framebox3)
        self.wait(0.2)

        # Вопрос задачи
        text_Question = Text("Вопрос:", font_size=80)
        self.play(ReplacementTransform(g, text_Question))
        self.wait(0.2)

        text_Question2 = Text("Вопрос:", font_size=80).next_to(gTaskArut, DOWN * 2)
        self.play(FadeOut(gTaskArut))
        self.play(ReplacementTransform(text_Question, text_Question2))
        self.wait(0.2)
        framebox4 = SurroundingRectangle(text_Question2, buff = .1)
        self.play(FadeOut(framebox4))
        self.wait(0.2)

        text_Question3_2 = Text("Доходность")
        text_Question3_3 = Text("его портфеля")
        text_Question3_4 = Text("?", font_size=96)
        group_text_Question3 = VGroup(text_Question3_2, text_Question3_3, text_Question3_4).arrange(direction = DOWN)

        self.play(Write(group_text_Question3))
        self.wait(0.2)

        framebox5 = SurroundingRectangle(text_Question3_2, buff = .1)

        self.play(Write(framebox5))
        self.wait(0.2)
        self.play(FadeOut(framebox5))
        self.wait(0.2)
        self.play(FadeOut(text_Question2))
        self.wait(0.2)

        # Вопрос на весь экран
        text_quastion_mark = Text("?", font_size=280)
        self.play(ReplacementTransform(group_text_Question3, text_quastion_mark))
        self.wait(0.2)
        self.play(FadeOut(text_quastion_mark))
        self.wait(0.2)

class Zadacha_Ot_Aruta_Solving(Scene):
    def construct(self):

        text_Formula_1 = Text("Формула", font_size = 150)
        text_Formula_2 = Text("Cложныe", font_size = 230) 
        text_Formula_2_1 = Text("проценты", font_size = 230) 
        group_text_Formula = VGroup(text_Formula_2, text_Formula_2_1).arrange(direction = DOWN)

        self.play(Create(group_text_Formula))
        self.wait(0.2)

        self.play(group_text_Formula.animate.shift(UP * 5))
        self.wait(0.2)

        matex_1 = MathTex(
            r"A = a(1+p)^{n}",
            substrings_to_isolate="p",
            font_size = 200
        )

        matex_1_1 = MathTex(
            r"A = a(1+p)^{n}",
            substrings_to_isolate="p",
            font_size = 200
        )
        matex_1_1.set_color_by_tex("p", YELLOW)

        self.play(Create(matex_1))
        
        self.wait(0.2)

        self.play(ReplacementTransform(matex_1, matex_1_1)) #TransformFromCopy
        self.wait(0.2)

        self.play(matex_1_1[1].animate.shift(UP))
        self.wait(0.2)
        self.play(matex_1_1[1].animate.shift(DOWN))

        matex_2 = MathTex(
            r"p = \left( \frac{A}{a} \right)^{\frac{1}{n}} - 1",
            substrings_to_isolate="p",
            font_size = 200
        ).move_to(DOWN * 4).set_color_by_tex("p", YELLOW)

        self.play(ReplacementTransform(matex_1_1[1], matex_2))

        matex_2_2 = MathTex(
            r"p = \left( \frac{A}{a} \right)^{\frac{1}{n}} - 1",
            substrings_to_isolate=["p"],
            font_size = 200
        ).move_to(DOWN * 4).set_color_by_tex("p", YELLOW)

        self.play(ReplacementTransform(matex_2, matex_2_2))
        self.wait(0.2)

        self.play(FadeOut(matex_1_1, group_text_Formula))
        self.wait(0.2)

        self.play(matex_2_2.animate.shift(UP * 8))
        self.wait(0.2)

        matex_2_2.set_color_by_tex("p", WHITE)
        
        text_Bylo = Text('a = 2000$',t2c={'a':DARK_BLUE}, font_size = 250)
        text_Stalo = Text('A = 40000$',t2c={'A':RED}, font_size = 250)
        text_Vremya = Text('n = 20 месяцев',t2c={'n':DARK_BROWN}, font_size = 250)
        g = VGroup(text_Bylo, text_Stalo, text_Vremya).scale(0.5).arrange(direction = DOWN).next_to(matex_2_2,DOWN * 5)#.arrange(direction = DOWN, aligned_edge = LEFT).shift(LEFT * 2)

        self.play(Create(g))
        self.wait(0.2)

        matex_2_3 = MathTex(
            r"p = \left( \frac{A}{a} \right)^{\frac{1}{n}} - 1",
            font_size = 200
        ).move_to(matex_2_2.get_center())
        # self.add(index_labels(matex_2_3[0]))
        matex_2_3[0][5].set_color(DARK_BLUE)

        self.remove(matex_2_2)
        self.add(matex_2_3)
        self.wait(0.5)

        matex_2_3[0][3].set_color(RED)
        self.wait(0.5)

        matex_2_3[0][9].set_color(DARK_BROWN)
        self.wait(0.5)

        self.play(FadeOut(g))
        self.wait(0.2)

        matex_3 = Tex(
            r"$p \approx 16\frac{\%}{\text{месяц}}$",
            font_size = 200
        )

        self.play(ReplacementTransform(matex_2_3, matex_3))
        self.wait(0.2)

        self.play(matex_3.animate.shift(UP * 2))
        self.wait(0.2)

        matex_4 = Tex(
            # r"$p \approx 600\%/\text{год}$",
            r"$p \approx 600 \frac{\%}{\text{год}}$",
            
            font_size = 200
        ).next_to(matex_3, DOWN * 4)

        self.play(Create(matex_4))
        self.wait(0.2)

        # Вопрос на весь экран
        text_quastion_mark = Text("?", font_size=580)
        self.play(FadeOut(matex_3))
        self.play(ReplacementTransform(matex_4, text_quastion_mark))
        self.wait(0.2)
