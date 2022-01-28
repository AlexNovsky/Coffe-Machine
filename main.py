from menu import Menu, menu_list
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    menu_item = input(f"What would you like to order? {menu.get_items()}\n").lower()
    if menu_item == "off":
        print("Turning Coffee machine off.\nGood bye!")
        is_on = False
    elif menu_item == "report":
        print("Here is your resources and money report:")
        coffee_maker.report()
        money_machine.report()
    else:
        if menu_item not in menu_list or not menu_item.isalpha():
            print(f"Your choice is '{menu_item}'.\nSorry that item is not available.\nTry again!")
        else:
            drink = menu.find_drink(menu_item)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
