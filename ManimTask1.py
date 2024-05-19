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

        text_Task = Text("Задача", font_size=80)
        text_Arut = Text("от инвестора Арута", font_size=80)
        for letter in text_Arut:
            letter.set_color(random_bright_color())
        gTaskArut = VGroup(text_Task, text_Arut).arrange(direction = DOWN)

        self.play(gTaskArut.animate(run_time=1, lag_ratio=0.1).shift(UP * 5))
        self.wait(0.5)

        text_Bylo = Text('Было a = 100$',t2c={'a = 100':DARK_BLUE}, font_size=96)
        text_Stalo = Text('Стало A = 5000$',t2c={'A = 5000':RED}, font_size=96)
        text_Vremya = Text('За время T = 20 месяцев',t2c={'20 месяцев':DARK_BROWN}, font_size=96)
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

        text_Question = Text("Вопрос:", font_size=80)
        self.play(ReplacementTransform(g, text_Question))
        self.wait(0.2)

        text_Question2 = Text("Вопрос:", font_size=80).next_to(gTaskArut, DOWN * 2)
        self.play(FadeOut(gTaskArut))
        self.play(ReplacementTransform(text_Question, text_Question2))
        self.wait(0.2)
        framebox4 = SurroundingRectangle(text_Question2, buff = .1)
        self.play(Create(framebox4))
        self.wait(0.2)
        self.remove(framebox4)
        self.wait(0.2)

        text_Question3_1 = Text("Помогите")
        text_Question3_1_1 = Text("инвестору Аруту")
        for letter in text_Question3_1_1:
            letter.set_color(random_bright_color())
        text_Question3_2 = Text("найти доходность")
        text_Question3_3 = Text("его портфеля")
        text_Question3_4 = Text("?", font_size=96)

        group_text_Question3 = VGroup(text_Question3_1, text_Question3_1_1, text_Question3_2, text_Question3_3, text_Question3_4).arrange(direction = DOWN)
        # group_text_Question3 = VGroup(text_Question3_1, text_Question3_2, text_Question3_3)

        # paragraph_Question3 = Paragraph(
        #     "Помогите",
        #     "Аруту",
        #     alignment="center",  # Выравнивание по центру
        #     font_size=80,
        # )
        self.play(Write(group_text_Question3))
        self.wait(0.2)

class Zadacha_Ot_Aruta_Solving(Scene):
    def construct(self):

        self.wait(0.2)
