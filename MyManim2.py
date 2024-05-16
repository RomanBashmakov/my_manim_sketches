import shutil
from manim import *

# shutil.rmtree('media')
# os.mkdir('media')
shutil.rmtree(os.path.join('media'))
os.mkdir('media')

class ToyExample(Scene):
    def construct(self):
        # name = Tex(r"Роман", font="Noto Sans")

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(
            r"$\mathscr{R} \rightarrow \mathbb{R}$оман",
            tex_template=myTemplate,
            font_size=144,
        )
        self.play(Create(tex))
        self.wait(2)
