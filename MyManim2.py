from manim import *

class CompoundInterestGrowth(Scene):
    def construct(self):
        # Настройка осей
        axes = Axes(
            x_range=[0, 6, 1],  # от 0 до 6 лет
            y_range=[0, 1400, 200],  # от 0 до 1400 долларов
            x_length=7,
            y_length=6,
            axis_config={"include_numbers": True},
            x_axis_config={"label_direction": DOWN},
            y_axis_config={"label_direction": LEFT}
        )

        # Метки осей
        x_label = axes.get_x_axis_label("Period (years)")
        y_label = axes.get_y_axis_label("Summ")

        self.play(Create(axes), Write(x_label), Write(y_label))

        # Параметры для расчета сложных процентов
        P = 1000  # начальная сумма
        r = 0.05  # годовая процентная ставка
        n = 12    # число периодов начисления процентов в год
        t_max = 5 # количество лет

        # Функция для расчета суммы со сложными процентами
        def compound_interest(t):
            return P * (1 + r / n) ** (n * t)
        
        # Создание графика роста
        graph = axes.plot(compound_interest, x_range=[0, t_max], color=BLUE)
        graph_label = axes.get_graph_label(graph, label="A(t) = 1000 \\left(1 + \\frac{0.05}{12}\\right)^{12t}", x_val=2.5, direction=UP / 2)
        
        self.play(Create(graph), Write(graph_label))
        
        # Анимация точек на графике для наглядности
        for i in range(t_max + 1):
            dot = Dot().move_to(axes.c2p(i, compound_interest(i)))
            self.play(FadeIn(dot), run_time=0.5)
            self.wait(0.5)
        
        # Показать значение в конечной точке
        final_value = compound_interest(t_max)
        final_value_text = MathTex(f"A(5) \\approx {final_value:.2f}", font_size=36)
        final_value_text.next_to(axes.c2p(t_max, final_value), RIGHT)
        self.play(Write(final_value_text))
        self.wait(2)
