import csv

# LECTURE 17 Exercise

# Objectives
# 1. Decompose Real-world thing (a menu) into multiple objects
# 2. Work with multiple Classes
# 3. Call chained class methods
# 4. Read/write files

# Classes
# Menu: collection of MenuCategory objects
# MenuCategory: menu subsection; collection of MenuItem objects
# MenuItem: menu item comprising Dish and price
# Dish: food dish
# MenuMaker (utility): creates Menu from CSV sourced data

# Jamaican Jerk Pit menu
# https://www.jamaicanjerkpit.com/menu/
# Source for additional Jamaican dishes
# https://jamaicans.com/10-dishes-every-jamaican-should-know-how-to-cook/

class Menu:
    """Represents a restaurant menu.

    Attributes:
        name: name of menu
        categories: menu categories

    Methods:
        __init__: initialize a new Menu instance
        add_category: add MenuCategory object
        add_categories: bulk add MenuCategory objects
        delete_category: delete MenuCategory
        update_category: update MenuCategory object
        __str__: provide informal string representation of menu
    """

    def __init__(self, name):
        """Initialize Menu instance.

        Parameters:
            name (str): menu name or title
            categories (list): MenuCategory objects

        Returns:
            None
        """

        self.name = name
        self.categories = []



    def get_category(self, name):
        """Return Category object.

        Parameters:
            name (str): Category name

        Returns:
            Category: returns object
        """

        for category in self.categories:
            if category.name.lower() == name.lower():
                return category


    def add_category(self, category):
        """Accepts a MenuCategory object and adds the category to
        the menu.

        Parameters:
            category (MenuCategory): menu category object

        Returns:
            None
        """

        self.categories.append(category)



    def add_categories(self, categories):
        """Accepts a list of MenuCategory objects and adds them
        to the menu (bulk add).

        Parameters:
            categories (list): list of MenuCategory objects

        Returns:
            None
        """

        for category in categories:
            self.add_category(category)


    def update_category(self, updates):
        """TODO"""
        pass


    def delete_category(self, category):
        """TODO"""
        pass


    def __str__(self):
        """Dunder method providing an informal (pretty) string
        representation of the Menu object in its current state.

        Parameters:
            None

        Returns
            str: string representation of the menu
        """

        string = f"{self.name.upper()}\n"
        for category in self.categories:
            string += category.__str__()

        return string


class MenuCategory:
    """Represents a subsection of a restaurant menu.

    Attributes:
        name: name of category
        display_name: name to display on menu
        items: list of menu items

    Methods:
        __init__: initialize a new MenuCategory instance
        get_item: get MenuItem
        add_item: add MenuItem
        add_items: bulk add MenuItem objects
        delete_item: delete MenuItem object
        update_item: update MenuItem object
        __str__: provide informal string representation of MenuCategory
    """

    def __init__(self, name, display_name):
        """Initialialize MenuCategory instance.

        Parameters:
            name (str): name of category
            short_name (str): name to display on menu
            items (list): list of MenuItem objects

        Returns:
            None
        """

        self.name = name
        self.display_name = display_name
        self.items = []


    def get_item(self, dish):
        """Return MenuItem object.

        Parameters:
            dish (Dish): Dish (item)

        Returns:
            MenuItem: returns object
        """

        for item in self.items:
            if item.dish.name.lower() == dish.name.lower():
                return item


    def add_item(self, menu_item):
        """Accepts a MenuItem object and adds the item to
        the menu.

        Parameters:
            menu_item (MenuItem): menu item instance

        Returns:
            None
        """

        self.items.append(menu_item)


    def add_items(self, menu_items):
        """Accepts a list of menu item objects and adds them
        to the menu (bulk add).

        Parameters:
            menu_items (list): list of MenuItem objects

        Returns:
            None
        """

        for item in menu_items:
            self.add_item(item) # call add_item() method


    def delete_item(self, dish):
        """Deletes a MenuItem based on its Dish name.

        Parameters:
            dish (Dish): Dish object

        Returns:
            None
        """

        for item in self.items:
            if item.dish.name.lower() == dish.name.lower():
                self.items.remove(item)
                break


    def update_item(self, dish, updates):
        """Update MenuItem based on Dish name.

        Parameters:
            dish (Dish): Dish object
            updates (dict): update values

        Returns:
            None
        """

        for item in self.items:
            if item.dish.name.lower() == dish.name.lower():
                for key, val in updates.items():
                    if key == 'name':
                        item.dish.name = val
                    elif key == 'description':
                        item.dish.description = val
                    elif key == 'category':
                        item.category = val
                    elif key == 'price':
                        try:
                            item.price = float(val)
                        except ValueError:
                            continue
                    else:
                        continue
                break


    def __str__(self):
        """Provides an informal string representation of the
        MenuItem object in its current state.

        Parameters:
            None

        Returns
            str: string representation of the dish
        """

        string = f"{self.display_name.upper()}\n"
        for item in self.items:
            string += f"{item.__str__()}"

        return string


