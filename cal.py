import math

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
    print("12. Exit")

    choice = input("Enter your choice (1-12): ")

    if choice == '12':
        print("Exiting calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4', '5', '7']:
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
        elif choice == '7':
            print("Result:", modulus(num1, num2))

    elif choice in ['6', '8', '9', '10', '11']:
        num = float(input("Enter number: "))

        if choice == '6':
            print("Result:", square_root(num))
        elif choice == '8':
            print("Result:", logarithm(num))
        elif choice == '9':
            print("Result:", sine(num))
        elif choice == '10':
            print("Result:", cosine(num))
        elif choice == '11':
            print("Result:", tangent(num))
    else:
        print("Invalid input. Please enter a number between 1 and 12.")
