from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order_menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

is_off = False
while not is_off:
    order = input(f"What would you like? ({order_menu.get_items()}): ")
    if order == "off":
        is_off = True
    elif order == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        coffee = order_menu.find_drink(order)
        if coffeeMaker.is_resource_sufficient(coffee) and moneyMachine.make_payment(coffee.cost):
            coffeeMaker.make_coffee(coffee)
            coffeeMaker.report()
            moneyMachine.report()



