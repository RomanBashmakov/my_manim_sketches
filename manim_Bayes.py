# self.add(index_labels(matex_2_3[0]))

import os
import shutil
from manim import *

# Какой шанс, что твой партнер уже умер, если прямо сейчас не отвечает на телефон?

# Не торопись обзванивать морги, давай сначала прикинем, чем этот партнер так занят?
# Эта сволочь скорее всего не очень умная, раз не ценит тебя, поэтому список занятий будет выглядеть как-то так:
    # умирает - 5 %
    # изменяет с девушкой - 5 % 
    # изменяет с парнем - 5 %
    # изменяет с коллегой - 5 %
    # изменяет с соседской собакой - 80 %
# Возле каждой опции прикинем вероятность того, что именно этим партнер сейчас и занят. Чем лучше вы его знаете, тем выше будет точность!
# Предположим теперь, что в каждой из этих опций, партнер не сможет тебе перезвонить с вероятностью 50%.

# Итак, событие "не перезвонил" уже случилось, давайте тогда найдем апостериорную вероятность того, что он умер!

# Для этого нам понадобятся формула полной вероятности и формула Байеса. Как ими пользоваться я расскажу у себя на канале, а пока что взглянем на результат!
# Ого, все не так страшно, ваш партнер мертв с вероятностью лишь Х%

# Ставь лайк, если тебя тоже успокаивает математика.

shutil.rmtree(os.path.join('media'))
os.mkdir('media')

class PieChart(MovingCameraScene):
    def construct(self):
        text_smert = Text('умирает - 5%', font = "Bradley Hand", font_size = 25)
        text_girl = Text('изменяет с девушкой - 5%', font = "Bradley Hand", font_size = 25)
        text_boy = Text('изменяет с парнем - 5%', font = "Bradley Hand", font_size = 25)
        text_colegue = Text('изменяет с коллегой - 5%', font = "Bradley Hand", font_size = 25)
        text_dog = Text('изменяет с собакой - 80%', font = "Bradley Hand", font_size = 25)

        self.camera.background_color = GRAY
        # Данные для круговой диаграммы
        data = [5, 5, 5, 5, 80]  # Проценты для каждого сектора
        colors = [BLACK, GREEN, BLUE, RED, ORANGE]  # Цвета для каждого сектора
        labels = ["умирает - 5%", "изменяет с девушкой - 5%", "изменяет с парнем - 5 %", "изменяет с коллегой - 5 %", "изменяет с соседской собакой - 80 %"]  # Метки для каждого сектора
        # Сумма всех значений данных
        total = sum(data)

        # Начальный угол
        start_angle = 0

        # Список для хранения секторов
        sectors = []

        # Создание секторов
        for value, color, label in zip(data, colors, labels):
            angle = value / total * TAU
            sector = Sector(start_angle = start_angle, angle = angle, color = color)
            sectors.append(sector)

            label_text = Text(label, font = "Bradley Hand", font_size = 12)
            self.play(self.camera.frame.animate.move_to(sector).set(width=label_text.width * 1.1))
            self.add(sector)

            # text_smert.move_to(sector, UP *2)
            # self.add(sector)

            # Расчет угла для размещения метки
            # mid_angle = start_angle + angle / 2
            # radius = 1.5  # Радиус, на котором будет размещена метка
            # label_x = radius * np.cos(mid_angle)
            # label_y = radius * np.sin(mid_angle)
            # label_position = np.array([label_x, label_y, 0])

            # Добавление метки
            label_text.move_to(sector.get_top(), DOWN)

            self.play(Create(label_text))

            self.wait(0.5)

            # self.remove(label_text)
            self.play(FadeOut(label_text))

            # Обновление начального угла для следующего сектора
            start_angle += angle

        # Анимация появления круговой диаграммы
        
        self.play(*[Create(sector) for sector in sectors])
        self.wait(0.2)
        self.play(self.camera.frame.animate.move_to(sector, UP * 3).set(width=sector.width * 1.5))


        # labels = ["умирает", "изменяет с девушкой", "изменяет с парнем", "изменяет с коллегой", "изменяет с соседской собакой"]  # Метки для каждого сектора
        g = VGroup(text_smert, text_girl, text_boy, text_colegue, text_dog).scale(0.5).arrange(direction = DOWN, buff = 0.1, aligned_edge=LEFT).next_to(sector,DOWN * 1)#.align_to(sector, LEFT)#.arrange(aligned_edge = LEFT)#.shift(LEFT * 2)

        self.play(Create(g))

        # self.play(self.camera.frame.animate.move_to(g).set(width=g.width * 1))

        self.wait(0.2)

        text_neOtvetit = Text('Вероятность не ответить - 50%', font = "Bradley Hand", font_size = 25)
        text_neOtvetit.move_to(g.get_bottom() + DOWN)
        self.add(text_neOtvetit)

        curvedDoubleArrow_1 = CurvedArrow (start_point = text_neOtvetit.get_left(),
                                               end_point = text_smert.get_left(),
                                               tip_shape = None,
                                               stroke_width = 1,
                                               radius = - 2)

        curvedDoubleArrow_2 = CurvedArrow (start_point = text_neOtvetit.get_left(),
                                               end_point = text_girl.get_left(),
                                               tip_shape = None,
                                               stroke_width = 1,
                                               radius = - 2)

        curvedDoubleArrow_3 = CurvedArrow (start_point = text_neOtvetit.get_left(),
                                               end_point = text_boy.get_left(),
                                               tip_shape = None,
                                               stroke_width = 1,
                                               radius = - 2)

        curvedDoubleArrow_4 = CurvedArrow (start_point = text_neOtvetit.get_left(),
                                               end_point = text_colegue.get_left(),
                                               tip_shape = None,
                                               stroke_width = 1,
                                               radius = - 2)

        curvedDoubleArrow_5 = CurvedArrow (start_point = text_neOtvetit.get_left(),
                                               end_point = text_dog.get_left(),
                                               tip_shape = None,
                                               stroke_width = 1,
                                               radius = - 2)
        
        self.play(self.camera.frame.animate.move_to(text_neOtvetit).set(width=text_neOtvetit.width * 1.2))
        self.play(Create(curvedDoubleArrow_1), run_time = 0.2)
        self.play(Create(curvedDoubleArrow_2), run_time = 0.2)
        self.play(Create(curvedDoubleArrow_3), run_time = 0.2)
        self.play(Create(curvedDoubleArrow_4), run_time = 0.2)
        self.play(Create(curvedDoubleArrow_5), run_time = 0.2)
        self.wait(0.5)



