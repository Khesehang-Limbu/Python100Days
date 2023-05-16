MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_checker(user_coffee, resource):
    water = MENU[user_coffee]["ingredients"]["water"]
    coffee = MENU[user_coffee]["ingredients"]["coffee"]
    if water > resource["water"]:
        print("Insufficient Water")
        return False
    if coffee > resource["coffee"]:
        print("Insufficient Coffee")
        return False
    if MENU[user_coffee] == MENU["latte"] or MENU[user_coffee] == MENU["cappuccino"]:
        milk = MENU[user_coffee]["ingredients"]["milk"]
        if milk > resource["milk"]:
            print("Insufficient Milk")
            return False
    return True


def process_coins():
    quarters = float(input("Insert quarters : "))
    dimes = float(input("Insert dimes : "))
    nickels = float(input("Insert nickles : "))
    pennies = float(input("Insert pennies : "))

    dollars = 0.25 * quarters + 0.10 * dimes * 0.05 * nickels + 0.01 * pennies
    return dollars


def check_transaction(inserted_amount, cost):
    if inserted_amount < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${round(inserted_amount - cost, 2)} in change")
        return True


def report_generator(resource, funds):
    print(f'Water : {resource["water"]}ml')
    print(f'Milk : {resource["milk"]}ml')
    print(f'Coffee: {resource["coffee"]}gm')
    print(f'Money : ${round(funds, 2)}')


def coffee_maker(coffee, resource):
    cost = MENU[coffee]["cost"]
    resource["water"] -= MENU[coffee]["ingredients"]["water"]
    resource["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    if MENU[coffee] == MENU["latte"] or MENU[coffee] == MENU["cappuccino"]:
        resource["milk"] -= MENU[coffee]["ingredients"]["milk"]

    resources["water"] = resource["water"]
    resources["coffee"] = resource["coffee"]
    resources["milk"] = resource["milk"]
    print(f"Here is your {coffee}☕️., enjoy")
    global money
    money += cost


money = 0
is_machine_shut = False
# TODO 1. Print Report


while not is_machine_shut:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "report":
        report_generator(resources, money)
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        if resource_checker(user_choice, resources):
            user_amount = process_coins()
            if user_choice == "espresso" and check_transaction(user_amount, MENU[user_choice]["cost"]):
                coffee_maker(user_choice, resources)
            elif user_choice == "latte" and check_transaction(user_amount, MENU[user_choice]["cost"]):
                coffee_maker(user_choice, resources)
            else:
                if check_transaction(user_amount, MENU[user_choice]["cost"]):
                    coffee_maker(user_choice, resources)
    elif user_choice == "off":
        is_machine_shut = True
    else:
        print("Invalid Input, please type a valid input")
