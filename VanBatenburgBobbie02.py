# VanBatenburg, Bobbie
# ICS 110P Assignment 02
# January 16, 2024
# Print a Mad Libs story based on user input

# Welcome user to program

print('Welcome to my MadLib program!')
print('I will ask you for some input, then use your input to print out a silly story!')


# Ask user for input
num1 = int(input('Enter a whole number: '))
name = input('Enter a name: ')
adj1 = input('Enter an adjective: ')
noun1 = input('Enter a noun: ')
num2 = float(input("Enter a decimal number: "))
adj2 = input('Enter an adjective: ')
noun2 = input('Enter a noun: ')
num3 = float(input('Enter a decimal number: '))
num4 = num2 + num3
num5 = int(input('Enter a whole number: '))
noun3 = input('Enter a plural noun: ')

# Tell the user a silly story
print("MY TRIP TO THE MALL")
print('Last Friday, I went to the mall with ', num1, 'of my friends.  My best friend,', name, 'bought a ', adj1, noun1, 'for $', num2, 'and I bought a ', adj2, noun2, 'for $', num3,'. Together we spent $', num4, ', which is enough to buy ', num5, noun3,'.')