class MenuItem:
    """A representation of a menu item.

        Attributes:
            dish: dish object (item)
            price: item price

        Methods:
            __init__: initialize a new menu item instance
    """

    def __init__(self, dish, price):
        """Initialialize MenuItem instance.

        Parameters:
            dish (Dish): dish object (item)
            price (float): item price

        Returns:
            None
        """

        self.dish = dish
        self.price = float(price)



    def __str__(self):
        """Provides an informal string representation of the
        MenuItem object in its current state.

        Parameters:
            None

        Returns
            str: string representation of the dish
        """

        string = f"{self.dish.name} ${self.price:.2f}\n"
        if self.dish.description:
            string += f" {self.dish.description}.\n"
        string += "\n"

        return string


class Dish:
    """Represents a food dish.

    Attributes:
        name: name of dish
        description: short description of dish

    Methods:
        __init__: initialize an instance
        __str__: provide informal string representation
    """

    def __init__(self, name, description=None):
        """Initialize Dish instance.

        Parameters:
            name (str): name of dish
            description (str): short description of dish

        Returns:
            None
        """

        self.name = name
        self.description = description


    def __str__(self):
        """Provides an informal string representation of the
        Dish object in its current state.

        Parameters:
            None

        Returns
            str: string representation of the dish
        """
        string = f"{self.name}."
        if self.description:
            string = string + f" {self.description}."

        return string


class MenuMaker:
    """TODO"""

    def __init__(self, data):
        """Initialize instance.

        Parameters:
            data (list): data sourced externally

        Returns:
            None
        """

        self.data = data


    def create_menu(self, name, categories):
        """Create menu, populating with items provided from external source.

        Parameters:
            name (str): menu name
            categories (list): menu categories

        Returns:
            menu (Menu): Menu object populated with MenuItem objects
            categories (list): menu categories
        """

        menu = Menu(name) # initialize Menu
        menu.add_categories(categories)

        for row in self.data:
            item = MenuItem(Dish(row[0], row[2]), row[3])
            menu.get_category(row[1]).add_item(item) # method chaining

        return menu



def read_csv(path, delimiter=','):
    """Accepts a path, creates a file object, and returns a list of
    the file contents, line by line. Utilizes built-in enumerate()
    to filter out headers line.

    Parameters:
        path (str): path to file
        delimiter (str): delimiter that overrides the default delimiter

    Returns:
        list: nested lists representing the file contents
     """

    with open(path, 'r', newline='', encoding='utf-8') as csv_file:
        data = []
        reader = csv.reader(csv_file, delimiter=delimiter)
        for i, line in enumerate(reader):
            if i > 0:
                data.append(line)

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


def main():
    """Entry point of program. Calls MenuMaker to create initial Menu from
    data sourced from CSV files. Calls Menu methods in order to add, update,
    and delete MenuItem objects and then writes Menu to file.

    Parameters:
        None

    Returns:
        None
    """

    # 1.0 GET CSV DATA
    path = 'jerk_pit.csv'
    data = read_csv(path)

    # 1.1 CREATE MENU
    menu_name = 'Jamaican Jerk Pit Menu'
    menu_categories = [
        MenuCategory('Starter', 'Calypso Starters'),
        MenuCategory('Greens', 'Caribbean Greens'),
        MenuCategory('Entree', 'Island Style Entrees'),
        MenuCategory('Side', 'Sides'),
        MenuCategory('Dessert', 'Dessert')
        ]

    menu = MenuMaker(data).create_menu(menu_name, menu_categories)

    # 1.2 ADD MENU ITEM
    # https://jamaicans.com/10-dishes-every-jamaican-should-know-how-to-cook/

    dish = Dish(
        'Ackee and Saltfish',
        'Sautéed saltfish (codfish) with boiled ackee'
        )
    menu_item = MenuItem(dish, 12.50)

    print(f"\nNew menu item\n{menu_item.__str__()}")

    menu.get_category('Entree').add_item(menu_item)

    # 1.3 ADD MENU ITEMS
    # https://jamaicans.com/10-dishes-every-jamaican-should-know-how-to-cook/

    porridge = MenuItem(
        Dish('Cornmeal porridge'),
        2.0
    )
    soup = MenuItem(
        Dish(
            'Red Peas Soup',
            'Rich Jamaican soup that features beef, pig tails, gungo peas, and yellow yam'
        ),
        3.5
    )
    menu.get_category('Starter').add_items([soup, porridge])

    # 1.4 UPDATE MENU ITEM
    # Plantains special $2.50 (was $5.00)
    plantains = menu.get_category('Starter').get_item(Dish('Fried Plantains'))

    print(f"\n Fried Plantains regular price = ${plantains.price:,.2f}\n")

    menu.get_category('Starter').update_item(Dish('Fried Plantains'), {'price': 2.5})

    # 1.5 DELETE MENU ITEM
    menu.get_category('Starter').delete_item(Dish('Jerk Wings'))

    # 1.6 PRINT TO SCREEN
    print(f"\n{menu.name}\n{menu.__str__()}\n")

    # 1.7 WRITE MENU TO FILE
    path = 'jerk_menu.txt'
    write_file(path, menu.__str__())

if __name__ == '__main__':
    main()