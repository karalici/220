"""
Name: Iva Karalic
vigenere.py

Problem: Implement the Vigenere cipher.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import GraphWin, Point, Rectangle, Entry, Text


def code(message, keyword):
    # change encode to say the message

    message_1 = message.replace(" ", "")
    message_2 = message_1.upper()

    keyword_1 = keyword.upper()
    acc = ""
    for i in range(len(message_2)):
        c = ord(message_2[i])
        key = ord(keyword_1[i % len(keyword_1)])
        new_number = (c + key) % 26
        new_word = str(chr(ord("A") + new_number))
        acc += new_word
    return acc


def main():
    # draw box and bones of the code
    win = GraphWin("Vigenere", 400, 400)
    win.setCoords(0, 0, 10, 10)

    message_point = Point(1.5, 8)
    message = Text(message_point, "Message to code: ")
    message.draw(win)

    message_text_input = Entry(Point(5, 8), 10)
    message_text_input.draw(win)

    keyword_point = Point(1.5, 4)
    message_text = Text(keyword_point, "Keyword:")
    message_text.draw(win)

    # Text box for keyword
    keyword_input = Entry(Point(5, 4), 10)
    keyword_input.draw(win)

    r = Rectangle(Point(4, 3), Point(6, 2))
    r.draw(win)

    encode = Text(Point(4.5, 2.5), "Encode")
    encode.draw(win)
    win.getMouse()
    message = message_text_input.getText()
    keyword = keyword_input.getText()

    code(message, keyword)

    exit_1 = Text(Point(1.5, 1), "Click anywhere to close")
    exit_1.draw(win)
    win.getMouse()
    win.close()


main()

if __name__ == "__main__":
    main()
