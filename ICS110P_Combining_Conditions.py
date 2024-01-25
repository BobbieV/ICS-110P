# VanBatenburg, Bobbie
# ICS 110P
# Combining Conditions

# Declare variables with Nikki's information
my_name = 'Nikki'
my_age = 100
my_fave_food = 'sushi'

# Get input from user (name, age, favorite food)
user_name = input('Enter your name: ')
user_age = int(input('Enter your age: '))
user_fave_food = ('Enter your favorite food: ')

# Check if user's name, age, and fave food is the same
if my_name == user_name or my_age == user_age or user_fave_food == my_fave_food:
               print('We have at least one thing in common!')
else:
               print('We have nothing in common! :p')
print('goodbye')
