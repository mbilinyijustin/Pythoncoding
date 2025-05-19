import math
from unittest import result


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

while True:
    print("\n--- Scientific Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Modulus (x % y)")
    print("8. Logarithm (log base 10)")
    print("9. Sine (sin x)")
    print("10. Cosine (cos x)")
    print("11. Tangent (tan x)")
    print("12. View History")
    print("13. Exit")

    choice = input("Enter your choice (1-13): ")

    if choice == '13':
        print("Exiting calculator. Goodbye!")
        break
    elif choice == '12':
        print("\n--- Calculator History ---")
        if not history:
            print("No Calculation yet.")
        else:
            for item in history:
                print(item)

    if choice in ['1', '2', '3', '4', '5', '7']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
            history.append(f"{num1} + {num2} = {result}")
        elif choice == '2':
            print("Result:", subtract(num1, num2))
            history.append(f"{num1} - {num2} = {result}")
        elif choice == '3':
            print("Result:", multiply(num1, num2))
            history.append(f"{num1} * {num2} = {result}")
        elif choice == '4':
            print("Result:", divide(num1, num2))
            history.append(f"{num1} / {num2} = {result}")
        elif choice == '5':
            print("Result:", power(num1, num2))
            history.append(f"{num1} ^ {num2} = {result}")
        elif choice == '7':
            print("Result:", modulus(num1, num2))
            history.append(f"{num1} % {num2} = {result}")

    elif choice in ['6', '8', '9', '10', '11']:
        num = float(input("Enter number: "))

        if choice == '6':
            print("Result:", square_root(num))
            history.append(f"√{num} = {result}")
        elif choice == '8':
            print("Result:", logarithm(num))
            history.append(f"log({num}) = {result}")
        elif choice == '9':
            print("Result:", sine(num))
            history.append(f"sin({num}°) = {result}")
        elif choice == '10':
            print("Result:", cosine(num))
            history.append(f"cos({num}°) = {result}")
        elif choice == '11':
            print("Result:", tangent(num))
            history.append(f"tan({num}°) = {result}")
        print("Result:", result)
    else:
        print("Invalid input. Please enter a number between 1 and 12.")
