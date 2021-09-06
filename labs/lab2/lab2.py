"""
Name: Iva Karalic
lab2.py

"""
def sum_of_threes():
    a = eval(input("Enter the max: "))
    acc = 0
    for x in range(0, a + 1, 3):
        acc = acc + x
    print(acc)

def multiplication_table():
    for h in range(1,11):
        for l in range(1, 11):
            print(h*l, end=" ")
        print()

def triangle_area():
    import math
    a = eval(input("Enter the value a: "))
    b = eval(input("Enter the value b: "))
    c = eval(input("Enter the value c: "))
    s = (a + b + c) / 2
    x = s * (s - a)(s - b)(s - c)
    A = math.sqrt(x)
    print(A)


def sumSquares():
    start = eval(input("Enter the start amount: "))
    end = eval(input("Enter the end amount: "))
    acc = 0
    for x in range(start, end + 1):
        acc = acc + x**2
    print(acc)


def power():
    base = eval(input("Enter the base number: "))
    exponent = eval(input("Enter the exponent number: "))
    acc = 1
    for x in range(exponent):
        acc = acc * base
    print(acc)
