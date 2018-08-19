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
# from uuid import uuid4


WIDTH = 96
ORDER_WIDTH = 96
no = {'no', 'n', 'nay', 'no thanks', 'jog on mate', 'that\'s all', 'nope'}
yes = {'yes', 'y', 'ye', 'sure', 'fuck yeah dawg', 'please', ''}


# MENU dic, SECTION dic, key item : vals being count and price
MENU = {

    'APPETIZERSss':
        {
            'Tarantula Crisp': {
                'price': 9.99,
                'ordered': 0,
                'stock': 10
            },
            'Crickett Platter': {
                'price': 9.99,
                'ordered': 0,
                'stock': 10
            },
            'Mouse Kabob': {
                'price': 9.99,
                'ordered': 0,
                'stock': 10
            },
        },

    'ENTRESss':
        {
            'Roadkill': {
                'price': 9.99,
                'ordered': 0,
                'stock': 10
            },
            'Brazed Housecat': {
                'price': 9.99,
                'ordered': 0,
                'stock': 10
            },
            'Human Infant': {
                'price': 9.99,
                'ordered': 0,
                'stock': 10
            },
        },

    'DESERTSss':
        {
            'Mice-cream': {
                'price': 9.99,
                'ordered': 0,
                'stock': 10
            },
            'Frog-yo': {
                'price': 9.99,
                'ordered': 0,
                'stock': 10
            },
            'Rabbit Souffle': {
                'price': 9.99,
                'ordered': 0,
                'stock': 10
            },
        },

    'BEVERAGESss':
        {
            'Rattlesnake': {
                'price': 9.99,
                'ordered': 0,
                'stock': 10
            },
            'Snake Eyes': {
                'price': 9.99,
                'ordered': 0,
                'stock': 10
            },
            'Milk Snake': {
                'price': 9.99,
                'ordered': 0,
                'stock': 10
            },
        },
}


def greeting():
    '''
    Fx will print conversational greeting to the user when opening script.
    '''

    ln_one = 'Hey there! Welcome to sssssSneksss Cafe!'
    ln_two = 'Have a ssseat, here\'s a menu:'
    ln_thr = '[enter \'leave\' at anytime to leave]'

    print(dedent(f'''
        {'*' * WIDTH}
        {(' ' * ((WIDTH - len(ln_one)) // 2)) + ln_one +
            (' ' * ((WIDTH - len(ln_one)) // 2))}
        {(' ' * ((WIDTH - len(ln_two)) // 2)) + ln_two +
            (' ' * ((WIDTH - len(ln_two)) // 2))}
        {(' ' * ((WIDTH - len(ln_thr)) // 2)) + ln_thr +
            (' ' * ((WIDTH - len(ln_thr)) // 2))}
        {'*' * WIDTH}
    '''))


def ask_question(question):
    return input(question)


def check_input(user_in, item):
    if user_in.lower() == 'quit':
        exit()
        return


def feedback(status):
    pass


def exit():
    print(dedent('''
        Thanks for stopping by!
    '''))
    sys.exit()


def run():
    greeting()
    print_menu()


def print_menu():
    for key, value in MENU.iteritems():
        print(key, value)


if __name__ == '__main__':
    run()



# MENU = [APP, ENT, DES, BEV]


# def ask_question(question):
#     return input(question)


# initial_order = True


# def take_order():
#     global no
#     global yes
#     global initial_order

#     ordering = True

#     while ordering:
#         phrase_one = 'What can I get ya?\n'
#         phrase_two = 'Anything else?\n'

#         if not initial_order:
#             item = input(f'''{phrase_two}''').lower()
#         else:
#             item = input(f'''{phrase_one}''').lower()

#         for i in range(len(MENU)):
#             for j in range(len(MENU[i])-1):
#                 if(MENU[i][j+1]['item']).lower() == item:
#                     MENU[i][j+1]['count'] += 1
#                     print(dedent(f'''
#                         Ok, that\'s {str(MENU[i][j+1]['count'])}
#                         {str(MENU[i][j+1]['item'])}.
#                     '''))

#         initial_order = False

#         if item in yes:
#             print('\n What can I get ya?')

#         if item in no:
#             read_order()
#             ordering = False
#             break

#         if item == 'leave':
#             exit()


# def read_order():
#     print('\nORDER\n')
#     for i in range(len(MENU)):
#             for j in range(len(MENU[i])-1):
#                 if(MENU[i][j+1]['count']) > 0:
#                     print(f'''{MENU[i][j+1]['count']} {MENU[i][j+1]['item']}, $ {(MENU[i][j+1]['count'] * MENU[i][j+1]['price'])}''')


# def check_input(user_in):
#     if user_in.lower() == 'leave':
#         exit()


# def order_ready():
#     global yes
#     ready = input('\nReady to order?\n')
#     if ready == 'leave':
#         exit()

#     if ready in yes:
#         take_order()
#     else:
#         print('\nlook hun, we\'re busy so make up your mind.')
#         order_ready()


# def give_menu():
#     print('-' * WIDTH)
#     print('MENU')
#     print('-' * WIDTH)
#     for i in range(len(MENU)):

#         print(dedent(f'''{' ' * 10}
#         {chr(8857)}{' ' * 3}{MENU[i][0]['header']}'''))

#         for j in range(len(MENU[i])-1):
#             print(dedent(f'''
#             {MENU[i][j+1]['item']} {'.' * (WIDTH - len(MENU[i][j+1]['item']) - 3 - len(str(MENU[i][j+1]['price'])))} ${MENU[i][j+1]['price']}
#             '''))
#     print('-' * WIDTH)


# def greeting():
#     '''
#     Fx will print conversational greeting to the user when opening script.
#     '''

#     ln_one = 'Hey there! Welcome to sssssSneksss Cafe!'
#     ln_two = 'Have a ssseat, here\'s a menu:'
#     ln_thr = '[enter \'leave\' at anytime to leave]'
#     print(dedent(f'''
#         {'*' * WIDTH}
#         {(' ' * ((WIDTH - len(ln_one)) // 2)) + ln_one +
#             (' ' * ((WIDTH - len(ln_one)) // 2))}
#         {(' ' * ((WIDTH - len(ln_two)) // 2)) + ln_two +
#             (' ' * ((WIDTH - len(ln_two)) // 2))}
#         {(' ' * ((WIDTH - len(ln_thr)) // 2)) + ln_thr +
#             (' ' * ((WIDTH - len(ln_thr)) // 2))}
#         {'*' * WIDTH}
#     '''))


# def exit():
#     print(dedent('''
#         Thanksss for ssstopping by!
#     '''))
#     sys.exit()


# def run():
#     greeting()
#     give_menu()
#     order_ready()


# if __name__ == '__main__':
#     run()
