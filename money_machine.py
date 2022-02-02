import re
"""Importing RegEX for entered coins checking"""


class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    """
        Defining currency and coin's values in dollar's amount.
    """
    def __init__(self):
        self.profit = 0
        self.money_received = 0
    """
        Setting variables for starting point and report printing
    """

    def report(self):
        """ Prints the current profit """
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """
            :return:    Total calculated amount in CURRENCY
        """
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            while True:
                coins_recieved = input(f"How many {coin}?: ")
                if not re.match("^[0-9]+$", coins_recieved):
                    print("You entered invalid amount. Only numbers acceptable.")
                else:
                    break
                """
                    :return    Breaking the checking if user's input is a number and continue with next input
                               Looping user with error message and asking to reenter amount for current coin value  
                               
                    Getting user's input and validating with regex expression that user's input is a numbers only.
                    If input NOT a number
                """
            self.money_received += int(coins_recieved) * self.COIN_VALUES[coin]
            """
                Calculating user's input in CURRENCY for each coin and append values to get total amount in CURRENCY
            """
        return self.money_received

    def make_payment(self, cost):
        """
            :return:    True if payment is accepted
                        False if  payment is insufficient
        """
        self.process_coins()
        """ Getting total amount be calling corresponding method """
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            """
                Setting profit variable for report
                Setting total amount as 0 for the future orders
            """
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
