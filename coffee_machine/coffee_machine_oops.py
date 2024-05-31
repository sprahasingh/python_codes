from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while True:
    coffee_options = menu.get_items()
    coffee_type = input(f"“What would you like? {coffee_options}:\n").lower()
    if coffee_type == 'off':
        exit()
    elif coffee_type == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        coffee_details = menu.find_drink(coffee_type)
        if coffee_maker.is_resource_sufficient(coffee_details):
            if money_machine.make_payment(coffee_details.cost):
                coffee_maker.make_coffee(coffee_details)
