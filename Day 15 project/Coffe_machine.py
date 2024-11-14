from main import MENU
from main import resources


def check_resources(choice):
    drink = MENU[choice]["ingredients"]
    for ingredient, amount_needed in drink.items():
        if resources.get(ingredient, 0) < amount_needed:
            print(f"Not enough {ingredient} to make {choice}.")
            return False
    return True


def update_resources(choice):
    drink = MENU[choice]["ingredients"]
    for ingredient, amount_needed in drink.items():
        resources[ingredient] -= amount_needed


def money(choice):

    cost = MENU[choice]["cost"]
    if not check_resources(choice):
        return

    print(f"That will be {cost} shekels")

    total_money_inserted = 0

    while total_money_inserted < cost:
        print("Please insert coins:")
        one_shekel = int(input("How many 1-shekel coins? ")) * 1
        two_shekel = int(input("How many 2-shekel coins? ")) * 2
        five_shekel = int(input("How many 5-shekel coins? ")) * 5
        ten_shekel = int(input("How many 10-shekel coins? ")) * 10

        round_total = one_shekel + two_shekel + five_shekel + ten_shekel
        total_money_inserted += round_total

        if total_money_inserted < cost:
            print(f"Not enough money. You need {cost - total_money_inserted} more shekels.")
        elif total_money_inserted > cost:
            change = total_money_inserted - cost
            print(f"Payment accepted! Your change is {change} shekels.")
        else:
            print("Payment accepted! No change required.")


    update_resources(choice)


def print_costs(menu):

    print("Drink Prices:")
    for drink, details in menu.items():
        cost = details["cost"]
        print(f"{drink.capitalize()}: {cost} shekels")


def print_report():
    print("Resource Report:")
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")


def main():

    print_costs(MENU)

    while True:
        choice = input("What would you like? (espresso/latte/cappuccino) or type 'report' to see resources:\n").lower()

        if choice == "report":
            print_report()
        elif choice in ["espresso", "latte", "cappuccino"]:
            print(f"You chose {choice}.")
            money(choice)
        elif choice == "-1":
            break
        else:
            print("Invalid choice. Please try again.")


main()
