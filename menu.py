menu_list = ["latte", "espresso", "cappuccino"]
"""
    Defining menu_list for checking user's input at the first verification of user's choice
"""

class MenuItem:
    """
        Models menu with all needed arguments
    """
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """
        Defining menu items and ingredients for each item in menu
    """

    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """
            :return: items names as a string for printing to the user
            Could be changed in menu class at any time without interrupting whole functionality
        """
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """
            Searches entered item in menu by name, returning item name as argument
        """
        for item in self.menu:
            if item.name == order_name:
                return item
