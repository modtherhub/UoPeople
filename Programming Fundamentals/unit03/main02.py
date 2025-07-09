try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")