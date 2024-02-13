# Bobbie VanBatenburg
# ICS 110P - Constants & Modules
# 2/12/2024

'''
# Math Module: pi
import math

pizza_radius = 6
pizza = 2 * math.pi * pizza_radius
print('The circumference of a 12" pizza is: ')
print(pizza)
'''
'''
# Math Module: square root

import math

number = int(input('Enter a number and I will tell you the square root!'))
num_sqrt = math.sqrt(number)
print('The square root of ', number,'is', num_sqrt)
'''
'''
# Math Module: factorial
import math
number = int(input('Enter a number and I will tell you the factorial of that number!'))
num_factorial = math.factorial(number)
print(number,"factorial equals", num_factorial)
'''
'''
# Math module: ceiling & floor
import math

number = float(input('Enter a decimal number and I will round it up and down for you!'))
num_round_up = math.ceil(number)
num_round_down = math.floor(number)
print('Rounded up, your number is: ', num_round_up)
print('Rounded down, your number is: ', num_round_down)
'''
'''
# Math Module: greatest common divisor

import math
print('Enter two numbers and I will tell you their greatest common divisor!')
number_1 = int(input('Enter your first number'))
number_2 = int(input('Enter your second number'))
gcd = math.gcd(number_1, number_2)
print('The greatest common divisor of ', number_1, 'and ', number_2, 'is: ', gcd)
'''
'''
#Math Module: exponentiation

import math

print('Enter two numbers and I can help you determine the exponential value!')
base = int(input('Enter the base number: '))
exponent = int(input('Enter the exponent: '))
total = math.pow(base, exponent)
print('The total of', base, 'to the', exponent, 'power is:', total)
'''
'''
# Determine interest

import math
print('I can help you figure out how much interest your savings will earn.')
base = float(input('Enter initial savings: '))
rate = float(input('Enter annual interest % rate: '))
years = int(input('Enter number of years saved: '))

total = base * math.pow(1 + (rate / 100), years)
print('Savings after', years, 'years is', total)
'''
'''
# Determine randomness
# Play a game where you try to guess the random number between 1-100
import random

print('I can generate a random number between 1 and 100')
random_number = random.randint(1,100)
your_guess = int(input('See if you can guess the number I am thinking of.  Enter your guess between 1 and 100: '))
if random_number == your_guess:
    print('YOU WIN! We both picked', random_number)
else:
    print('My number was', random_number, 'and your number was', your_guess,". Better luck next time.")
'''

# Math & Random Modules example

import math
import random
my_random_num = random.randint(1, 1000)
user_num = int(input('Enter a number: '))

print('My number is:', my_random_num)
print("The GCD of our numbers is:")
print(math.gcd(my_random_num, user_num))
