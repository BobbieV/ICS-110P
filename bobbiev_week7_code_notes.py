# VanBatenburg, Bobbie
# Putting the FUN in Functions
'''
# Define a function that prints "hello"
def print_hello():
    # Code that will execute when the function is called
    print("hello")
# Call the print_hello() function
print_hello()

# Define a function that prints a face
def print_face():
    face_char = 'o'
    print(' ', face_char, '', face_char)
    print('  ', face_char)
    print("", face_char * 5)

# Call the print_face() function
print_face()

# Test Yourself:
# Define a function called print_pattern()
def print_pattern():
    print('@@@@@')
# Write a program that calls the function twice
print_pattern()
print_pattern()

# Test Yourself: Function Definition: print_shape()
#Define a new function called print_shape()
def print_shape():
    print('***')
    print('***')
    print('***')
# Call the function once in your program
print_shape()
'''

# Define a function that prints "hello" to a person
def print_hello(name):
    print('Hello, ' + name + '!')
'''
# Call the print_hello(name) function
print_hello(input('What is your name?'))
'''

# Define the main function
def main():
    user_name = input('Enter your name: ')
    print_hello(user_name)
# Call the main function
main()
# Test Yourself: Function Definition: print_shape() with one parameter
#Define a new function called print_shape()
def print_shape(shape):
    print(shape * 3)
    print(shape * 3)
    print(shape * 3)
# Call the function once in your program
print_shape(input('Press a key and I will make a shape out of it: '))

# Define a function that returns "hello"
def return_hello():
    msg = "hello"
    return msg
message = return_hello()
print(message)

# Define a function that adds two numbers together then returns the sum
def add_numbers(num1, num2):
    total = num1 + num2
    return total
num1 = int(input('enter a number'))
num2 = int(input('Enter another number'))
sum_of_nums = num1 + num2
print(sum_of_nums)
