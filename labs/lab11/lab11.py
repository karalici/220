"""
Name: Iva Karalic
lab11.py
"""

from random import randint


def getFile(file_name):
    file = open(file_name, "r")
    words = file.read()
    return words.split("\n")


def getWord(words):
    secret_word = words[randint(0, len(words)-1)]
    return secret_word


def guessedWord(secret_word, letters):
    guessed_word = ["_"] * len(secret_word)
    for letter in letters:
        for j in range(len(secret_word)):
            if secret_word[j] == letter:
                guessed_word[j] = letter
    return "".join(guessed_word)


def guessLetters(secret_word, guessed_word, guessed_letters):
    letters = input("Guess a letter: ")
    while letters in guessed_letters or ((len(letters) != 1) or not (ord(letters) >= 97 and ord(letters) <= 122)):
        print("This letter has already been guessed, try again:")
        letters = input("Guess a letter")
        letters = letters.lower()
    guessed_letters.append(letters)
    if guessedWord(secret_word, guessed_letters) != guessed_word:
        return (True, guessedWord(secret_word, guessed_letters))
    return (False, guessedWord(secret_word, guessed_letters))


def wordSpell(guessed_word, secret_word):
    if guessed_word == secret_word:
        return True
    else:
        return False


def printBoard(guess_word, turn_count, guessed_letters):
    print("----------------------------------------------")
    print("Guessed word: ", guess_word)
    print()
    print("Turn count:", turn_count)
    print("Guessed letters:", guessed_letters)
    print("----------------------------------------------")


def playGame():
    turn_count = 0
    guessed_letters = []
    secret_word = getWord(getFile("wordlist.txt"))
    guessed_word = "_" * len(secret_word)
    printBoard(guessed_word, turn_count, guessed_letters)
    while turn_count < 7 and not wordSpell(guessed_word, secret_word):
        guess = guessLetters(secret_word, guessed_word, guessed_letters)
        if guess[0] == False:
            turn_count += 1
        else:
            guessed_word = guess[1]
        printBoard(guessed_word, turn_count, guessed_letters)
    if turn_count >= 7:
        print("Game is over! You Lose!")
    elif wordSpell(guessed_word, secret_word):
        print("Congratulations, you won the game")


def main():
    # add other function calls here
    playGame()
    pass


main()
