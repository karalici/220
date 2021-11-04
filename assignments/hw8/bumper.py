"""
Name: Iva Karalic
bumper.py

Problem: Program that does things like bumper cars.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from random import randint
import math
from time import sleep
from graphics import GraphWin, Circle, Point, color_rgb


def get_random(numbers):
    random = randint(-numbers, numbers)
    return random


def did_collide(circle1, circle2):
    radius1 = circle1.getRadius()
    radius2 = circle2.getRadius()
    center1 = circle1.getCenter()
    center2 = circle2.getCenter()
    dis = math.sqrt((center1.getX() - center2.getX()) ** 2 + (center1.getY() - center2.getY()) ** 2)
    return bool(dis <= radius1 + radius2)


def hit_vertical(circle1, window):
    center_point = circle1.getCenter()
    center_x = center_point.getX()
    radius = circle1.getRadius()
    return bool(center_x + radius >= window.getWidth() or center_x - radius <= 0)


def hit_horizontal(ball, win):
    center_point = ball.getCenter()
    center_point_y = center_point.getY()
    radius = ball.getRadius()
    return bool(center_point_y + radius >= win.getHeight() or center_point_y - radius <= 0)


def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return color_rgb(red, green, blue)


def main():

    def window():
        win = GraphWin("Bumper", 500, 500)
        circle1 = Circle(Point(250, 250), 25)
        circle2 = Circle(Point(150, 350), 25)

        circle1.draw(win)
        circle2.draw(win)

        circle1.setFill(get_random_color())
        circle1.setOutline("purple")
        circle2.setFill(get_random_color())
        circle2.setOutline("light blue")

        circle1x = get_random(10)
        circle1y = get_random(10)
        circle2x = get_random(10)
        circle2y = get_random(10)

        while win.checkMouse() is None:
            sleep(.01)
            circle1.move(circle1x, circle1y)
            circle2.move(circle2x, circle2y)
            if did_collide(circle1, circle2):
                circle1x = circle1x * -1
                circle1y = circle1y * -1
                circle2x = circle2x * -1
                circle2y = circle2y * -1
            if hit_horizontal(circle1, win):
                circle1y = circle1y * -1

            if hit_horizontal(circle2, win):
                circle2y = circle2y * -1

            if hit_vertical(circle1, win):
                circle1x = circle1x * -1

            if hit_vertical(circle2, win):
                circle2x = circle2x * -1

    window()


if __name__ == "__main__":
    main()
