import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Cannot divide zero."
    return x / y

def modulus(x, y):
    return x % y


def power(x, y):
    return x ** y


def square_root(x):
    if x < 0:
        return "Error! Cannot take square root of negative number."
    return math.sqrt(x)


while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Exit")

    choice = input("Enter your choice (1-7):")

    if choice == '7':
        print("Existing calculator. Goodbye!👋")
        break

    if choice in ['1', '2', '3', '4', '5', ]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
    elif choice == '6':
        num = float(input("Enter Number: "))
        print("Result:", square_root(num))
    else:
        print("Invalid input. Please enter a number between 1 and 5")
