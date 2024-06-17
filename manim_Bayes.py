# self.add(index_labels(matex_2_3[0]))

import os
import shutil
from manim import *

# shutil.rmtree('media')
# os.mkdir('media')
shutil.rmtree(os.path.join('media'))
os.mkdir('media')

# Вероятность, что ты закроешь ютуб на i-том шортсе определяется по формуле на видео
# какова вероятность, что ты просмотришь 10 шортсов и закроешь Youtube?
# первая мысль - это просто подставить 10 в формулу
# но это неправильно
# потому что в первую очередь необходимо хотя бы досмотреть до 10 видео и не закрыть youtube раньше
# Вероятность, что ты не закроешь youtube на i-ом видео будет равна 1 - p
# А вероятность, что youtube не будет закрыт до 10 видео равна 
# То есть надо не закрыть в первые девять видео, но закрыть на десятом, что в итоге будет равно 

# Не забудь подписаться, 

class ChangeOpacity(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        super().__init__(number, **kwargs)
        self.start = start
        self.end = end
   
    def interpolate_mobject(self, alpha: float) -> None:
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)

#================================================================================================
#================================================================================ PossibilityTask
class PossibilityTask(MovingCameraScene):
  def construct(self):

        self.camera.background_color = DARKER_GRAY
        f1 = MathTex(
                r" P = \frac{1}{1+i}",
                font_size = 300
            )

        f1_1 = Tex(
                r" P - вероятность закрытия Youtube",
                font_size = 150
            ).move_to(f1, DOWN)

        f1_2 = Tex(
                r" i - номер видео",
                font_size = 150
            ).move_to(f1_1, DOWN)
        
        f3 = MathTex(
                10,
                font_size = 300
            )
        
        a_1 = Line(f1.get_bottom() + f1.get_left(), f1.get_top() + f1.get_right(), stroke_width = 15).set_opacity(0.0).set_color(RED)
        a_2 = Line(f1.get_top() + f1.get_left(), f1.get_bottom() + f1.get_right(), stroke_width = 15).set_opacity(0.0).set_color(RED)
        self.wait(2)
        
        g = VGroup(f1, f1_1, f1_2, f3, a_1, a_2).scale(0.5).arrange(direction = DOWN * 2)
        f3.move_to(f1[0][6].get_center()).set_opacity(0.0)
        a_1.move_to(f1.get_center())
        a_2.move_to(f1.get_center())
        self.add(f3)

        self.add(a_1, a_2)

        self.play(Create(f1))
        self.wait(0.2)
        # self.add(index_labels(f1[0]))

        f1[0][0].set_color(YELLOW)
        f1_1[0][0].set_color(YELLOW)
        self.play(TransformFromCopy(f1[0][0], f1_1))
        self.wait(0.2)

        f1[0][6].set_color(RED)
        f1_2[0][0].set_color(RED)
        self.play(TransformFromCopy(f1[0][6], f1_2))
        self.wait(0.2)
        
        f2 = Tex(
                r"P(i = 10) \text{ --- } ?",
                font_size = 250
            ).next_to(g, DOWN * 80)
        
        boundary = AnimatedBoundary(f2[0][0], colors = [RED, GREEN],
                                    cycle_rate = 1)

        self.add(f2, boundary)
        self.wait(2)

        self.play(self.camera.frame.animate.move_to(f2[0]).set(width=f2.width*1.1))
        self.wait(0.5)

        self.play(self.camera.frame.animate.move_to(g).set(width=g.width*1.1))
        self.wait(0.5)

        self.play(FadeOut(f1[0][6]))
        self.wait(0.5)
        f3.set_color(RED).set_opacity(1)
        self.wait(0.5)

        surraundingRectangle = SurroundingRectangle(mobject = f3, color = RED, buff = 0.1, corner_radius=0.2)
        self.play(ShowCreationThenFadeOut(surraundingRectangle), run_time = 3)
        self.wait(2)

        self.play(a_1.animate.set_opacity(1.0), run_time = 0.1)
        self.play(a_2.animate.set_opacity(1.0), run_time = 0.1)
        self.wait(2)


        self.camera.background_color = DARKER_GRAY
        f1 = MathTex(
                r" P = \frac{1}{1+i}",
                font_size = 300
            )

