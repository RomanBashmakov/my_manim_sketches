
import os
import shutil
from manim import *

shutil.rmtree(os.path.join('media'))
os.mkdir('media')

class PieChart(MovingCameraScene):
    def construct(self):
        