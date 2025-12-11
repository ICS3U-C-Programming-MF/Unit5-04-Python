#!/usr/bin/env python3
# Created by Maximiliano Fairman
# Created on Dec 9th, 2025
# this asks for 3 parameters: an operation sign
# and two decimal numbers.
# It performs the operation on the two numbers.


def calculate(sign, first_number, second_number):
    if sign == "+":
        return first_number + second_number
    elif sign == "-":
        return first_number - second_number
    elif sign == "*":
        return first_number * second_number
    elif sign == "/":
        if second_number == 0:
            raise ValueError("Cannot divide by zero.")
        return first_number / second_number
    else:
        raise ValueError("Invalid operation sign.")


def main():
    print("=== Calculator ===")

    # Validate operation sign
    while True:
        sign = input("Enter operation (+, -, *, /): ").strip()
        if sign in ["+", "-", "*", "/"]:
            break
        print("Invalid operation. Please choose one of +, -, *, /.")

    # Validate first number
    while True:
        try:
            first_number = float(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a decimal number.")

    # Validate second number
    while True:
        try:
            second_number = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a decimal number.")

    # Call function
    try:
        result = calculate(sign, first_number, second_number)
        print("Result:", result)
    except ValueError as e:
        print("Error:", e)


# Run program
main()
