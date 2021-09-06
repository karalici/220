"""
Name: Iva Karalic
convert.py

Problem: Convert degrees celsius to fahrenheit.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

# test values:
# 0c -> 32f
# 100c -> 212f
# main method/function
# identifiers
def main():
        celsius = eval(input("What temperature is it outside in celsius?: ")) # get the input in celsius
        fahrenheit = (9/5) * celsius + 32 # convert input to fahrenheit with the equation (9/5) * celsius + 32
        print("that's", fahrenheit, "degrees in fahrenheit! woohoo!") # print the temperature in fahrenheit


main()

