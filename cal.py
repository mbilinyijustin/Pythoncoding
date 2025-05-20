import math
import tkinter as tk


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y


def power(x, y):
    return x ** y


def square_root(x):
    if x < 0:
        return "Error! Cannot take square root of negative number."
    return math.sqrt(x)


def modulus(x, y):
    return x % y


def logarithm(x):
    if x <= 0:
        return "Error! Logarithm undefined for zero or negative numbers."
    return math.log10(x)


def sine(x):
    return math.sin(math.radians(x))


def cosine(x):
    return math.cos(math.radians(x))


def tangent(x):
    return math.tan(math.radians(x))


# List to store history
history = []

# Main loop
while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Logarithm (base 10)")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. View History")
    print("13. Clear History")
    print("14. Exit")

    choice = input("Enter your choice (1–14): ")

    result = None  # reset for each loop
    if choice in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            result = add(num1, num2)
            history.append(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            history.append(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            history.append(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            history.append(f"{num1} / {num2} = {result}")
        elif choice == '5':
            result = modulus(num1, num2)
            history.append(f"{num1} % {num2} = {result}")
        elif choice == '6':
            result = power(num1, num2)
            history.append(f"{num1} ^ {num2} = {result}")

    elif choice == '7':
        num = float(input("Enter number: "))
        result = square_root(num)
        history.append(f"√{num} = {result}")

    elif choice == '8':
        num = float(input("Enter number: "))
        result = logarithm(num)
        history.append(f"log10({num}) = {result}")

    elif choice in ['9', '10', '11']:
        angle = float(input("Enter angle in degrees: "))
        if choice == '9':
            result = sine(angle)
            history.append(f"sin({angle}) = {result}")
        elif choice == '10':
            result = cosine(angle)
            history.append(f"cos({angle}) = {result}")
        elif choice == '11':
            result = tangent(angle)
            history.append(f"tan({angle}) = {result}")

    elif choice == '12':
        print("\n--- Calculator History ---")
        if not history:
            print("No history yet.")
        else:
            for item in history:
                print(item)

    elif choice == '13':
        history.clear()
        print("History cleared.")

    elif choice == '14':
        print("Exiting calculator. Goodbye!")
        break

    else:
        print("Invalid input. Please enter a number between 1 and 14.")

    if result is not None:
        print("Result:", result)
