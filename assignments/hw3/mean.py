"""
Name: Iva Karalic
mean.py

Problem: This calculates RMS, Harmonic, and Geometric averages

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
# The program will calculate and display the RMS mean, the harmonic mean
# and the geometric mean with values that the user enters.
# The input will be the numbers entered by the user.
# The output will be the calculated RMS, harmonic and geometric means.
# 1. Ask the user for the input.
# 2. Loop the inputs
# 3. Compute the RMS, harmonic and geometric means.
# 4. Print and round the answers

import math

def main():
    # Ask user for input
    values = eval(input("Enter the # of values: "))

    # Set accumulators
    acc = 0
    acc2 = 0
    acc3 = 1

    # Ask the user to enter the value
    for i in range(values):
        amount = eval(input("Enter the value: "))
    # RMS Average
    acc = acc + amount ** 2
    # Harmonic Mean
    acc2 = acc2 + 1 / amount
    # Geometric mean
    acc3 = acc3 * amount

    # compute
    mean = acc / amount
    rms_average = math.sqrt(mean)
    harmonic_mean = values / acc2
    geometric_mean = acc3 ** (1 / values)

    # print and round
    print(round(rms_average, 3))
    print(round(harmonic_mean, 3))
    print(round(geometric_mean, 3))

if __name__ == "__main__":
    main()