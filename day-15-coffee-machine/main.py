MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 1000,
    "milk": 500,
    "coffee": 250,
    "money": 0.0,
}
class MachineOff(Exception): pass

def get_input(user_input):
    if user_input.lower() == "off":
        raise MachineOff
    elif user_input.lower() == "report":
        print_report()
    elif user_input.lower() in MENU:
        if check_sufficient_resources(user_input):
            if process_payment(user_input): #If payment successful then make the drink.
                make_drink(user_input)
            return
        else:
            print("Can't make drink")
            return
    else:
        print("You typed some nonsense. Try again.")

    return

def process_payment(selected_drink):
    """Simulates taking money, returns True if user pays enough for the drink. Returns false if they don't"""
    global resources
    cost = MENU[selected_drink]["cost"]
    money_inserted = 0.0
    print(f"You chose {selected_drink.capitalize()}. That will be ${cost:.2f}")

    def give_change(given,required):
        """Calculates change to give as a float and returns it. Subtracts the change given from the machines resources"""
        change_to_give = float(given) - float(required)
        resources["money"] -= change_to_give
        return change_to_give

    transacting = True
    while transacting:
        user_input = input("Simulate entering coin. Enter coin value as float. Enter 'F' when done.\n")

        if user_input.lower() == "f":
            print(f"Transaction ended.")
            if money_inserted < cost :
                give_change(float(money_inserted), 0.0)
                print(f"You didn't pay enough. Refunding: ${money_inserted:.2f}")
            transacting = False
        else:
            try:
                value = float(user_input)
                money_inserted += value
                resources["money"] += value

                if money_inserted < cost:
                    print(f"${money_inserted:.2f} / {cost:.2f}")
                elif money_inserted == cost:
                    print(f"${money_inserted:.2f} / {cost:.2f}")
                    transacting = False
                    return True
                elif money_inserted > cost:
                    print(f"${money_inserted:.2f} / {cost:.2f}")
                    transacting = False
                    print(f"${give_change(money_inserted, cost):.2f} change given.")
                    return True
            except ValueError:
                print("Please enter a valid or amount or enter 'F' to finish.")

    return False


def make_drink(selected_drink):
    print(f"Here is your {selected_drink.capitalize()}. Enjoy.")
    req_water = MENU[selected_drink]["ingredients"]["water"]
    req_milk = MENU[selected_drink]["ingredients"]["milk"]
    req_coffee = MENU[selected_drink]["ingredients"]["coffee"]

    resources["water"] = int(resources["water"]) - int(req_water)
    resources["milk"] = int(resources["milk"]) - int(req_milk)
    resources["coffee"] = int(resources["coffee"]) - int(req_coffee)

    return

def print_report():
    """Print a string that lists resources and quantities remaining."""
    print(f"Water remaining: {resources["water"]}ml.\n"
          f"Milk remaining: {resources["milk"]}ml.\n"
          f"Coffee Remaining: {resources["coffee"]}g.\n"
          f"Money: ${resources["money"]:.2f}")
    return

def print_drink_menu():
    """Print a string listing available drinks and their costs."""
    for drink in MENU:
        cost = float(MENU[drink]["cost"])
        print(f"{drink.capitalize()}: ${cost:.2f}")
    return

def check_sufficient_resources(selected_drink):
    """Checks if there is sufficient resources for the selected_drink. Returns True if there is. Returns False if there is not."""
    if selected_drink not in MENU:
        print(f"{selected_drink} does not exist.")
        return False
    else:
        print(f"Checking {selected_drink}")
        avail_water = resources["water"]
        avail_milk = resources["milk"]
        avail_coffee = resources["coffee"]
        req_water = MENU[selected_drink]["ingredients"]["water"]
        req_milk = MENU[selected_drink]["ingredients"]["milk"]
        req_coffee = MENU[selected_drink]["ingredients"]["coffee"]

        if req_water > avail_water or req_milk > avail_milk or req_coffee > avail_coffee:
            if req_water > avail_water:
                print(f"Not enough water! {req_water}ml required, {avail_water}ml available.")
            if req_milk > avail_milk:
                print(f"Not enough milk! {req_milk}ml required, {avail_milk}ml available.")
            if req_coffee > avail_coffee:
                print(f"Not enough coffee! {req_coffee}g required, {avail_coffee}g available.")
            return False

        return True

def coffee_machine():
    print("Menu:")
    print_drink_menu()
    get_input(input("Hello, what would you like?\n"))

try:
    while True:
        coffee_machine()
except MachineOff:
    print("Machine turned off")