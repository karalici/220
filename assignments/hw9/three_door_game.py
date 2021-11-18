"""
Name: Iva Karalic
three_door_game.py

Problem: Creates a three door game

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint
from graphics import GraphWin, Rectangle, Point, Text
from button import Button


def main():
    win = GraphWin("Three Button Game", 400, 400)
    win.setCoords(0, 0, 10, 10)

    rectangle1 = Rectangle(Point(1, 4), Point(3, 6))
    door1 = Button(rectangle1, "Door 1")
    door1.draw(win)

    rectangle2 = Rectangle(Point(4, 4), Point(6, 6))
    door2 = Button(rectangle2, "Door 2")
    door2.draw(win)

    rectangle3 = Rectangle(Point(7, 4), Point(9, 6))
    door3 = Button(rectangle3, "Door 3")
    door3.draw(win)

    instruction = Text(Point(5, 2), "Click to choose my door!")
    instruction.setSize(15)
    instruction.draw(win)

    rand = randint(0, 2)
    list_0 = [door1, door2, door3]
    list_1 = ["Door 1", "Door 2", "Door 3"]
    random_door_str = list_1[rand]

    door_clicked = win.getMouse()
    print(door_clicked)

    if list_0[rand].is_clicked(door_clicked):
        text_won = Text(Point(5, 9), "You Win!")
        text_won.draw(win)
        list_0[rand].color_button("green")
        instruction.setText("Click to close!")
    else:
        lost_text = Text(Point(5, 9), "You lost")
        lost_text.draw(win)
        instruction.setText("{0}".format(random_door_str) + " is my secret door! \n \n"
                                                            "Click to close!")

        if door1.is_clicked(door_clicked):
            door1.color_button("red")
        elif door2.is_clicked(door_clicked):
            door2.color_button("red")
        elif door3.is_clicked(door_clicked):
            door3.color_button("red")

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
