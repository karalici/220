"""
Name: Iva Karalic
greeting.py

Problem: Draw a heart with a moving arrow.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from math import sqrt
from time import sleep
from graphics import GraphWin, Circle, Polygon, Point, Text


def main():

    win = GraphWin("Valentines Card", 500, 500)
    # draw two circle
    circle1 = Circle(Point(170, 150), 75)
    circle2 = Circle(Point(320, 150), 75)
    circle1.setFill("pink")
    circle2.setFill("pink")
    circle1.setOutline("pink")
    circle2.setOutline("pink")
    circle1.draw(win)
    circle2.draw(win)
    middle = Circle(Point(250, 200), 60)
    middle.setFill("pink")
    middle.setOutline("pink")
    middle.draw(win)
    # draw a triangle
    triangle = Polygon(Point(170 - 75 * sqrt(2) / 2, 150 + 75 * sqrt(2) / 2),
                  Point(245, 350),
                  Point(320 + 75 * sqrt(2) / 2, 150 + 75 * sqrt(2) / 2))
    triangle.setFill("pink")
    triangle.setOutline("pink")
    triangle.draw(win)
    valentine_text = Text(Point(250, 200), "Happy Valentines Day!")
    valentine_text.draw(win)

    # draw arrow
    # make the arrow move
    arrow_triangle = Polygon(Point(450, 450), Point(450, 470), Point(470, 450))
    arrow_triangle.setFill("black")
    arrow_triangle.draw(win)
    rectangle_draw = Polygon(Point(455, 465), Point(465, 455), Point(500, 485), Point(485, 500))
    rectangle_draw.setFill("black")
    rectangle_draw.draw(win)

    for num in range(100):
        sleep(0.1)
        rectangle_draw.move(-5, -5)
        arrow_triangle.move(-5, -5)
    # click on the window to close
    close_text = Text(Point(250, 450), "Click anywhere to close")
    close_text.draw(win)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
