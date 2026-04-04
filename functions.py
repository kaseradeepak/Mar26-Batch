# Function - set of instructions that performs a particular operation.
# Functions introduces reusability and abstraction.

# DRY Principle - Don't Repeat Yourself
# abstraction - hiding unnecessary details from the client.
# functions helps us to make our code modular.

# Functions - Subroutines (Long Back ~1960-70)

# functions - define once and reuse many times.

# function definition
def say_hello():
    print("Hello World")

def say_bye():
    print("Bye World")

def say_hi():
    print("Hi Everyone")

# say_hello() # function calling.

# def : defines a function
# function name
# parentheses.
# parameters
# colon - Start of the function unit.

def show_header():
    print("=" * 20)
    print("Welcome to Masai Class.")
    print("=" * 20)

def show_content():
    print("This is the class on Python functions.")

def show_footer():
    print("=" * 20)
    print("Thans for attending the class.")
    print("=" * 20)

def show_entire_content():
    show_header()
    show_content()
    show_footer()

# A function can call other functions too.

# Function Parameters - Input to the functions.
# function parameters introduces flexibility and generalization to the functions, they transforms the function from a single-purpose tool into versatile and more resuable component that works for different types of input.

# Function Parameters solves the rigidity problem: 
# function without parameters can only do one specific thing with hardcoded values.

# x: int => Type Hinting
def calculate(x: int, y: int, oprn: str):
    if oprn == '+':
        return x + y
    elif oprn == '-':
        return x - y
    elif oprn == '*':
        return x * y
    elif oprn == '/':
        return x / y


