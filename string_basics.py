# VanBatenburg, Bobbie
# String Basics
'''
my_string = "What's new, Scooby-Doo?"

print(my_string[3])
print(my_string[5:10])
print(my_string[15:])
print(my_string[:5])
print(my_string[5:20:2])

print('The last character is: ', my_string[-1])
'''
'''
name = input("Enter your name: ")
print('The last character is: ', name[len(name)-1])

print('The last 3 characters are: ', name[-3:])
length = len(name)
print(length)
'''
'''
msg = input('Enter a message: ')
if 'hello' in msg:
    print('Hello to you too!')
'''
'''
print('ana' in 'banana')
'''
name = input('Enter your name: ')
if name < 'nikki':
    print('Your 1st initial comes before mine in the alphabet!')
elif name > 'nikki':
    print('Your 1st initial comes after mine in the alphabet')
else:
    print(' Uhhhhh do we have the same name?')
