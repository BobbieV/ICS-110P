# VanBatenburg, Bobbie
# List Basics
'''
# This variable holds 1 integer
my_integer = 100

# This variable holds 1 string
my_string = "blueberry cheesecake"

# Create a list
grocery_list = ['eggs', 'milk', 'kale', 'gushers']
my_list = [1, 'Hello', 3.14, True]

print(grocery_list)

# Create a list called myNums containing the elements 5, 10, and 20
myNums = [5, 10, 20]

# Create a list called myNoms containing 3 of your favorite foods
myNoms = ['pizza', 'nachos', 'acai bowls']

# Create a list called myList containing the elements -100 and the string "Lists are fun!"
myList = [-100, 'Lists are fun!']

# Create an empty list called myEmptyList
myEmptyList = []
'''
'''
# Try it yourself: Working with List Elements

# Create a list of 5 cities you would like to visit
my_cities = ['Seattle', 'Portland', 'Las Vegas', 'Santa Fe', 'Dallas/Fort-Worth']

# Print the last city in your list
print(my_cities[4])

# Replace the last city with a different city
my_cities[4] = 'San Francisco'

# Print the last city in your list again
print(my_cities[4])
'''
'''
# When we use a method, we follow this format:
#    object_name.method()
grocery_list = ['eggs', 'milk', 'kale', 'gushers']
print(grocery_list)

# Add an element with append()
grocery_list.append("Apples")
print(grocery_list)

# Remove an element with remove()
grocery_list.remove('kale')
print(grocery_list)

# Remove an element at a specified index number with pop()
grocery_list.pop(1)
print(grocery_list)
'''
'''
# Try It Yourself: Adding/Removing Elements
house_prices = ['$140,000', '$550,000', '$480,000']
print(house_prices)

# 1. Update the price of the second item in house_prices to '$175,000'.
house_prices[1] = '$175,000'
print(house_prices)

# 2. Add a price to the end of the list with a value of '$1,000,000'.
house_prices.append('$1,000,000')
print(house_prices)

# 3. Remove the 1st element from house_prices, using the pop() method.
house_prices.pop(0)
print(house_prices)

# 4. Remove '$480,000' from house_prices using the remove() method.
house_prices.remove('$480,000')
print(house_prices)
'''
'''
grocery_list = ['eggs', 'milk', 'kale', 'gushers', 'apples']
groceries2 = ['cereal', 'poptarts', 'ice cream']

my_list = grocery_list + groceries2

# len()
list_length = len(my_list)
print('There are ', list_length, 'items on the list.')
'''
'''
numbers = [5, 19, 50, 0, 14, 20, 5, 100, 5]

max_number = max(numbers)
min_number = min(numbers)
sum_numbers = sum(numbers)
print(min_number)
print(max_number)
print(sum_numbers)
your_number = int(input('Tell me a number and if it is present in the list, I will tell you the index number\nEnter your number: '))
index_first_val_match = numbers.index(your_number)
print('The index of the first match of your value is ', index_first_val_match)
how_many_times_in_list = numbers.count(your_number)
print('It occurs ', how_many_times_in_list, ' times in this list.')
'''
'''
grocery_list = ['eggs', 'milk', 'kale', 'gushers', 'apples']

for i in grocery_list:
    print(i)
'''
'''
names = ['Anna', 'Bob', 'Charlie', 'Diana']

for n in names:
    print(n)

print('Finished with the loop!')
'''
'''
# Test Yourself: Print out these lists with a for loop

groceries = ['milk', 'eggs', 'kale', 'candy']

for g in groceries:
    print(g)

home_prices = [550000, 1800000, 762000]

for h in home_prices:
    print(h)

ages = [18,18, 20, 18, 26, 19, 18, 19]
for a in ages:
    print(a)
'''
'''
# Test Yourself: Using for loops with lists

# A list of temperatures (in Celcius)
temps = [30, 20, 2, -5, -15, -8, -1, 0,5, 35, 16, -4, 10, -17]

# Count how many temps in the list are below 0
below_zero = 0
for i in temps:
    if i < 0:
        below_zero = below_zero + 1
print(below_zero, 'temps in the list are below zero.')
'''

# Test Yourself: Using for loops with lists

# A list of stock prices
stock_prices = [34.62, 76.30, 85.05]

# Print contents of list with a $ in front
for i in stock_prices:
    print('$', i)
