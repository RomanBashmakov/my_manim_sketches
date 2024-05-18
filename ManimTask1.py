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

        text_Task = Text("Задача от ", font_size=96)
        # self.add(text_Task)

        text_Arut = Text("Арута", font_size=96)
        for letter in text_Arut:
            letter.set_color(random_bright_color())

        group = VGroup(text_Task, text_Arut).arrange(RIGHT)
        # group.next_to(ORIGIN)
        self.play(Create(group))
        # self.wait(1)
        self.play(group.animate(run_time=1, lag_ratio=0.1).shift(UP * 2))
        self.wait(0.5)

        # text_Bylo = Text("Было", font_size=96)
        # text_Bylo = MarkupText('<span foreground="blue" size="x-large">Blue text</span> is <i>cool</i>!"')
        text_Bylo = Text('Было 100$',t2c={'100':DARK_BLUE}, font_size=96)
        # self.play(Create(text_Bylo))
        # self.wait(1)

        text_Stalo = Text('Стало 5000$',t2c={'5000':RED}, font_size=96)
        # self.play(Create(text_Stalo))
        # self.wait(1)

        g = VGroup(text_Bylo, text_Stalo).arrange(direction = DOWN, aligned_edge = LEFT).scale(0.7).next_to(group,DOWN).shift(LEFT * 2)

        self.play(Create(g))

        # self.add(text_Bylo, text_Stalo)

        # self.play(Create(text_Bylo))
        # self.play(Create(text_Stalo))

        self.wait(1)

