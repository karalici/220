"""
Name: Iva Karalic
interest.py

Problem: This calculates the interest rate

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def main():
    annual_interest_rate = eval(input("Enter the annual interest rate: "))
    number_of_days_in_a_billing_cycle = eval(input("Enter the number of days in a billing cycle: "))
    net_balance_shown = eval(input("Enter the net balance shown: "))
    payment_amount = eval(input("Enter the payment amount: "))
    day_the_payment_was_made = eval(input("Enter the day of the billing cycle when the payment was made: "))
    step1 = net_balance_shown * number_of_days_in_a_billing_cycle
    step2 = payment_amount * (number_of_days_in_a_billing_cycle - day_the_payment_was_made)
    step3 = step1 - step2
    step4 = step3 / number_of_days_in_a_billing_cycle
    monthly_interest_rate = (annual_interest_rate / 12) / 100
    answer = monthly_interest_rate * step4
    rounded = round(answer, 2)
    print(rounded)


if __name__ == "__main__":
    main()