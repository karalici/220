"""
Name: Iva Karalic
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("Enter your name in first last order: ")
    first = name.split()
    print(first[1] + "," + first[0])


def company_name():
    website = input("Enter the website in a three-part internet domain name: ")
    name = website.split(".")
    print(name[1])


def initials():
    students = eval(input("Enter the number of students: "))
    for i in range(students):
        user_input = input("Enter the first name of student " + str(i + 1) + ":")
        last_name = input("Enter " + str(user_input) + "'s last name: ")
        print(str(user_input + "'s initials are " + user_input[0] + last_name[0] + "."))


def names():
    full_names = input("Enter people's names, separated by commas:")
    seperate_names = full_names.split(",")
    print("The Initials are ", end=" ")
    for i in seperate_names:
        name = i.split()
        print(name[0][0] + name[1][0], end=" ")


def thirds():
    number_of_sentences = eval(input("Enter the number of sentences: "))
    for i in range(number_of_sentences):
        sentences = input("What are the sentences? ")
        s = len(sentences)
        for x in range(2, s + 1, 3):
            print(sentences[x], end=" ")


def word_average():
    sentences = input("What is the sentence? ")
    strip = sentences.replace(" ", "")
    l = len(strip)

    word = sentences.split()
    length = len(word)
    print(l / length)


def pig_latin():
    sentences = input("What is the sentence? ")
    s = sentences.split()
    for i in s:
        print(i[1:] + i[0] + "ay", end=" ")


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()


main()
