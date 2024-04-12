# --- BASIC OPERATIONS AND CONTROL FLOW ---

# Function to multiply two numbers or sum them if the product exceeds 1000.
def multiplication_or_sum(num1, num2):
    product = num1 * num2  # Calculate the product.
    if product <= 1000:    # Check if product is less than or equal to 1000.
        return product
    else:                  # If product is greater, return sum.
        return num1 + num2

# Demonstrating the function with different conditions.
result = multiplication_or_sum(20, 30)  # Expected to multiply.
print("The result is", result)

result = multiplication_or_sum(40, 30)  # Expected to sum due to large product.
print("The result is", result)

print("Hello, World!")  # Basic print statement to display a message.

# --- LISTS AND ITERATION ---

# Creating and printing a list of numbers.
numList = [1, 2, 3, 4, 5, 6]
print(numList)

# Printing all elements of the list using a for loop.
for x in numList:
    print(x)

# --- INPUT AND SIMPLE DATA PROCESSING ---

# Prompting user input, then printing a greeting.
# Uncomment to use:
# name = input("What is your name? ")
# print("Hello " + name)

# Calculating age from birth year provided by user.
# Uncomment to use:
# birth_year = input("Enter your birth year: ")
# age = 2024 - int(birth_year)
# print("Your age is ", age)

# --- DATA TYPE CONVERSION ---

# Demonstrating conversion between different data types: int, float, bool, str.
# Uncomment below to see data type conversion in action.
# first = input("First: ")
# second = input("Second: ")
# sum = float(first) + float(second)
# print("Sum: " + str(sum))

# --- STRING MANIPULATION ---

# Playing with string methods.
course = "python for beginners"
print(course.capitalize())  # Capitalize the first letter.
print(course.find('b'))     # Find the index of 'b' in the string.
print(course.count('n'))    # Count the occurrences of 'n'.
print(course.isspace())     # Check if the string is all whitespace.
blank_space = ' '
print(blank_space.isspace())  # Check if a string with a space is all whitespace.

# --- CONDITIONAL STATEMENTS ---

# Example of if statements.
if 5 > 2:
    print("Five is greater than two")

# Comparing two numbers input by the user.
# Uncomment below lines to run the comparison.
# first_number = int(input("Enter a number: "))
# second_number = int(input("Enter another number: "))
# if first_number > second_number:
#     print(f"{first_number} is greater than {second_number}")
# if first_number < second_number:
#     print(f"{first_number} is less than {second_number}")

# --- COMMENTS AND DOCSTRINGS ---

"""
This is a 
Multiline
String.
These can be used for multiline
comments since they will be ignored unless
they are assigned to a variable.
"""

# --- TYPE AND VARIABLE BASICS ---

# Demonstrating variable declaration and type casting.
x = int(3)  # Declare x as an integer.
y = str(4)  # Declare y as a string.
z = float(5)  # Declare z as a float.
r = bool(1)  # Declare r as a boolean.
print(x, y, z, r)
print(type(y))  # Show the type of y.

# Variable naming conventions and assignments.
"""
Variable names can start with a letter or _, but they cannot start with a number.
camelCase, PascalCase, snake_case are common naming conventions.
"""

# Assigning multiple values in one line.
a, b, c, d = "Why", "does", "this", "work"
print(a, b, c, d)

# Assigning the same value to multiple variables in one line.
e = f = g = "cheese"
print(e, f, g)

# Unpacking a list into variables.
fruits = ["apples", "bananas", "cherries"]
h, i, j = fruits
print(h, i, j)

# --- FUNCTIONS AND SCOPE ---

# Defining and using functions.
def returnName():
    # Prints a welcome message with a global username.
    print("Welcome", user_name)
# Note: `user_name` should be defined outside the function for this to work.

def newFunc():
    # Demonstrates creating a global variable from within a function.
    global gloVar
    gloVar = "What are we talking about, fellas?"
# Call `newFunc()` and then print `gloVar` to see the effect.

def changeGlobal():
    # Modifies a global variable from within a function.
    global globalVariable
    globalVariable = "radical"
# Initialize `globalVariable`, call `changeGlobal()`, and print `globalVariable`.

# --- BOOLEAN VALUES AND EXPRESSIONS ---

# Demonstrating boolean expressions and the bool() function.
print(10 > 9)  # True, because 10 is greater than 9.
print(10 == 9)  # False, 10 is not equal to 9.
print(10 < 9)  # False, 10 is not less than 9.
print(bool("hello"))  # True, non-empty strings are truthy.
number = 15
print(bool(number))  # True, non-zero numbers are truthy.

# --- CLASSES ---

# Example of a simple class with a constructor and a method.
class Employee:
    def __init__(self, age, weight, height, first_name, last_name, catch_phrase):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.catch_phrase = catch_phrase

    def print_name(self):
        print(self.first_name, self.last_name)
