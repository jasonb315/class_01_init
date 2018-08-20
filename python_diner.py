# imports
from textwrap import dedent
import sys
import uuid
import csv


# globals
initial_order = True
WIDTH = 66
menu_set = False
menu = {}
default_menu = {

    'APPETIZERSss':
        {
            'noms': {
                'price': 3.99,
                'stock': 25
            },
            'friedcrickets': {
                'price': 3.99,
                'stock': 25
            },
            'mousebobs': {
                'price': 4.99,
                'stock': 25
            },
            'cricketplatter': {
                'price': 5.99,
                'stock': 25
            },
            'eggyweggs': {
                'price': 3.99,
                'stock': 25
            },
            'froglegs': {
                'price': 4.99,
                'stock': 25
            },
        },

    'ENTRESss':
        {
            'roadkill': {
                'price': 7.99,
                'stock': 56
            },
            'parrot': {
                'price': 12.99,
                'stock': 16
            },
            'smallchild': {
                'price': 23.99,
                'stock': 3
            },
            'monkey': {
                'price': 19.99,
                'stock': 12
            },
            'dog': {
                'price': 17.99,
                'stock': 35
            },
            'cat': {
                'price': 14.99,
                'stock': 45
            },
        },

    'ssSIDESss':
        {
            'nomnoms': {
                'price': 3.99,
                'stock': 100000000
            },
            'treefrog': {
                'price': 5.99,
                'stock': 12
            },
            'cricketfries': {
                'price': 5.99,
                'stock': 50
            },
            'kitten': {
                'price': 8.99,
                'stock': 54
            },
            'puppy': {
                'price': 8.99,
                'stock': 0
            },
            'infant': {
                'price': 12.99,
                'stock': 2
            },
        },

    'DESssERTSss':
        {
            'micecream': {
                'price': 5.99,
                'stock': 15
            },
            'frogyo': {
                'price': 5.99,
                'stock': 45
            },
            'cake': {
                'price': 5.99,
                'stock': 6
            },
            'milksnake': {
                'price': 7.99,
                'stock': 85
            },
            'cococrickets': {
                'price': 6.99,
                'stock': 4
            },
            'sssouffle': {
                'price': 10.99,
                'stock': 2
            },
        },

    'BEVERAGESss':
        {
            'water': {
                'price': 0.99,
                'stock': 10000
            },
            'fanta': {
                'price': 1.99,
                'stock': 50
            },
            'blep': {
                'price': 5.99,
                'stock': 50
            },
            'superblep': {
                'price': 5.99,
                'stock': 7
            },
            'rattlesnake': {
                'price': 5.99,
                'stock': 7
            },
            'snakeeyes': {
                'price': 5.99,
                'stock': 7
            },
        },
}


class Order:
    '''
    this is the order constructor
    '''
    def __init__(self):
        '''
        instantiation
        '''
        self.items = {}
        self.total = 0
        self.id = str(uuid.uuid4())

    def __repr__(self):
        return f'''Order: {self.id} | Items: {self.items} | Total: {
            round(self.total, 2)}'''

    def __len__(self):
        return len(self.items)

    def modify_order(self, prompt):
        '''
        When called, this will adjust the order. prompt takes one input as the item to modify, and a second optional as the nuber to add or subtract
        '''
        try:
            item, quantity = prompt.split(
                ' ')[0].lower(), int(prompt.split(' ')[1])
        except (IndexError, TypeError):
            print('One then?')
            item, quantity = prompt.split(' ')[0].lower(), 1
        else:
            item, quantity = prompt.split(
                ' ')[0].lower(), int(prompt.split(' ')[1])
        # 'order' is an array [item, quantity]
        # I have the item I want and I know it's on the menu.
        # find it in stock and check amount.
        # If good, modify order for count and price
            # go through menu
        for cat, value in menu.items():
            for food in menu[cat]:
                if item == food:
                    # ok we have attention to the menu item
                    # if subtracting from order
                    if quantity < 0:
                        # subtracting, check order for presence
                        if item in self.items:

                            if (self.items[item] + quantity) >= 0:
                                self.items[item] += quantity
                                self.total += (quantity * menu[cat][
                                    food]['price'])
                                menu[cat][food]['stock'] -= quantity
                                print(f'''{abs(quantity)} {
                                    item} has been removed from your order.''')
                                print('Anything else?\n')
                            else:
                                print('You haven\'t ordered that many.')

                        else:
                            print(
                                'I\'m sorry, you haven\'t '
                                'ordered any of those.')
                            print('Anything else?\n')

                    # if adding to order
                    if quantity > 0:
                        # check stock
                        if (menu[cat][food]['stock'] - quantity) >= 0:
                            # make food
                            menu[cat][food]['stock'] -= quantity
                            # serve
                            if item in self.items:
                                self.items[item] += int(quantity)
                            else:
                                self.items[item] = int(quantity)
                            # and bill
                            self.total += (quantity * menu[cat][food]['price'])
                            print(f'''{abs(quantity)} {
                                item} has been added to your order.''')
                            print('Anything else?\n')
                        elif(menu[cat][food]['stock'] > 0):
                            print(f'''Sorry, we only have {
                                menu[cat][food]['stock']} left.''')
                            print('I\'ll put them all on your order')

                            if item in self.items:
                                self.items[item] += menu[cat][food]['stock']
                            else:
                                self.items[item] = menu[cat][food]['stock']

                            self.total += (menu[cat][food]['stock'] * menu[cat][food]['price'])
                            menu[cat][food]['stock'] = 0
                        elif(menu[cat][food]['stock'] == 0):
                            print('We\'re all out of those')

    def display_order(self):
        '''
        prints the order to the user and saves it to a txt file.
        If no file, will create,
        if file, will overwrite.
        Order instances are unique.
        '''
        user_receipt = ''
        user_receipt += ('\n' + '*' * 50 + '\n' + 'The Python Diner' + '\n' + 'Order ' + str(self.id) + '\n' + '=' * 50)
        sub_total = 0
        taxed = 0
        for cat, value in menu.items():
            for food in menu[cat]:
                if food in order.items:
                    user_receipt += (f'''\n{self.items[food]} {food} ... {self.items[food] * menu[cat][food]['price']}''')
                    sub_total += self.items[food] * menu[cat][food]['price']

        taxed = round((float(sub_total) * .096), 2)

        user_receipt += ('\n' + '-' * 50)
        user_receipt += ('\nSubtotal: {:>40.2f}'.format(round(sub_total, 2)))
        user_receipt += ('\nTax: {:>45.2f}'.format(round(taxed, 2)))
        user_receipt += ('\n' + '-' * 50)
        user_receipt += ('\nTotal Due: {:>39.2f}'.format(round((sub_total + taxed), 2)))
        user_receipt += ('\n' + '*' * 50)

        print(user_receipt)

        with open(f'order-{self.id}.txt', 'w') as f:
            f.write(user_receipt)


