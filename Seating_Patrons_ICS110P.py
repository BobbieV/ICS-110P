# Bobbie VanBatenburg
# ICS 110P
# 1/25/2024

# Ask a user how many people are in their party
num_guests = int(input('How many people in your party? '))

# if it's a party of 1, seat them at the counter               
if num_guests < 2:
    print('We have a lovely seat for you at the counter!')
# if it's a party of 2, seat them at a small table
elif 1 < num_guests < 3:
    print('There is a beautiful table for two, ready just for you!')
# Otherwise seat them at a large table
elif 2 < num_guests < 9:
    print('We have a large table with plenty of room for all of you!')
# if the group is larger than 8, ask them to wait while accomdations are made
else:
    print('Please give us just a moment to organize the perfect space for your group.')


