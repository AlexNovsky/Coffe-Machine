from menu import Menu, MenuItem, menu_list
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    menu_item = input(f"What would you like to order? {menu.get_items()}\n").lower()
    if menu_item == "off":
        is_on = False
    elif menu_item == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if menu_item not in menu_list or not menu_item.isalpha():
            print(f"Your choice is '{menu_item}'.\nSorry that item is not available.\nGood bye!")
            is_on = False
        #
        # if menu_item != "latte" and menu_item != "espresso" and menu_item != "cappuccino":
        #     print("Sorry that item is not available.\nGood bye!")
        #     is_on = False
        # elif not menu_item.isalpha():
        #     print("Sorry that item is not available.\nGood bye!")
        #     is_on = False
        else:
            drink = menu.find_drink(menu_item)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
