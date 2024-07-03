import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Square root of negative number."
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative number."
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def arcsin(x):
    return math.degrees(math.asin(x))

def arccos(x):
    return math.degrees(math.acos(x))

def arctan(x):
    return math.degrees(math.atan(x))

def sinh(x):
    return math.sinh(x)

def cosh(x):
    return math.cosh(x)

def tanh(x):
    return math.tanh(x)

def log10(x):
    return math.log10(x)

def ln(x):
    return math.log(x)

def main():
    print("Welcome to the Python Scientific Calculator!")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (x^y)")
    print("6. Square Root (√x)")
    print("7. Factorial (x!)")
    print("8. Sin (sin x)")
    print("9. Cos (cos x)")
    print("10. Tan (tan x)")
    print("11. Sinh (sinh x)")
    print("12. Cosh (cosh x)")
    print("13. Tanh (tanh x)")
    print("14. Logarithm (log10 x)")
    print("15. Natural Logarithm (ln x)")
    print("16. Exit")

    while True:
        choice = input("Enter your choice (1-16): ")

        if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
                      '11', '12', '13', '14', '15', '16'):
            if choice == '16':
                print("Thank you for using the calculator. Goodbye!")
                break

            if choice in ('3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'):
                x = float(input("Enter the number: "))
                if choice == '6':
                    print(f"Square root of {x} is {square_root(x)}")
                elif choice == '7':
                    print(f"Factorial of {x} is {factorial(int(x))}")
                elif choice == '8':
                    print(f"sin({x}) = {sin(x)}")
                elif choice == '9':
                    print(f"cos({x}) = {cos(x)}")
                elif choice == '10':
                    print(f"tan({x}) = {tan(x)}")
                elif choice == '11':
                    print(f"sinh({x}) = {sinh(x)}")
                elif choice == '12':
                    print(f"cosh({x}) = {cosh(x)}")
                elif choice == '13':
                    print(f"tanh({x}) = {tanh(x)}")
                elif choice == '14':
                    print(f"log10({x}) = {log10(x)}")
                elif choice == '15':
                    print(f"ln({x}) = {ln(x)}")

            else:
                x = float(input("Enter the first number: "))
                y = float(input("Enter the second number: "))

                if choice == '1':
                    print(f"{x} + {y} = {add(x, y)}")
                elif choice == '2':
                    print(f"{x} - {y} = {subtract(x, y)}")
                elif choice == '3':
                    print(f"{x} * {y} = {multiply(x, y)}")
                elif choice == '4':
                    if y == 0:
                        print("Error! Division by zero.")
                    else:
                        print(f"{x} / {y} = {divide(x, y)}")
                elif choice == '5':
                    print(f"{x} ^ {y} = {exponentiate(x, y)}")
        else:
            print("Invalid input. Please enter a valid number (1-16).")

if __name__ == "__main__":
    main()
