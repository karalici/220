"""
Name: Iva Karalic
lab4.py
"""
import math

from graphics import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move rectangle")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        user_click = win.getMouse()
        # builds a circle
        shape = Rectangle(Point(user_click.x - 10, user_click.y - 10), Point(user_click.x + 10, user_click.y + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

        # create a space to instruct user
        inst_pt = Point(width / 2, 10)
        instructions = Text(inst_pt, "Click anywhere to close")
        instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    rec = Rectangle(p1, p2)
    rec.draw(win)

    length = abs(p2.getX() - p1.getX())
    width = abs(p2.getY() - p1.getY())
    area = length * width
    perimeter = 2 * (length + width)

    txt = Text(Point(50, 50), "Area: " + str(area))
    txt2 = Text(Point(100, 100), "Perimeter: " + str(perimeter))
    txt.draw(win)
    txt2.draw(win)

    inst_pt = Point(width / 0.5, 5)
    instructions = Text(inst_pt, "Click anywhere to close")
    instructions.draw(win)

    win.getMouse()
    win.close()

def circle():
    win = GraphWin("Lab 4", 400, 400)
    i = Point(110, 110)
    instructions = Text(i, "Click on the center of the circle ")
    instructions.draw(win)

    user_click = win.getMouse()
    instructions = Text(Point(150, 50), "Click on the outside of the circle ")
    instructions.draw(win)
    user_click2 = win.getMouse()
    x1 = user_click.getX()
    x2 = user_click2.getX()
    y1 = user_click.getY()
    y2 = user_click2.getY()
    r = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    txt = Text(Point(250, 250), "Radius: " + str(r))
    txt.draw(win)
    shape = Circle(user_click, r)
    shape.draw(win)

    ins = Text(Point(250, 150), "Click anywhere to close")
    ins.draw(win)
    win.getMouse()
    win.close()

def pi2():
    x = eval(input("how many terms do you want? "))
    acc = 0
    for i in range(x):
        num = 4
        denom = 1 + 2 * i
        fraction = (num / denom) * ((-1) ** i)
        acc += fraction
    print(acc)
    print(math.pi - acc)


def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