#================================================================================ PossibilityTask
#================================================================================================
#================================================================================================
#================================================================================ Negative_Pos_9
class Negative_Pos_9(MovingCameraScene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY

        g_max = 7
        g_counter = 0

        # Формирование
        g = VGroup().scale(0.5)
        for i in range(0, g_max - 3):
            if i == 0:
                g.add(MathTex(r"P'(9) = ",font_size = 200))
            elif i == 1:
                g.add(MathTex(r"\left(1 - \frac{1}{1+1}\right)",font_size = 200))
            elif i == 2:
                g.add(MathTex(r"\times \left(1 - \frac{1}{1+2}\right)",font_size = 200))
            elif i == 3:
                g.add(MathTex(r"\times \left(1 - \frac{1}{1+3}\right)\times",font_size = 200))
                
            g_counter += 1

        g.add( MathTex(r" \quad \cdots \quad", font_size = 200))
        g_counter += 1

        g.add( MathTex(r"\times \left(1 - \frac{1}{1+9}\right)",font_size = 200))
        g_counter += 1

        g.add( MathTex(r" = \displaystyle\prod_{i=1}^{9} \left(1 - \frac{1}{1+i}\right)",font_size = 200))
        g_counter += 1

        g.arrange(RIGHT, buff = 1)

        # Вывод
        for i in range(0, g_max - 3):
            self.play(self.camera.frame.animate.move_to(g[i]).set(width=g[1].width * 3.5))
            self.play(Create(g[i]))

            if i != 0:
                self.add(Integer(number = i).set_color(ORANGE).scale(2.5).next_to(g[i], UP * 2))
                self.wait(0.1)
                print(g_counter)

            g_counter -= 1

        self.play(self.camera.frame.animate.move_to(g[g_max - g_counter]).set(width=g[1].width * 3.5))
        self.play(Create(g[g_max - g_counter]))
        self.wait(0.1)

        g_counter -= 1

        self.play(self.camera.frame.animate.move_to(g[g_max - g_counter]).set(width=g[1].width * 3.5))
        self.play(Create(g[g_max - g_counter]))
        self.add(Integer(9).set_color(ORANGE).scale(2.5).next_to(g[g_max - g_counter], UP * 2))
        self.wait(0.1)

        g_counter -= 1

        self.play(self.camera.frame.animate.move_to(g[g_max - g_counter]).set(width=g[1].width * 3.5))
        self.play(Create(g[g_max - g_counter]))
        self.wait(0.1)

        g_counter -= 1
#================================================================================ Negative_Pos_9
#================================================================================================
#================================================================================================
#======================================================================================== Summary
class Summary(MovingCameraScene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY

        f1 = MathTex(
                r" P(10) = \displaystyle\prod_{i=1}^{9} \left(1 - \frac{1}{1+i}\right)\times \left(\frac{1}{1+10}\right)",
                font_size = 300
            )

        self.play(self.camera.frame.animate.move_to(f1[0][0:4]).set(width=f1[0][0:4].width * 2.5))
        
        self.play(Create(f1))
        # self.add(index_labels(f1[0]))
        self.wait(1)
        self.play(self.camera.frame.animate.move_to(f1[0][21:28]).set(width=f1[0][21:28].width * 2.5), run_time = 3)

        self.play(self.camera.frame.animate.move_to(f1).set(width=f1.width * 1.1), run_time = 3)

        f2 = MathTex(
                r" P(10) \approx 1 \%",
                font_size = 300
            )
        
        self.play(Transform(f1, f2))

        self.play(self.camera.frame.animate.move_to(f2).set(width=f2.width * 1.1), run_time = 3)

#======================================================================================== Summary
#================================================================================================


class TransformFromCopyAnimationEffect(Scene):
  def construct(self):
        circle=Circle()      
        self.play(circle.animate.set_fill(opacity = 1.0))
        self.wait()

        square = Square()
        self.play(TransformFromCopy(circle, square), run_time=2)
        self.wait()

class Help1(Scene):
    def construct(self):
        f1=MathTex(
            r"\frac{d}{dx}f(x) =\lim_{h\to 0}{f(x+h)-f(x) \over ",
            r"(x+h)-(x)",
            "}" 
            )
        f2=MathTex(
            r"\frac{d}{dx}f(x)\quad =\quad\lim_{h\to 0}{f(x+h)\quad-\quad f(x) \over ",
            "h",
            "}"
            )
        self.add(f1)
        self.play(ReplacementTransform(f1[1],f2[1]))
        self.wait()

class Help1(Scene):
    def construct(self):
        f1=MathTex(
            r"\displaystyle\prod_{i=1}^{9} \left(1 - \frac{1}{1+i}\right)"
            )
        self.add(f1)
        self.wait()


# ============================================================================
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class MotivationMem(MovingCameraScene):
    def construct(self):
        # Исходные выражения
        math_mem_0 = MathTex(
            r" 0.99^{365}&\approx 0.03 \\",
            r" 1.01^{365}&\approx 38",
            font_size = 200
        )

        self.play(Create(math_mem_0))
        self.wait(0.2)

        # Исходное выражение 1
        math_mem_0_0 = MathTex(
            r" 0.99^{365} &\approx 0.03",
            font_size = 200
        )

        self.play(math_mem_0.animate.shift(UP * 6))
        self.wait(0.2)

        # 365 в рамку
        # self.add(index_labels(math_mem_0[0]))
        surraundingRectangle = SurroundingRectangle(mobject = math_mem_0[0][0:12], color = YELLOW, buff = 0.15, corner_radius=0.2)
        self.play(ShowCreationThenFadeOut(surraundingRectangle), run_time = 1)
        self.wait(0.2)

        # оставить только одно уравнение
            # сдвинуть к центру
        self.play(FadeOut(math_mem_0[1]))
        self.remove(math_mem_0[1])

        self.wait(0.2)

        self.play(self.camera.frame.animate.move_to(math_mem_0[0]).set(width=math_mem_0_0.width*1.5))
        self.wait(0.3)

        # 365 в рамку
        math_mem_0[0][4:7].set_color(YELLOW)
        surraundingRectangle = SurroundingRectangle(mobject = math_mem_0[0][4:7], color = YELLOW, buff = 0.1, corner_radius=0.2)
        self.play(ShowCreationThenFadeOut(surraundingRectangle), run_time = 1)
        self.wait(0.2)

        # Год
        text_365 = Text("Год", font_size = 200, font = "Bradley Hand").next_to(math_mem_0[0][4:7], UP * 8)
        self.play(Create(text_365), run_time=0.5)
        self.wait(0.2)

        # Стрелка на 365
        a_365 = Arrow(text_365.get_bottom(), math_mem_0[0][4:7].get_top())
        self.play(Create(a_365), run_time=0.5)
        self.wait(0.2)

        self.play(FadeOut(a_365, text_365))
        self.wait(0.2)
        # ============================================= 1
        g_max = 6
        g_counter = 0

        # Формирование
        g = VGroup().scale(0.5)
        for i in range(0, g_max - 2):
            if i == 0:
                g.add(MathTex(r"0.99^{365} = ",font_size = 200))
            elif i == 1:
                g.add(MathTex(r"0.99",font_size = 200))
            else:
                g.add(MathTex(r" \times 0.99",font_size = 200))
                
            g_counter += 1
            # if i == 0:
            #     g.add( MathTex(r"1",font_size = 200))
            # else:
            #     g.add( MathTex(r" \times 0.99",font_size = 200))
            #     g_counter += 1

        g.add( MathTex(r" \quad \cdots \quad", font_size = 200))
        g_counter += 1

        g.add( MathTex(r" \times 0.99",font_size = 200))
        g_counter += 1

        g.arrange(RIGHT, buff = 1)
        g.move_to(DOWN * 15)

        # Вывод

        for i in range(0, g_max - 2):
            self.play(self.camera.frame.animate.move_to(g[i]).set(width=g[1].width * 3.5))
            self.play(Create(g[i]))

            if i != 0:
                self.add(Integer(number = i).set_color(ORANGE).scale(2.5).next_to(g[i], UP * 2))
                self.wait(0.1)
                print(g_counter)

            g_counter -= 1

        self.play(self.camera.frame.animate.move_to(g[g_max - g_counter]).set(width=g[1].width * 3.5))
        self.play(Create(g[g_max - g_counter]))
        self.wait(0.1)

        g_counter -= 1

        self.play(self.camera.frame.animate.move_to(g[g_max - g_counter]).set(width=g[1].width * 3.5))
        self.play(Create(g[g_max - g_counter]))
        self.add(Integer(365).set_color(ORANGE).scale(2.5).next_to(g[g_max - g_counter], UP * 2))
        self.wait(0.1)

        g_counter -= 1
        # ======================= 1

        self.play(self.camera.frame.animate.move_to(math_mem_0[0]).set(width=math_mem_0_0.width*1.5))
        self.wait(0.3)

        # добавить единицу
        math_mem_3 = MathTex(
            r" 1 \times 0.99^{365}&\approx0.03 \\",
            r" 1.01^{365} &\approx 38",
            font_size = 200
        )
        math_mem_3[0][0:2].set_color(YELLOW)
        math_mem_3[0].move_to(math_mem_0[0])

        self.play(ReplacementTransform(math_mem_0[0], math_mem_3[0]))

        # self.play(ReplacementTransform(math_mem_0_0, math_mem_3))
        # self.wait(0.2)

        # # arrows = [Arrow(2 * DR, 2 * UL), Arrow(2 * DR, 2 * UL)]
        # # VGroup(*arrows).set_x(0).arrange(buff=2)
        # # self.play(GrowArrow(arrows[0]))
        # # self.wait(0.2)

        # Ты сегодня
        text_you = Text("Ты сегодня", font_size = 200, font = "Bradley Hand").move_to(UP * 2)
        self.play(Create(text_you), run_time=0.5)
        self.wait(0.2)

        # Стрелка
        a_1 = Arrow(text_you.get_center() + UL * 1, math_mem_3[0][0:2].get_center() + DR * 1)
        self.play(Create(a_1), run_time=0.5)
        self.wait(0.2)

        # "1 *" в рамку
        framebox_1 = SurroundingRectangle(mobject = math_mem_3[0][0:2], color = YELLOW, buff = 0.15, corner_radius=0.2)
        self.play(ShowCreationThenFadeOut(framebox_1), run_time = 2)
        self.wait(0.2)

        self.play(FadeOut(a_1, text_you))

        g = VGroup().scale(0.5).arrange(direction = RIGHT).next_to(math_mem_3,UP * 5).arrange(direction = RIGHT)
        for i in range(1, 3):
            g += MathTex(
                r" \times 0.99",
                font_size = 100
            )
        self.wait(0.2)

        # Умножить на ОТ

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


class My_test(MovingCameraScene):
    def construct(self):
        g_max = 6
        g_counter = 0

        # Формирование
        g = VGroup().scale(0.5)
        for i in range(0, g_max - 2):
            if i == 0:
                g.add(MathTex(r"0.99^{365} = ",font_size = 200))
            elif i == 1:
                g.add(MathTex(r"0.99",font_size = 200))
            else:
                g.add(MathTex(r" \times 0.99",font_size = 200))
                
            g_counter += 1
            # if i == 0:
            #     g.add( MathTex(r"1",font_size = 200))
            # else:
            #     g.add( MathTex(r" \times 0.99",font_size = 200))
            #     g_counter += 1

        g.add( MathTex(r" \quad \cdots \quad", font_size = 200))
        g_counter += 1

        g.add( MathTex(r" \times 0.99",font_size = 200))
        g_counter += 1

        g.arrange(RIGHT, buff = 1)

        # Вывод
        for i in range(0, g_max - 2):
            self.play(self.camera.frame.animate.move_to(g[i]).set(width=g[1].width * 3.5))
            self.play(Create(g[i]))

            if i != 0:
                self.add(Integer(number = i).set_color(ORANGE).scale(2.5).next_to(g[i], UP * 2))
                self.wait(0.1)
                print(g_counter)

            g_counter -= 1

        self.play(self.camera.frame.animate.move_to(g[g_max - g_counter]).set(width=g[1].width * 3.5))
        self.play(Create(g[g_max - g_counter]))
        self.wait(0.1)

        g_counter -= 1

        self.play(self.camera.frame.animate.move_to(g[g_max - g_counter]).set(width=g[1].width * 3.5))
        self.play(Create(g[g_max - g_counter]))
        self.add(Integer(365).set_color(ORANGE).scale(2.5).next_to(g[g_max - g_counter], UP * 2))
        self.wait(0.1)

        g_counter -= 1


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
        self.play(Create(framebox1))
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
