# Bobbie VanBatenburg
# ICS 100P
# 2/12/2024
# Try-Except

try:
    print('Enter two numbers and I will add them together!')
    num1 = int(input('Enter the 1st number: '))
    num2 = int(input('Enter the 2nd number: '))
    total = num1 + num2
    print('The sum of your two numbers is...', total)

except ValueError as e:
    print('Hmmm....Something went wrong')
    print('Error:')
    print(e)


