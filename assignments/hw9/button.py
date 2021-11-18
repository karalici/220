"""
Name: Iva Karalic
button.py

Problem: Creates class button.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import Text


class Button:
    """
    creates button
    """
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        point1_x = self.shape.getP1().getX()
        point2_x = self.shape.getP2().getX()
        point_x = point.getX()

        point1_y = self.shape.getP1().getY()
        point2_y = self.shape.getP2().getY()
        point_y = point.getY()
        return bool(point1_x <= point_x <= point2_x and point1_y <= point_y <= point2_y)

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, new_label):
        self.text.setText(new_label)
