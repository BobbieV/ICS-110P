# Get user's name
print('Enter your name:')
name = input()

# Print out the user's name
print('Hello,', name)

# Print ot the type of value in name
print(type(name))

# Prompt user to enter 2 numbers, then print total
print('Enter a number:', end=' ')
num1 = int(input())
print('Enter another number:', end=' ')
num2 = int(input())

# Calculate the total of the user's two numbers
total = num1 + num2

# Print the total
print("The sum of your two numbers is:", end=" ")
print(total)
    
# Prompt the user to enter a price, then add the tax
print('Enter the price:', end=" ")
price = float(input())
hawaii_tax = 1.045
total_cost = price * hawaii_tax
print('The total cost is:', total_cost)

# Convert '15' to int type and assign it to my_number
my_number = int('15')

print(type(my_number))

# Add 5 to the user's number
print('Enter a number:', end=' ')
user_number = int(input())
new_number = user_number + 5

# Print out new number
print(new_number)

# Test input prompt shortcut
hours = 40
weeks = 50
hourly_wage = int(input('Enter hourly wage: '))
print('Salary is', hourly_wage * hours * weeks)

# Read three numbers from user input
num1 = float(input('Enter a number: '))
num2 = float(input('Enter a 2nd number: '))
num3 = float(input('Enter a 3rd number '))
product = num1 * num2 * num3
print(product)
