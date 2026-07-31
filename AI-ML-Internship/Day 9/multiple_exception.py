try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ValueError:
    print("Please enter only numbers.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")