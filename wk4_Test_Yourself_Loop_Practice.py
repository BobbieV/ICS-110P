# VanBatenburg, Bobbie
# 2/3/2024
# ICS 110P

# Test Yourself: Loop Practice
'''
# Counting with while loops
# To iterate N times using an integer loop variable i with a while loop:

i = 1
while i >= N:
    # loop body
    i = i + 1
'''
# Loop Practice: Basic Counting with while Loops
'''
# Write a while loop that iterates 10 times

i = 1
while i <= 10:
    print(i)
    i = i + 1
'''
'''
# Write a while loop that iterates 99 times

i = 1
while i <= 99:
    print(i)
    i = i + 1
'''
'''
# Write a while loop that iterates 2 times

i = 1
while i <= 2:
    print(i)
    i = i + 1
'''
'''
# Write a while loop that counts down from 5, 4, 3, 2, 1

i = 5
while i > 0:
    print(i)
    i = i -1
'''
'''
# Write a while loop that counts from 0 to 100 by 2's (0, 2, 4...)

i = 0
while i <= 100:
    print(i)
    i = i + 2
    '''

# Loop Practice: Basic Counting with while loops
'''
# Beginning with the year 1792, every 4 years is a US presidential election year
i = int(input('Enter a year after 1792:'))
while i <= 2024:
    print(i, " is an election year")
    i = i + 4
'''
'''
# Write a while loop that iterates over the odd integers from 211 down to 31 (inclusive)
i = 211
while i >= 31:
     print(i)
     i = i - 3
'''
'''
# Write a while loop that iterates from -100 to 65

i = -100
while i <= 65:
     print(i)
     i = i + 1
'''
# Break Statements
'''
while True:
     print('Enter 1 to print hello')
     print('Enter 2 to print goodbye')
     print('Enter 0 to exit')
     number = int(input('Enter a number: '))

     if number == 1:
          print('hello')
     elif number == 2:
          print('goodbye')
     elif number == 0:
          break
     else:
          print('That is not a valid option')
'''
