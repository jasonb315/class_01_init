# When run, the program should print an intro message and th
# e menu for the restraunt.
# The restaurant’s menu should include appetizers, entrees, d
# esserts, and beverages. At least 3 in each category
# The program should prompt the user for an order
# When a user enters an item, the program should print an a
# cknowledgment of their input
# The program should tell the user how to exit

from textwrap import dedent
import sys

WIDTH = 96

# SEAT = [
#     {
#         'question': 'How many today?\n',
#         'answer': '0',
#     },
# ]
MENU = [APP, ENT, DES, BEV]

APP = [
    {
        'item:': 'Tarantula Crisp',
        'count': 0,
    },
    {
        'item:': 'Crickett Platter',
        'count': 0,
    },
    {
        'item:': 'Mouse Kabob',
        'count': 0,
    },
]

ENT = [
    {
        'item:': 'Roadkill',
        'count': 0,
    },
    {
        'item:': 'Brazed Housecat',
        'count': 0,
    },
    {
        'item:': 'Human Infant',
        'count': 0,
    },
]

DES = [
    {
        'item:': 'Mice-cream',
        'count': 0,
    },
    {
        'item:': 'Frog-yo',
        'count': 0,
    },
    {
        'item:': 'Oreos and Cream',
        'count': 0,
    },
]

BEV = [
    {
        'item:': 'Rattlesnake',
        'count': 0,
    },
    {
        'item:': 'Snake Eyes',
        'count': 0,
    },
    {
        'item:': 'Milk Snake',
        'count': 0,
    },
]

# close menu


def ask_question(question):
    return input(question)


def check_input(user_in, item):
    if user_in.lower() == 'leave':
        exit()
        return

    if user_in.lower()


def give_menu():
    for i in range(MENU):
        print(MENU[i])
        for e in MENU[i]:
            print(e['item'])


def greeting():
    '''
    Fx will print conversational greeting to the user when opening script.
    '''

    ln_one = 'Hey there! Welcome to sssssSneksss Cafe!'

    print(dedent(f'''
        {'*' * WIDTH}
        {(' ' * ((WIDTH - len(ln_one)) // 2)) + ln_one + (' ' * (WIDTH - len(ln_one)) // 2))}
        {'*' * WIDTH}
    '''))


def exit():
    print(dedent('''
        Thanksss for ssstopping by!
    '''))


def run():
    greeting()
    give_menu()


if __name__ == '__main__':
    run()
