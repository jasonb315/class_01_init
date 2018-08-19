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
import uuid
# prompt = input(f'''{chr(3847)} ''')

WIDTH = 96

no = {'no', 'n', 'nay', 'no thanks', 'jog on mate', 'that\'s all', 'nope'}
yes = {'yes', 'y', 'ye', 'sure', 'fuck yeah dawg', 'please', ''}

SPE = {
    '01': 'Ready to order? what can I get ya?\n',
    '02': 'Anyting else?\n',
}

ordering = True

# MENU dic, SECTION dic, key item : vals being count and price
MENU = {}

D_MENU = {

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


class Order:
    def __init__(self):
        self.receipt = {'subtotal': 0}
        self.id = str(uuid.uuid4())

    def __repr__(self):
        return f'''Order: {self.id} | Items: {self.receipt['subtotal']} | Total: {len(self.receipt)}'''

    def __len__(self):
        return len(self.receipt)

    def add_item(self, item, quantity):
        try:
            flag = False
            for key, value in MENU.items():
                if item in MENU[key]:
                    flag = True
                    stock = MENU[key][item]['stock']
                    if quantity < int(stock):
                        MENU[key][item]['stock'] -= 1
                        if item in current.receipt:
                            current.receipt[item] += quantity
                            total = _get_subtotal(item)
                            print(f'''{current.receipt[item]} orders of {item} has been added to your order. Your total is $ {total}''')
                        else:
                            current.receipt[item] = 1
                            total = _get_subtotal(item)
                            print(f'''{quantity} order of {item} has been aded to your order. Your roral is ${total}''')
                    else:
                        print('Sorry, we don\'t have that many.')
            if flag is False:
                raise KeyError('404, food not found.')
        except(TypeError, KeyError):
            raise KeyError('We don\'t, sell that.')

    def remove_item(self, item, quantity):
        for key, value in MENU.items():
                if item in MENU[key]:
                    if item not in current.receipt:
                        raise ValueError('You haven\'t ordered any of those.')
                if current.receipt[item] == 1:
                    current.receipt['subtotal'] -= menu[key][item]['price']
                    del current.receipt[item]
                else:
                    current.receipt[item] -= quantity
                    current.receipt['subtotal'] -= MENU[key][item]['price'] * quantity
                total = round(current.receipt['subtotal'], 2)
                print(f'{quantity} order(s) of {item} has been removed from your meal. Your total is ${total}')

    def display_order(self, receipt):
        tax = round(_get_sales_tax(current.receipt['subtotal']), 2)

        for key, value in current.receipt.items():
            unit_cost = _calculate_line_item(key)
            if unit_cost is not None:
                print(unit_cost[0].ljust(40), '$', unit_cost[1] * current.receipt[key])
        print('-' * 50)
        print('Subtotal'.ljust(40), '$', round(current.receipt['subtotal'], 2))
        print('Sales Tax'.ljust(40), '$', tax)
        print('-' * 10)
        print('Total Due'.ljust(40), '$', str(float(round(current.receipt['subtotal'] + tax))), 2)
        print('*' * 50)

    def print_receipt(self, receipt):

        receipt_file = ''
        receipt_file += (f'''\n {'*' * 50} \n The Snakes Cafe \n Order: {self.id} \n {'=' * 50}''')

        subtotal = current.receipt['subtotal']
        for key, value in current.receipt.items():
            unit_cost = _calculate_line_item(key)
            if unit_cost is not None:
                # item = unit_cost[0]
                price = unit_cost[1]
                to_output = (f'''{key} x {value}''')
                receipt_file += ('\n{:<25} {:>25.2f}'.format(to_output, price))
        tax = subtotal * 0.096
        receipt_file += ('\n' + '-' * 50 + '\nSubtotal {:>42.2f}'.format(subtotal))
        receipt_file += ('\nSales Tax {:>41.2f}'.format(tax))
        receipt_file += ('\n' + '-' * 10 + '\nTotal Due {:>41.2f}\n'.format(subtotal + tax))
        with open(f'order-{current.id}.txt' + self.id + '.txt', 'w') as f:
            f.write(receipt_file)


current = Order()


def _import_menu(file_path):
    try:
        with open(file_path, 'r') as f:
            menu_import = csv.reader(f)
            for row in menu_import:
                item = iter(row[1:])
                #https://docs.python.org/3.5/library/functions.html#iter
                if row[0] in menu.keys():
                    menu[row[0]].update(dict(zip(item, item)))
                else:
                    menu[row[0]] = dict(zip(item, item))
            print_menu()

    except (IndexError, FileNotFoundError) as error:
        raise Exception('File not found or incorrect filetype; please use a CSV.')
        what_menu()


def what_menu():
    greeting()
    print('Would you like to import a menu?')
    menu_choice = input(f'''{chr(3847)}   ''')
    global yes
    if menu_choice.lower() in yes:
        print('What is the filepath?')
        file_path = input(f'''{chr(3847)}   ''')
        _import_menu(file_path)
    else:
        global MENU
        MENU = D_MENU
        print_menu()


def _get_subtotal(item):
    """
    This function gets the subtotal of all purchased items.
    """
    try:
        for key, value in MENU.items():
            if item in MENU[key]:
                current.receipt['subtotal'] += MENU[key][item]['price']
        return round(current.receipt['subtotal'], 2)
    except TypeError:
        print('*points out window* Oh hey what\'s that! *runs away*')


def _get_sales_tax(subtotal):

    tax = subtotal * 0.101
    return tax


def _calculate_line_item(item):
    """
    This function gets each line item and its cost from the main menu.
    Argument: An item
    Output: The item and its per-unit price as a tuple
    """
    for key, value in MENU.items():
        if item in MENU[key]:
            item_name = item
            unit_cost = MENU[key][item]['price']
            return(item_name, unit_cost)


def greeting():
    '''
    Fx will print conversational greeting to the user when opening script.
    '''

    ln_one = 'Hey there! Welcome to sssssSneksss Cafe!'
    ln_two = 'Have a ssseat!'

    print(dedent(f'''
        {'*' * WIDTH}
        {(' ' * ((WIDTH - len(ln_one)) // 2)) + ln_one +
            (' ' * ((WIDTH - len(ln_one)) // 2))}
        {(' ' * ((WIDTH - len(ln_two)) // 2)) + ln_two +
            (' ' * ((WIDTH - len(ln_two)) // 2))}
        {'*' * WIDTH}

    '''))


# def ask_question(question):
#     return input(question)


def check_input(user_in):
    global ordering

    if user_in.lower() == 'quit' or user_in.lower() == 'leave':
        exit()
        return

    elif user_in.lower() == 'menu':
        print_menu()
        return

    if ordering is True:
        found = False
        for cat in MENU:
            for food in MENU[cat]:
                if user_in.lower() == food.lower():
                    MENU[cat][food]['ordered'] += 1
                    print(f'''Alrighty, that's {MENU[cat][food]['ordered']} {food}''')
                    found = True
                    break
        if found is False:
            print('Sorry, what was that?')

        found = False

    if user_in.lower() in no:
        ordering = False
        Order.display_order(current.receipt)


def exit():
    print(dedent('''
        Thanks for ssssssssstopping by!
    '''))
    sys.exit()


def print_menu():

    for cat, value in MENU.items():
        print('')
        print(f'''{chr(8857)}   {cat}''')
        print('')
        for food in MENU[cat]:
            print(dedent(f'''{food}{'.' *
            (WIDTH - 1 -len(food) -
            len(str(MENU[cat][food]['price'])))}${MENU[cat][food]['price']}'''))
    print('')
    take_order()


def take_order():
    global ordering
    global no

    initial_order = True

    while ordering:
        if initial_order:
            print(SPE['01'])
            check_input(input(f'''{chr(3847)}   '''))
            initial_order = False
        else:
            print(SPE['02'])
            check_input(input(f'''{chr(3847)}   '''))


def run():
    what_menu()
    print_menu()

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        exit()
