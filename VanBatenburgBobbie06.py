# VanBatenburg, Bobbie
# ICS 110P Assignment 6
# 2/19/2024
# Create a function called main that asks the user to choose between two tasks
# One task (function option1() ) uses the math module with user input
# The second task (function option2() ) uses the random module with user input

import math
import random

# define option1 math function
def option1():
    user_num = int(input('Enter a number and I will find the square root!'))
    total = math.sqrt(user_num)
    print('The square root of ', user_num, 'is: ', total)

# define option2 random function
def option2():
    user_num = int(input('Choose a number 1, 2 or 3 and see if we choose the same number!'))
    my_num = random.randint(1,3)
    if user_num == my_num:
        print('You win! We both guessed ', my_num)
    elif user_num != my_num:
        print('Sorry, you did not win this time. My number was ', my_num)
    else:
        print('Sorry, that is not a valid option.')
# define main function
def main():
    # Greet the user and explain what the program can do
    print('Hello. I can do math or play a guessing game.')
    # Tell them how to play
    wanna_play = int(input('Enter 1 for math, 2 for the guessing game. or 0 to quit: '))
    # Create a loop so they can keep going as long as they want
    while wanna_play != 0:
        # Filter out junk responses
        try:
            # ooo they chose the math option
            if wanna_play == 1:
                option1()
                main()
            # ooo we gonna play a game
            elif wanna_play == 2:
                option2()
                main()
            # just in case they don't provide a valid response
            elif wanna_play >= 3:
                print('Sorry that is not a valid option.')
                main()
        # in case of errors
        except:
            print('Sorry, that is not a valid option.  Please try again.')
    # they select 0 to quit
    print('Goodbye!')
# Call the main function
main()
        
