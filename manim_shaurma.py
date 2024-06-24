
import os
import shutil
from manim import *

shutil.rmtree(os.path.join('media'))
os.mkdir('media')

class Shaurma(MovingCameraScene):
    def construct(self):
        mob = SVGMobject("shaw.svg") 
        # self.play(Create(mob))
        # self.wait(1)

        # Размеры сетки
        rows = 5
        cols = 5

        # Создаем несколько текстовых объектов
        texts = [Text(f"Item {i}") for i in range(1, (rows * cols))]
        mobs = [SVGMobject("shaw.svg").scale(0.5) for i in range(0, (rows * cols))]

        # Размеры сетки
        rows = 5
        cols = 5

        # Определяем шаги по x и y
        x_step = 2.5
        y_step = 1.5

        # Располагаем объекты по сетке
        for i, mob in enumerate(mobs):
            row = i // cols
            col = i % cols
            mob.move_to(np.array([col * x_step - (cols-1) * x_step / 2, 
                                   -(row * y_step) + (rows-1) * y_step / 2, 0]))

        # Группируем все объекты
        grid = VGroup(*mobs)

        # # Добавляем сетку на сцену
        # self.add(grid)

        # Анимация появления сетки
        self.play(Create(grid))
        self.wait(2)

        self.play(mobs[0].animate.shift(UP * 6, ).scale(2))
        self.wait(2)

        