import shutil
from manim import *

# shutil.rmtree('media')
# os.mkdir('media')
shutil.rmtree(os.path.join('media'))
os.mkdir('media')

class ToyExample(Scene):
    def construct(self):
        circles = VGroup(*[Circle(radius=0.2, color=BLUE) for _ in range(10)])
        circles.arrange_in_grid(buff=0.2)
        self.play(Create(circles))
        self.wait(2)
