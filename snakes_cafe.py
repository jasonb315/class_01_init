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

APP = [
    {
        'header': 'APPETIZERSss',
    },
    {
        'item': 'Tarantula Crisp',
        'count': 0,
    },
    {
        'item': 'Crickett Platter',
        'count': 0,
    },
    {
        'item': 'Mouse Kabob',
        'count': 0,
    },
]

ENT = [
    {
        'header': 'ENTRESss',
    },
    {
        'item': 'Roadkill',
        'count': 0,
    },
    {
        'item': 'Brazed Housecat',
        'count': 0,
    },
    {
        'item': 'Human Infant',
        'count': 0,
    },
]

DES = [
    {
        'header': 'DESSSERTSss',
    },
    {
        'item': 'Mice-cream',
        'count': 0,
    },
    {
        'item': 'Frog-yo',
        'count': 0,
    },
    {
        'item': 'Rabbit Souffle',
        'count': 0,
    },
]

BEV = [
    {
        'header': 'BEVERAGESss',
    },
    {
        'item': 'Rattlesnake',
        'count': 0,
    },
    {
        'item': 'Snake Eyes',
        'count': 0,
    },
    {
        'item': 'Milk Snake',
        'count': 0,
    },
]

MENU = [APP, ENT, DES, BEV]


def ask_question(question):
    return input(question)


def take_order():
    initial_order = True
    ordering = True
    no = {'no', 'n', 'nay', 'no thanks', 'jog on mate', 'that\'s all'}

    while ordering:
        if initial_order:
            item = input('What can I get ya?').lower()
        else:
            item = input('Anything else?').lower()

        if item == no:
            pass

        else:
            check_input(item)

            for i in range(len(MENU)):
                for j in range(len(MENU[i])-1):
                    if(MENU[i][j+1]['item']).lower() == item:
                        MENU[i][j+1]['count'] += 1
                        print(dedent(f'''
                            Ok, that's going to be {str(MENU[i][j+1]['count'])} {str(MENU[i][j+1]['item'])}
                        '''))
                        initial_order = False
                        take_order()
                    else:
                        ordering = False


def check_input(user_in):
    if user_in.lower() == 'leave':
        exit()


def order_ready():
    yes = {'yes', 'y', 'ye', 'sure', 'Fuck yeah dawg', ''}
    ready = input('Ready to order?')
    if ready in yes:
        take_order()
    else:
        print('look we\'re busy so make up your mind.')
        order_ready()


def give_menu():

    for i in range(len(MENU)):

        print(dedent(f'''
            {'-' * WIDTH}
            {MENU[i][0]['header']}
            {'-' * WIDTH}
        '''))
        for j in range(len(MENU[i])-1):
            print(MENU[i][j+1]['item'])
        print('-' * WIDTH)


def greeting():
    '''
    Fx will print conversational greeting to the user when opening script.
    '''

    ln_one = 'Hey there! Welcome to sssssSneksss Cafe!'

    print(dedent(f'''
        {'*' * WIDTH}
        {(' ' * ((WIDTH - len(ln_one)) // 2)) + ln_one +
            (' ' * ((WIDTH - len(ln_one)) // 2))}
        {'*' * WIDTH}
    '''))


def exit():
    print(dedent('''
        Thanksss for ssstopping by!
    '''))


def run():
    greeting()
    give_menu()
    order_ready()


if __name__ == '__main__':
    run()
