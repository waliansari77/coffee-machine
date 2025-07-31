Menu = {
"espresso":{
        "ingredients":{
            "water":50,
            "milk":0,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
    "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }
}

resources = {
    "water":300,
    "milk":200,
    "coffee":100,
}

profit = 0

def report ():
    return f" water: {resources["water"]}ml\n milk: {resources["milk"]}ml\n coffee: {resources["coffee"]}g\n Money: ${profit}"

def process_coins(quarters,dimes,nickles,pennies):
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total

Machine_On = True
while Machine_On:
    user = input("What would you like? (espresso/cappuccino/latte): ").lower()

    if user in Menu:

        drink = Menu[user]["ingredients"]

        if resources["water"] <= Menu[user]["ingredients"]["water"]:
            print("Sorry there is not enough Water!")
        elif resources["milk"] <= Menu[user]["ingredients"]["milk"]:
            print("Sorry there is not enough Milk!")
        elif resources["coffee"] <= Menu[user]["ingredients"]["coffee"]:
            print("Sorry there is not enough Coffee!")
        else:
            print("Please insert coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))

            total_calculate = process_coins(quarters, dimes, nickles, pennies)

            item = Menu[user]
            if total_calculate < item["cost"]:
                print(f"Sorry that's not enough money. Money refunded.")
            else:
                change = total_calculate - item["cost"]

                resources["milk"] -= item ["ingredients"]["milk"]
                resources["coffee"] -= item ["ingredients"]["coffee"]
                resources["water"] -= item ["ingredients"]["water"]
                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {user}☕ enjoy!")
                profit += item["cost"]

    elif user == "report":
        print(report())
    elif user == "off":
        Machine_On = False
        print("Thank you for your time. Goodbye!")

    else:
        print(f"Coffee not found in the menu!")




