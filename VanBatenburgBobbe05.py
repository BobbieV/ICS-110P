# VanBatenburg, Bobbie
# ICS 100P Assignment 05
# 2/12/2024
# This program will ask the user to choose between two tasks, one a math module application
# and two, a random module application

# Greet the user
user_name = input('Enter your name: ')
print('Hello, ', user_name)

# Explain the two tasks/filter out for errors
try: 
    wanna_play = int(input('Enter 1 for help with exponents or enter 2 to play a game.'))
    # If they picked 1, play a math game
    if wanna_play == 1:
        # We're not taking chances that these folks are gonna follow directions
        try:
            # Gonna have to import that Math Module
            import math
            # Lay it out for the user
            print('Enter two numbers and I can help you determine the exponential value!')
            base = int(input('Enter the base number: '))
            exponent = int(input('Enter the exponent: '))
            total = math.pow(base, exponent)
            print('The total of', base, 'to the', exponent, 'power is:', total)
        # If they didn't enter numbers they gonna find out
        except ValueError as e:
            print('Sorry, an error has occurred.')
            print(e)
            print('Please try again.')
    # We're gonna play a game!
    elif wanna_play == 2:
        # If they picked 2, play a game where you try to guess the random number between 1-100
        try:
            # Gotta import that Random Module
            import random

            print('I can generate a random number between 1 and 100')
            # Generate a random number between 1 and 100
            random_number = random.randint(1,100)
            your_guess = int(input('See if you can guess the number I am thinking of.  Enter your guess between 1 and 100: '))
            # What happens if they WIN
            if random_number == your_guess:
                print('YOU WIN! We both picked', random_number)
            # What happens if they LOSE
            else:
                print('My number was', random_number, 'and your number was', your_guess,". Better luck next time.")
        # if the user didn't enter a number, it's time to let em know
        except ValueError as e:
            print('Sorry, an error has occurred.')
            print(e)
            print('Please try again.')
    # If they didn't pick 1 or 2 it's not gonna work
    else:
        print('Sorry, that is not a valid option.  Please try again.')
# If they didn't enter a nuumber (int) for wanna_play, we gonna tell em 
except ValueError as e:
            print('Sorry, that is not a valid option.')
            print(e)
            print('Please try again.')
