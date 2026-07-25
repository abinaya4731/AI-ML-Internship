#Q1: Create a function called hello().

def hello():
    print("Hello, World!")
hello()
    
#Q2: Create a function called welcome().
def welcome():
    print("Welcome to the program!")
welcome()   

#Q3: Create a function to add two numbers.
def add_numbers(a, b):
    return a + b
print(add_numbers(5, 3))

#Q4: Create a function to subtract two numbers.
def subtract_numbers(a, b):
    return a - b
print(subtract_numbers(10, 4))  

#Q5: Create a function to multiply two numbers.
def multiply_numbers(a, b):
    return a * b
print(multiply_numbers(6, 7))

#Q6: Create a function to divide two numbers.
def divide_numbers(a, b):
    return a / b
print(divide_numbers(20, 4))

#Q7: Create a function to find the square of a number.
def square_number(a):
    return a ** 2
print(square_number(5))

#Q8: Create a function to find the cube of a number.
def cube_number(a):
    return a ** 3
print(cube_number(3))

#Q9: Create a function to check if a number is even or odd.
def check_even_odd(a):
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(7))

#Q10: Create a function that prints "Hello, Your Name" using a parameter.
def print_hello_name(name):
    print("Hello, " + name + "!")
print_hello_name("Alice")
