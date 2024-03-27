# VanBatenburg, Bobbie
# ICS 110P Assignment 09
# 03/26/2024
# This program will create a list of five values, use three different list
# methods/functions, pass list to a function called print_list,
# use a for loop to print list contents with numbers counting down from 5


def main():
    # Create a list of 5 values
    locations = ['Aurora, TX', 'Maury Island, WA', 'Roswell, NM', 'McMinnville, OR', 'Lancaster, NH']
    # Use a list method/function (1 of 3) and explain to the user what's going on
    length = len(locations)
    print('I have created a list that contains ', length, 'locations that have a history of UFO activity. \nHere is my list: \n', locations)

    # Use a list method/function (2 of 3) and explain to the user what's going on
    print('We had better add that time back in 1969 with Jimmy Carter to the list.\nI am going to use the append() method to add it to the end of the list now.')
    locations.append('Leary, GA')
    print(locations)
    new_length = len(locations)
    print('My list now has ', new_length, 'locations.')

    # Use a list method/function (3 of 3) and explain to the use what's going on
    print('I changed my mind.  I no longer want to include Leary, GA on my list.  I will use the pop() function to remove it.')
    locations.pop()
    print(locations)

    def print_list():
        number = 5
        print('Now I will use a for loop to print out a numbered version of this list.\n5 places associated with UFO activity:')
        for i in locations:
            print(number, i)
            number = number - 1
    print_list()

main()
        
