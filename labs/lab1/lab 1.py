"""
Name: Iva Karalic
lab1.py

Problem: This function calculates the area of rectangle
"""
def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)
calc_rec_area()
def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)
calc_volume()
def calc_shooting_percentage():
    shots = eval(input("Enter the shots made: "))
    total = eval(input("Enter the total shots made: "))
    shooting_percentage = shots / total * 100
    print("Shooting Percentage =", shooting_percentage)
calc_shooting_percentage()
def calc_coffee():
    per_pound = 10.50
    shipping = 0.86
    fixed = 1.50
    purchased = eval(input("Enter the number of pounds purchased: "))
    coffee = per_pound * shipping * purchased + fixed
    print("Coffee =", coffee)
calc_coffee()
def calc_kilometers():
    kilometers = eval(input("Enter the kilometers: "))
    miles = 0.62137
    kilometers = kilometers * miles
    print("Kilometers to miles =", kilometers)
calc_kilometers()



