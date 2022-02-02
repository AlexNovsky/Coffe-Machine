from menu import Menu, menu_list
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
    '''
    Importing page object classes to our main script
    '''

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
    '''
    Defining variables to imported classes to use class methods with arguments in main script
    '''
is_on = True
    '''
    If is_on is True, continue execution of the main script until is_on = True. 
    Defining is_on as a variable at the very beginning of executable part. 
    '''
while is_on:
    menu_item = input(f"What would you like to order? {menu.get_items()}\n").lower()
    '''
    Getting user's choice according menu and lowering input to simplify script work with menu_item variable
    :off - terminating script and exiting
    :report - printing report of remaining resources and money, Coffee machine earned during current session
    :sufficient menu_item - continuing script of Coffee machine 
    '''
    if menu_item == "off":
        print("Turning Coffee machine off.\nGood bye!")
        is_on = False
        '''
        Stopping script by assigning False statement to is_on variable
        '''
    elif menu_item == "report":
        print("Here is your resources and money report:")
        coffee_maker.report()
        money_machine.report()
        '''
        Calling method report from coffe_maker and money_machine classes
        '''
    else:
        if menu_item not in menu_list or not menu_item.isalpha():
            '''
            - Checking that entered item in menu_list, defined as a list in menu PO
            - Checking that entered menu_item is alphabetic, do avoid unexpected termination of script due
             to the invalid format of entered menu_item. Users are so users, you know =) 
            '''
            print(f"Your choice is '{menu_item}'.\nSorry that item is not available.\nTry again!")
        else:
            drink = menu.find_drink(menu_item)
            '''
            If checking passed and menu_item is in menu_list, proceeding with the execution and defining drink variable 
            '''
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            '''
            - checking if we have resources for the user's choice, is entered coins enough to pay for the drink
            - making drink, subtract resources and returning change
            - keeping script in a loop 
            '''