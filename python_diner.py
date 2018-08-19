# imports
from textwrap import dedent
import sys
import uuid
import csv


# globals
WIDTH = 66
menu_set = False
menu = {}
default_menu = {

    'APPETIZERSss':
        {
            'noms': {
                'price': 9.99,
                'stock': 10
            },
            'crickets': {
                'price': 9.99,
                'stock': 10
            },
            'mousebobs': {
                'price': 9.99,
                'stock': 10
            },
        },

    'ENTRESss':
        {
            'roadkill': {
                'price': 9.99,
                'stock': 10
            },
            'housecat': {
                'price': 9.99,
                'stock': 10
            },
            'infant': {
                'price': 9.99,
                'stock': 10
            },
        },

    'DESERTSss':
        {
            'micecream': {
                'price': 9.99,
                'stock': 10
            },
            'frogyo': {
                'price': 9.99,
                'stock': 10
            },
            'sssouffle': {
                'price': 9.99,
                'stock': 10
            },
        },

    'BEVERAGESss':
        {
            'water': {
                'price': 9.99,
                'stock': 10
            },
            'sssoda': {
                'price': 9.99,
                'stock': 10
            },
            'milksnake': {
                'price': 9.99,
                'stock': 10
            },
        },
}


class Order:
    def __init__(self):
        self.items = {}
        self.total = 0
        self.id = str(uuid.uuid4())

    def __repr__(self):
        return f'''Order: {self.id} | Items: {self.items} | Total: {self.total}'''

    def __len__(self):
        return len(self.items)

    def modify_order(self, order):

        print('in modify_order')
        try:
            item = str(order[0])
        except IndexError:
            print('I\'m sorry, what?')
            return
        try:
            quantity = int(order[1])
        except IndexError:
            print('One of those then?')
            quantity = 1

        # 'order' is an array [item, quantity]
        # I have the item I want and I know it's on the menu.
        # find it in stock and check amount.
        # If good, modify order for count and price

        if quantity == 0:
            print('I\'m sorry, how many?')
        else:
            # go through menu
            for cat, value in menu.items():
                for food in menu[cat]:
                    if item == food:
                        # ok we have attention to the menu item
                        # if subtracting from order
                        if quantity < 0:
                            # subtracting, check order for presence
                            if food in order.items:
                                # is present, check for overdraw, if ok make change to order and stock
                                if self.items[item] - quantity >= 0:
                                    # order shrinks
                                    self.items[item] += quantity
                                    # bill drops
                                    self.total += (quantity * menu[cat][food]['price'])
                                    # stock expands
                                    menu[cat][food]['stock'] -= quantity
                                    # feedback{
                                    print(f'''{abs(quantity)} {item} has been removed from your order.''')
                            else:
                                print('I\'m sorry, you haven\'t ordered any of those.')
                        # if adding to order
                        if quantity > 0:
                            # check stock
                            if (menu[cat][food]['stock'] - quantity) >= 0:
                                # make food
                                menu[cat][food]['stock'] -= quantity
                                # serve
                                self.items[item] = int(quantity)
                                print(self.items[item])
                                print(self.items)

                                # and bill
                                self.total += (quantity * menu[cat][food]['price'])


order = Order()


def take_order():

    initial_order = True

    if initial_order:
        initial_order = False
        print('Ready to order? what can I get ya?\n')

    else:
        print('Anyting else?\n')
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

    for cat, value in menu.items():
        print('')
        print(f'''{chr(8857)}   {cat}''')
        print('')
        for food in menu[cat]:
            print(dedent(f'''{food}{'.' *
            (WIDTH - 1 -len(food) -
            len(str(menu[cat][food]['price'])))}${menu[cat][food]['price']}'''))
    print('')


def menu_select():
    print('To see our menu, enter \'see menu\'.')
    print('Or to load a menu, enter \'load menu\'')


def load_external_menu(path):
    try:
        with open(path, 'r') as f:
            menu_import = csv.reader(f)
            for row in menu_import:
                menu[row[0]]
                # item = iter(row[1:])
                # if row[0] in menu.keys():
                #     menu[row[0]].update(dict(zip(item, item)))
                # else:
                #     menu[row[0]] = dict(zip(item, item))
            print_menu()

    except (IndexError, FileNotFoundError):
        raise Exception('Err: Check file path, ensure CSV format')


def core():
    global menu_set
    global default_menu
    global menu
    """
    This function drives the app.
    All input is routed here and used to run the appropriate functions.
    It is the backbone of the program
    """
    greet()
    menu_select()

    while True:

        prompt = str(input(f'''{chr(3847)}   ''')).lower()

        if prompt == 'quit':
            exit()

        if menu_set is False:

            if prompt == 'see menu':

                menu = default_menu
                menu_set = True
                print_menu()
                take_order()

            elif prompt == 'load menu':

                print('Please enter the path of an CSV file')
                path = input('> ')
                load_external_menu(path)
                menu_set = True

        # if the item is on the menu:
        for cat, value in menu.items():
            if (prompt.split(' ')[0].lower()) in (menu[cat].keys()):
                # print(value)
                # print(menu[cat].keys())
                # print('on the menu')
                # print(prompt.split(' ')[0].lower(), prompt.split(' ')[1])

                order.modify_order([prompt.split(' ')[0].lower(), prompt.split(' ')[1]])

        if prompt == '':
            pass

def exit():
    print(dedent('''
        Thanks for ssssssssstopping by!
    '''))
    sys.exit()


if __name__ == '__main__':
    try:
        core()
    except KeyboardInterrupt:
        exit()
