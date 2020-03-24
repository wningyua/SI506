import csv

# LECTURE 16

# Objectives
# 1. Explore a Python Class and its attributes and methods
# 2. Distinguish between class and instance variable
# 3. Learn how to initialize a class instance with __init__
# 4. Understand purpose of 'self' keyword
# 5. Call class methods
# 6. Implement try/except block to catch ValueError exceptions
# 7. Read/write files using DictReader()/DictWriter()


class Menu():
    """Represents a restaurant menu (a custom type).

    Attributes:
        name: name of menu
        item: menu entree and optional side dish
        items: collection of menu items

    Methods:
        __init__: initialize a new menu instance
        add_item: add to instance an entree and optional side
        add_dict_item: add to instance an entree/optional side dict
        add_items: bulk add to instance a list of entree/optional side strings
        add_dict_items: bulk add to instance a list of entree/optional dicts
        delete_item: delete instance item
        update_item: update instance item
        __str__: provide informal string representation of the instance
    """

    default_side = 'spam' # class variable

    def __init__(self, name):
        """Initialize instance. Set name value.

        Parameters:
            name (str): menu name or title

        Returns:
            None
        """

        # Instance variables
        self.name = name
        self.item = {'entree': None, 'side': None} # dict literal
        self.items = []


    def add_item(self, entree, side=None):
        """Accepts a string representation of an entree and, if
        provided, an optional side dish, and adds the item to
        the menu in the form of a dictionary.

        Parameters:
            entree (str): main menu item
            side (str): optional side dish

        Returns:
            None
        """

        self.items.append({'entree': entree, 'side': side})


    def add_dict_item(self, item):
        """Accepts a dictionary representing an entree and, if
        provided, an optional side dish, and adds the dictionary
        to the menu.

        Parameters:
            item (dict): main menu item and optional side dish

        Returns:
            None
        """

        self.items.append(item)


    def add_items(self, items):
        """Accepts a list of menu items, each represented as a list
        of strings, and adds them to the menu (bulk add).

        items format: [[<'entree'>, <'side'>],...]

        Parameters:
            items (list): list containing nested lists of menu items

        Returns:
            None
        """

        for item in items:
            if item[1]: # have optional side
                self.add_item(item[0], item[1])
            else:
                self.add_item(item[0])
                # self.add_item(item[0], self.default_item) # class variable


    def add_dict_items(self, items):
        """Accepts a list of menu items, each represented as a
        dictionary, and adds them to the menu (bulk add).

        items format: [{'entree': entree, 'side': side},...]

        Parameters:
            items (list): list containing nested lists of menu items

        Returns:
            None
        """

        for item in items:
            self.items.append(item)


    def delete_item(self, item):
        """Accepts a menu item and deletes it.

        Parameters:
            item (dict): entree and optional side dish

        Returns:
            None
        """

        if item in self.items:
            self.items.remove(item)


    def update_item(self, item, entree, side=None):
        """Accept a menu item to be updated with strings
        representing an entree and, if provided, an optional
        side dish.

        Parameters:
            item (dict): entree and optional side dish to be updated
            entree (str): new entree
            side (str): new side dish, if provided

        Returns:
            None
        """

        index = self.items.index(item)
        self.items[index] = {'entree': entree, 'side': side}


        # try:
        #     index = self.items.index(item)
        #     self.items[index] = {'entree': entree, 'side': side}
        # except ValueError:
        #     msg = '\nError: '
        #     if item['side']:
        #         msg += f"{item['entree']} + {item['side']}"
        #     else:
        #         msg += {item['entree']}
        #     msg += " is not on the menu.\n"

        #     print(msg)


    def __str__(self):
        """Provides an informal (pretty) string representation of the
        menu object in its current state.

        Definition: This method is known as a "dunder" (double
        underscore) method. It emulates the behavior of a pre-defined
        built-in method (e.g., __init__()).

        Parameters:
            None

        Returns
            str: string representation of the menu
        """

        string = ''
        for item in self.items:
            for key, val in item.items():
                if key == 'entree':
                        string += val
                else:
                    if not val:
                        string += '\n'
                    else:
                        string += f" + {val}\n"

        return string
        # return string.upper() # match menu image


def read_csv(path, delimiter=','):
    """Accepts a path, creates a file object, and returns a list of
    the file contents, line by line.

    Parameters:
        path (str): path to file
        delimiter (str): delimiter that overrides the default delimiter

    Returns:
        list: nested lists representing the file contents
     """

    with open(path, 'r', newline='', encoding='utf-8') as csv_file:
        data = []
        reader = csv.reader(csv_file, delimiter=delimiter)
        for i, line in enumerate(reader): # good point for skipping the header
            if i > 0:            # ignore header line
                data.append(line)

        return data


