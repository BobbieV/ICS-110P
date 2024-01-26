# Bobbie VanBatenburg
# 1/25/2024
# ICS 110P
# Greet the user, then sell them some stuff

# Prices of assorted items
jar_of_earwigs = 14.99
rusty_flashlight = 17
knuckle_sandwich = 0
# Ask the user for their name and say Hello *Name*
user_name = input('What is your name?')
# Say hello, addressing user by name
print('Hello, ', end='')
print(user_name)
# Explain to the user that you are selling items, ask if they want anything
you_like_buy = input('I have some very unique items for sale.  Would you be interested in hearing about them?')
if you_like_buy == 'n' or you_like_buy == 'no':
    print('Let me know if you change your mind.  Goodbye!')
# make sure they answer correctly
elif you_like_buy != 'y' and you_like_buy != 'yes' and you_like_buy != 'n' and you_like_buy != 'no':
    print('Sorry, I do not understand that answer. Please try again later.')
elif you_like_buy == 'y' or you_like_buy == 'yes':
# define whatchu_want and user_money
    whatchu_want = int(input('I have this jar full of earwigs for $14.99 (1), a rusty flashlight for $17 (2) or a knuckle sandwich for free (3).  Which one would you like?  Choose a number 1-3'))
    user_money = int(input('How much money do you have to spend today?'))
# Buy or don't buy #1
    if whatchu_want == 1 and user_money >= 14.99:
        print('SOLD!  You are the proud new owner of this lovely jar of earwigs!')
    elif whatchu_want == 1 and user_money < 14.99:
        print('That\'s not quite enough, but perhaps you would be interested in a complimentary knuckle sandwich instead?')
# Buy or don't buy #2
    elif whatchu_want == 2 and user_money >= 17:
        print('Congratulations!  You have purchased the finest rusty flashlight this side of the Mississippi!')
    elif whatchu_want == 2 and user_money < 17:
        print('That\'s not quite enough, but perhaps you would be interested in a complimentary knuckle sandwich instead?')
# Get one knuckle sandwich brah.
    elif whatchu_want == 3:
        print('Alright then.  You asked for it.')
        print('BANG! ZOOM! RIGHT IN THE KISSER!')
        print('Just kidding.  I am not a certified knuckle sandwich technician, but I do have one I can refer you to if you are still interested.')
    elif whatchu_want != 1 and whatchu_want != 2 and whatchu_want != 3 or user_money != int:
        print('Hmmm.  That doesn\'t make sense.')
