# VanBatenburg, Bobbie
# f-strings & Formatting Output

# Print 'I am selling a watermelon for $4.95'
name = 'Bobbie'
item = 'watermelon'
price = 4.95
quantity = 3
total = price + (price *.045)

print('I am selling a', item, '.')
print('I am selling a ' + item + '.')
print('%s is selling %d %s for $%s.' % (name, quantity, item, price))
print('{} is selling {} {} for ${}' .format(name,item, quantity, price))

print(f'I am selling a {item}')

print(f"Hello, {input('Enter your name: ')}!")
'''
print('It costs $', price)
print('It costs $' + str(price))

# Print the price of matermelon + tax
total = price + (price *.045)
print('The watermelon (plus tax) costs ....')
print(total)
'''
msg =(
    f'{name} is selling {quantity} {item}.'
    f'Each {item} costs ${price}.'
    f'The price plus tax is: ${total:.2f}'
)
print(msg)