class PieChart_2(MovingCameraScene):
    def construct(self):

        self.camera.background_color = GRAY

        text_smert = Text('умирает - 5%', font = "Bradley Hand", font_size = 25)
        text_girl = Text('изменяет с девушкой - 5%', font = "Bradley Hand", font_size = 25)
        text_boy = Text('изменяет с парнем - 5%', font = "Bradley Hand", font_size = 25)
        text_colegue = Text('изменяет с коллегой - 5%', font = "Bradley Hand", font_size = 25)
        text_dog = Text('изменяет с собакой - 80%', font = "Bradley Hand", font_size = 25)

        text_neOtvetit = Text('Вероятность не ответить - 50%', font = "Bradley Hand", font_size = 25)

        g = VGroup(text_smert, text_girl, text_boy, text_colegue, text_dog).scale(0.5).arrange(direction = DOWN, buff = 0.1, aligned_edge=LEFT)#.next_to(sector,DOWN * 1)#.align_to(sector, LEFT)#.arrange(aligned_edge = LEFT)#.shift(LEFT * 2)

        self.play(self.camera.frame.animate.move_to(g).set(width=g.width * 1.2))

        self.play(Create(g))

        self.wait(0.2)

        # curvedDoubleArrow = CurvedDoubleArrow (start_point = np.array([-2, -1, 0]),
        #                                        end_point = np.array([2, 1, 0]))

        text_neOtvetit.move_to(g.get_bottom() + DOWN)
        self.add(text_neOtvetit)

        curvedDoubleArrow_1 = CurvedArrow (start_point = text_neOtvetit.get_left(),
                                               end_point = text_smert.get_left(),
                                               tip_shape = None,
                                               stroke_width = 1,
                                               radius = - 2)

        curvedDoubleArrow_2 = CurvedArrow (start_point = text_neOtvetit.get_left(),
                                               end_point = text_girl.get_left(),
                                               tip_shape = None,
                                               stroke_width = 1,
                                               radius = - 2)

        curvedDoubleArrow_3 = CurvedArrow (start_point = text_neOtvetit.get_left(),
                                               end_point = text_boy.get_left(),
                                               tip_shape = None,
                                               stroke_width = 1,
                                               radius = - 2)

        curvedDoubleArrow_4 = CurvedArrow (start_point = text_neOtvetit.get_left(),
                                               end_point = text_colegue.get_left(),
                                               tip_shape = None,
                                               stroke_width = 1,
                                               radius = - 2)

        curvedDoubleArrow_5 = CurvedArrow (start_point = text_neOtvetit.get_left(),
                                               end_point = text_dog.get_left(),
                                               tip_shape = None,
                                               stroke_width = 1,
                                               radius = - 2)
        
        self.play(self.camera.frame.animate.move_to(text_neOtvetit).set(width=text_neOtvetit.width * 1.2))
        self.play(Create(curvedDoubleArrow_1), run_time = 0.2)
        self.play(Create(curvedDoubleArrow_2), run_time = 0.2)
        self.play(Create(curvedDoubleArrow_3), run_time = 0.2)
        self.play(Create(curvedDoubleArrow_4), run_time = 0.2)
        self.play(Create(curvedDoubleArrow_5), run_time = 0.2)
        self.wait(0.5)


class PieChart_Formulas(MovingCameraScene):
    def construct(self):

        self.camera.background_color = GRAY
        
        f1 = MathTex(
                r" P(B|A) = \frac{P(B|A)P(B)}{P(A)}",
                font_size = 300
            )
        
        self.play(self.camera.frame.animate.move_to(f1).set(width=f1.width * 1.2))
        self.play(Create(f1))
        self.wait(0.5)

        f2 = MathTex(
                r" P(B|A) \approx \frac{1}{20}",
                font_size = 300
            )

        self.play(Transform(f1, f2))
        self.wait(0.5)

