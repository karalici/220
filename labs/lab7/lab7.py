"""
Name: Iva Karalic
Partner: <your partner's name goes here – first and last>
<ProgramName>.py
"""

import math


def cash_conversion():
    integer = eval(input("Input an Integer: "))
    print("$"+"{:.2f}".format(integer))


def encode():
    x = input("Enter a word:")
    k = eval(input("What is the key:"))
    acc = ""
    for c in x:
        i = ord(c)
        add = i+k
        numbers = chr(add)
        acc += numbers
    print(acc)


def sphere_area(radius):
    area = 4 * (radius**2) * math.pi
    return area


def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius**3)
    return volume


def sum_n(n):
    total = 0
    for i in range(n+1):
        total += i
    return total


def sum_n_cubes(n):
    total = 0
    for i in range(n+1):
        total += i ** 3
    return total


def encode_better():
    x = input("What is the word:")
    k = input("What is the cipher key:")
    acc = ""
    for i in range(len(x)):
        c = ord(x[i])
        key = ord(k[i])
        new_word = c + key - 97
        acc += chr(new_word)
    print(acc)


def main():
    cash_conversion()
    encode()
    print(sphere_area(2))
    print(sphere_volume(5))
    print(sum_n(3))
    print(sum_n_cubes(3))
    encode_better()


main()
