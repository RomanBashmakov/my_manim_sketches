import shutil
from manim import *

# shutil.rmtree('media')
# os.mkdir('media')
shutil.rmtree(os.path.join('media'))
os.mkdir('media')

class ToyExample(Scene):
    def construct(self):
        # name = Tex(r"Роман", font="Noto Sans")

        # myTemplate = TexTemplate()
        # myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        # tex = Tex(r"Roman")

        # self.play(Create(tex)) 
        # self.wait(2)


        text_Task = Text("Задача от ", font_size=96)
        # self.add(text_Task)

        text_Arut = Text("Арута ", font_size=96)
        for letter in text_Arut:
            letter.set_color(random_bright_color())

        group = VGroup(text_Task, text_Arut).arrange(RIGHT)
        self.play(Create(group))

