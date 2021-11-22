"""
Name: Iva Karalic
lab12.py
"""


from random import randint
from algorithms import read_data, is_in_linear


def find_and_remove(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Iva"
    except:
        pass
    return lst


def good_input():
    x = eval(input("Enter a number between 1 and 10: "))
    while x < 1 or x > 10:
        x = eval(input("Error! Input out of range \n Enter a number between 1 and 10: "))
    return x


def num_digits():
    x = eval(input("Enter a positive number: "))
    while x > 0:
        y = 0
        while x != 0:
            y += 1
            x //= 10
        print("Number of digits = ", y)
        x = eval(input("Enter a positive number: "))


def hi_lo_game():
    num = randint(1, 100)
    guesses = 1
    guess = eval(input("Guess a number between 1 and 100:"))
    while guesses < 7 and guess != num:
        if guess > num and guess != 6:
            guess = eval(input("Too high, Guess again. "))
        elif guess < num and guess != 6:
            guess = eval(input("Too low, Guess again. "))
        guesses += 1
    if guess == num:
        print("You win in", guesses, "guesses.")
    else:
        print("Sorry, you lose. The number was", num, ".")


def main():
    # add other function calls here
    lst = [1, 2, 3, 4, 5, 6]
    print(find_and_remove(lst, 4))
    print(read_data("num_file.txt"))
    print(is_in_linear(70, read_data("num_file.txt")))
    good_input()
    num_digits()
    hi_lo_game()
    pass


main()