order = Order()


def take_order():
    '''
    First order and subsequent orders have different prompts.
    '''
    global initial_order

    if initial_order:
        initial_order = False
        print('Ready to order? what can I get ya?\n')
        print(chr(8811) + '   <item_name> [ + or - integer ]\n')

    else:
        print('Anything else?\n')
        print('enter \'order\' to see your order.\n')
        # ordering = False


def greet():
    '''
    Fx will print conversational greeting to the user when opening script.
    '''

    ln_one = 'Hey there! Welcome to sssssSneksss Cafe.'
    ln_two = 'Have a ssseat!'
    ln_thr = 'Enter \'quit\' at any time to leave.'
    sy = chr(9868)
    print(dedent(f'''
        {sy * WIDTH}
        {(' ' * ((WIDTH - len(ln_one)) // 2)) + ln_one +
            (' ' * ((WIDTH - len(ln_one)) // 2))}
        {(' ' * ((WIDTH - len(ln_two)) // 2)) + ln_two +
            (' ' * ((WIDTH - len(ln_two)) // 2))}
        {(' ' * ((WIDTH - len(ln_thr)) // 2)) + ln_thr +
            (' ' * ((WIDTH - len(ln_thr)) // 2))}
        {sy * WIDTH}'''))


def print_menu():
    '''
    prints the menu
    '''
    for cat, value in menu.items():
        print('')
        print(f'''{chr(8857)}   {cat}''')
        print('')
        for food in menu[cat]:
            print(dedent(f'''{food}{'.' *
            (WIDTH - 1 -len(food) -
            len(str(menu[cat][food]['price'])))} $ {
                menu[cat][food]['price']}'''))
    print('')


def menu_select():
    '''
    opening prompt called before menu selection in core()
    '''
    print('To see our menu, enter \'see menu\'.')
    print('Or to load a menu, enter \'load menu\'')


def load_external_menu(path):
    global menu
    global default_menu
    print('feature not enabled')
    menu = default_menu
    # try:
    #     with open(path, 'r') as f:
    #         menu_import = csv.reader(f)
    #         for row in menu_import:
    #             menu[row[0]]
    #             # item = iter(row[1:])
    #             # if row[0] in menu.keys():
    #             #     menu[row[0]].update(dict(zip(item, item)))
    #             # else:
    #             #     menu[row[0]] = dict(zip(item, item))
    #         print_menu()

    # except (IndexError, FileNotFoundError):
    #     raise Exception('Err: Check file path, ensure CSV format')


def core():
    """
    This function drives the app.
    All input is routed here and used to run the appropriate functions.
    It is the backbone of the program
    """
    global menu_set
    global default_menu
    global menu
    greet()
    menu_select()

    while True:

        prompt = str(input(f'''{chr(8811)}   ''')).lower()

        if prompt == 'quit':
            exit()

        if menu_set is False:

            if prompt == 'see menu':

                menu = default_menu
                menu_set = True
                print_menu()
                print('Enter \'menu\' again any time to look at the menu.')
                take_order()

            elif prompt == 'load menu':

                print('Please enter the path of an CSV file')
                path = input('> ')
                load_external_menu(path)
                menu_set = True

        # if the item is on the menu:
        for cat, value in menu.items():
            if (prompt.split(' ')[0].lower()) in (menu[cat].keys()):

                order.modify_order(prompt)

        if prompt == 'menu':
            print_menu()

        if prompt == 'order':
            if initial_order is False:
                order.display_order()

        if prompt == '':
            pass


def exit():
    '''
    exits the app
    '''
    print(dedent('''
        Thanks for ssssssssstopping by!
    '''))
    sys.exit()


if __name__ == '__main__':
    '''
    run : core
    keu exit : polite
    '''
    try:
        core()
    except KeyboardInterrupt:
        exit()
