import math
import tkinter as tk
from tkinter import messagebox

# List to store history
history = []

# main app window
root = tk.Tk()
root.title("Calculator with History")

# StringVar for the display
expression = tk.StringVar()


# functions
def press(num):
    expression.set(expression.get() + str(num))


def clear():
    expression.set("")


def calculate():
    expr = expression.get()
    try:
        # Define allowed names (safe eval context)
        allowed_names = {
            'sin': lambda x: math.sin(math.radians(x)),
            'cos': lambda x: math.cos(math.radians(x)),
            'tan': lambda x: math.tan(math.radians(x)),
            'log': math.log10,
            'sqrt': math.sqrt,
            'abs': abs,
            'pow': pow
        }

        # Add math constants
        allowed_names['pi'] = math.pi
        allowed_names['e'] = math.e

        # Replace custom symbols with valid Python
        expr = expr.replace('√', 'sqrt')
        expr = expr.replace('^', '**')

        # 🧠 Auto-close unmatched parentheses
        open_parens = expr.count('(')
        close_parens = expr.count(')')
        if open_parens > close_parens:
            expr += ')' * (open_parens - close_parens)

        # Evaluate the expression safely
        result = eval(expr, {"__builtins__": {}}, allowed_names)

        history.append(f"{expression.get()} = {result}")
        expression.set(str(result))
        update_history()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input or calculation error:\n{e}")
        expression.set("")


def update_history():
    history_text.delete(1.0, tk.END)
    if history:
        history_text.insert(tk.END, "\n".join(history))
    else:
        history_text.insert(tk.END, "No history yet")


def clear_history():
    history.clear()
    update_history()


# Layout
entry = tk.Entry(root, textvariable=expression, font=("Arial", 20), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '^', '+',
    '√', 'log', 'sin', 'cos',
    'tan', 'C', '=', 'C H'
]


# Function to handle button click
def button_click(value):
    if value == 'C':
        clear()
    elif value == '=':
        calculate()
    elif value == 'C H':
        clear_history()
    else:
        # For math functions add parentheses automatically
        if value in ['√']:
            expression.set(expression.get() + 'sqrt(')
        elif value in ['log', 'sin', 'cos', 'tan']:
            expression.set(expression.get() + value + '(')
        else:
            press(value)


# Create buttons dynamically
row_val = 1
col_val = 0
for btn in buttons:
    action = lambda x=btn: button_click(x)
    b = tk.Button(root, text=btn, width=7, height=2, font=("Arial", 14), command=action)
    b.grid(row=row_val, column=col_val, padx=3, pady=3)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# History text box
history_label = tk.Label(root, text="History", font=("Arial", 14))
history_label.grid(row=row_val, column=0, columnspan=4)

history_text = tk.Text(root, height=10, width=35, font=("Arial", 12))
history_text.grid(row=row_val + 1, column=0, columnspan=4, padx=10, pady=5)

update_history()

root.mainloop()


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
