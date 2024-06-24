
import os
import shutil
from manim import *

shutil.rmtree(os.path.join('media'))
os.mkdir('media')


def make_mobs (mob_type) -> list:
    mobs = list()
    for x in np.nditer(mob_type):
        if x == 1: 
            mobs.append(SVGMobject("cucumber.svg"))
        else:
            mobs.append(SVGMobject("apple_red.svg"))
    return mobs 

def moveAlongPath(mobject_1, mobject_2, movingCameraScene):
    path = Line(mobject_1.get_center(), mobject_2.get_center(),stroke_opacity=0.5).set_opacity(0)
    path.points[1:3] += UP*2

    mobject_1.save_state()
    def update_rotate_move(mob,alpha):
        mobject_1.restore()
        mobject_1.move_to(path.point_from_proportion(alpha))
        mobject_1.rotate(2*PI*alpha)

    movingCameraScene.add(mobject_2,mobject_1,path)
    movingCameraScene.play(
            UpdateFromAlphaFunc(mobject_1,update_rotate_move),
            run_time=4
        )
    
    movingCameraScene.wait()

def placeInLine (mobs, rows, cols, x_step, y_step):
    for i, mob in enumerate(mobs):
        row = i // cols
        col = i % cols
        mob.move_to(np.array([col * x_step - (cols-1) * x_step / 2, 
                                -(row * y_step) + (rows-1) * y_step / 2, 0]))

class Permutations(MovingCameraScene):
    def construct(self):
        self.camera.background_color = GRAY

        # Создаем несколько объектов
        mob_type = np.array([1, 1, 0, 0, 0])
        mobs = make_mobs(mob_type)
        mobs_2 = make_mobs(mob_type)

        # Располагаем mobs по сетке вертикально
        placeInLine(mobs, 5, 1, 1.1, 2.1)
            
        # Располагаем mobs_2 по сетке горизонтально
        placeInLine(mobs_2, 1, 5, 1.1, 2.1)

        # Группируем вертикальные объекты
        grid = VGroup(*mobs).scale(0.5)
        # Группируем горизонтальные объекты
        grid_2 = VGroup(*mobs_2).next_to(grid.get_top(), UP)

        # Анимация появления объектов
        self.play(self.camera.frame.animate.move_to(grid).set(height = grid.height * 1.1))
        self.play(Create(grid))
        
        group = VGroup(grid, grid_2)

        # Определение масштаба камеры по ширине и высоте
        scale_width = self.camera.frame_width / group.width
        scale_height = self.camera.frame_height / group.height

        # Выбор наименьшего масштаба для гарантии, что все объекты попадут в кадр
        optimal_scale = max(scale_width, scale_height)

        # Установка ширины и высоты кадра камеры
        self.play(self.camera.frame.animate.set(width = group.width * optimal_scale * 1.4))
        self.play(self.camera.frame.animate.move_to(group))

        for i, mob_1 in enumerate(mobs):
            self.play(Transform(mobs[i], mobs_2[i]))

        new_position = (self.camera.frame.get_top() - grid_2.get_top()) * UP

        self.remove(grid)
        self.play(grid_2.animate.move_to(new_position))

        # moveAlongPath(grid_2[0], grid_2[4], self)
        self.wait(0.2)