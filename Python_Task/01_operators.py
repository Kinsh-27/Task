'''Write a program to perform addition, subtraction,
 multiplication, and division of two numbers provided by
 the user'''

def arithmetic_operations():
    print("Arithmetic Operations")

    # Taking input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Performing operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Division
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Undefined (division by zero is not allowed)"

    print(f"Addition of two numbers: {addition}")
    print(f"Subtraction of two numbers: {subtraction}")
    print(f"Multiplication of two numbers: {multiplication}")
    print(f"Division of two numbers: {division}")

arithmetic_operations()
