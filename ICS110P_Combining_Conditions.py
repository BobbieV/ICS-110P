# VanBatenburg, Bobbie
# ICS 110P
# Combining Conditions

user_age = int(input('Enter your age: '))
if 18 < user_age < 22:
    print('You are a young adult.')
elif 22 < user_age < 35:
    print('You are STILL a young adult.')
elif 35 < user_age < 50:
    print('Dang, you are a grown-ass adult.')
elif 50 < user_age < 65:
    print('Are you getting the AARP mailers?')
elif 65 < user_age < 80:
    retired = input('Are you retired yet? (y/n)')
    if retired == 'y':
        print('Congratulations!')
    else:
        print('I hope you are retiring soon!')
elif user_age >80:
    print('The best years are yet to come!')
else:
    print('You are a baby!')
'''
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
'''