def read_csv_as_dict(path, delimiter=','):
    """Accepts a path, creates a file object, and returns a list of
    dictionaries that represent the row values.

    Parameters:
        path (str): path to file
        delimiter (str): delimiter that overrides the default delimiter

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(path, 'r', newline='', encoding='utf-8') as csv_file:
        data = []
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        for line in reader:
            data.append(line) # OrderedDict()
            # data.append(dict(line)) # convert OrderedDict() to dict

        return data


def write_file(path, data):
    """Accepts a path, creates a file object, and returns a list of
    dictionaries that represent the row values.

    Parameters:
        path (str): path to file
        delimiter (str): delimiter that overrides the default delimiter

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(path, 'w', newline='', encoding='utf-8') as file_obj:
        # file_obj.write(data)
        # file_obj.writelines(data)

        for row in data:
            file_obj.write(row)


def write_csv_from_dict(path, data, fieldnames):
    """TODO"""

    with open(path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader() # first row
        for row in data:
            writer.writerow(row)


def main():
    """Entry point of program. Initializes Menu instances and calls Menu
    methods in order to modify Menu state. Calls file read/write methods
    to bulk add menu items to a Menu instance and save a copy of the current
    state of a Menu instance to a file.

    Parameters:
        None

    Returns:
        None
    """


    # 1.0 INSTANTIATE NEW MENU INSTANCE
    menu_v1 = Menu('MENU 1.0')

    # 1.1 BULK ADD ITEMS (list of strings)
    path = 'spam.csv'
    items = read_csv(path)

    print(f"\nMENU 1.0 items\n{items}\n")

    menu_v1.add_items(items) # populate menu

    # 1.2 ADD NEW ITEMS INDIVIDUALLY
    menu_v1.add_item('egg')
    menu_v1.add_item('oatmeal yogurt fruit plate', 'spam')

    # 1.3 PRINT STRING REPRESENTATION OF MENU INSTANCE
    print(f"\n{menu_v1.name} + 2 items\n{menu_v1.__str__()}\n")

    # 1.4 UPDATE ITEM
    item = {'entree': 'egg', 'side': None}
    menu_v1.update_item(item, 'egg hash browns toast', 'spam')

    # UNCOMMENT Update non-existent item (demo try/except)
    # item = {'entree': 'cereal', 'side': 'toast'}
    # menu_v1.update_item(item, 'pancakes', 'spam')

    # 1.5 PRINT STRING REPRESENTATION OF MENU INSTANCE
    print(f"\n{menu_v1.name} + updated item\n{menu_v1.__str__()}\n")

    # 1.6 WRITE MENU TO FILE
    path = 'menu_1.txt'
    # write_file(path, menu_v1.__str__())

    # write_file(path, menu_v1.items) # TypeError arg must be str not dict


    # 2.0 INSTANTIATE NEW MENU INSTANCE
    menu_v2 = Menu('MENU 2.0')

    # 2.1 READ IN CSV ROWS AS DICTS (cool)
    path = 'spam.csv'
    items = read_csv_as_dict(path)

    print(f"\nMENU 2.0 items\n{items}\n")

    menu_v2.add_dict_items(items) # populate menu

    # 2.1 ADD DICT ITEMS INDIVIDUALLY
    menu_v2.add_dict_item({'entree': 'pancakes sausage', 'side': 'spam'})
    menu_v2.add_dict_item({'entree': 'waffles strawberries whipped cream', 'side': None})

    # 2.2 DELETE ITEM
    item = {
        'entree': 'Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top',
        'side': 'spam'
        }
    menu_v2.delete_item(item)

    # 2.3 PRINT STRING REPRESENTATION OF MENU INSTANCE
    print(f"\n{menu_v2.name} + 2 items - Lobster\n{menu_v2.__str__()}\n")

    # 2.4 WRITE MENU TO FILE
    path = 'menu_2.csv'
    write_csv_from_dict(path, menu_v2.items, ('entree','side'))


    #3.0 INSTANTIATE NEW MENU INSTANCE
    menu_v3 = Menu('MENU 3.0')

    # 3.1 READ IN CSV ROWS AS DICTS (cool)
    path = 'coneys.csv'
    items = read_csv_as_dict(path)

    print(f"\nMENU 3.0 items\n{items}\n")

    menu_v3.add_dict_items(items) # populate menu

    # 3.2 ADD DICT ITEMS INDIVIDUALLY
    menu_v3.add_item('new york-style chili dog', 'fries')
    menu_v3.add_item('new york-style chili cheese dog', 'fries')

    # 3.3 PRINT STRING REPRESENTATION OF MENU INSTANCE
    print(f"\n{menu_v3.name} + 2 items\n{menu_v3.__str__()}\n")

    # 3.4 DELETE ITEM
    item = {'entree': 'kalamazoo-style coney', 'side': 'fries'}
    menu_v3.delete_item(item)

    # 3.5 PRINT STRING REPRESENTATION OF MENU INSTANCE
    print(f"\n{menu_v3.name} minus Kzoo\n{menu_v3.__str__()}")

    # 3.6 WRITE MENU TO FILE
    path = 'menu_3.csv'
    # write_csv_from_dict(path, menu_v3.items, ('entree','side'))


if __name__ == '__main__':
    main()