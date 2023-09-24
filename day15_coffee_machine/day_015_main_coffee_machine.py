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


############# MY SOLUTION ################

COINS = {
    'quarter': 0.25,
    'dime': 0.1,
    'nickles': 0.05,
    'pennies': 0.01}


maintenance = False

machineMoneySum = 0
machineCoins = [0, 0, 0, 0]

paymentCoinsSum = 0
paymentCoins = [0, 0, 0, 0]


# 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
def turnOff():
    """Changes the boolean and ends the while loop"""
    global maintenance
    maintenance = True
    print(f"Switching off for maintenance.")


# 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
def printReport():
    """Shows how many resources left"""
    print(f' Water: {resources["water"]}\n Milk: {resources["milk"]}\n Coffee: {resources["coffee"]}\n Money: ${machineMoneySum}\n')


# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “ Sorry there is not enough water. ”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
def checkResources(coffee):
    global resources
    machineWater = resources['water']
    machineMilk = resources['milk']
    machineCoffee = resources['coffee']
    orderWater = MENU[coffee]['ingredients']['water']
    orderCoffee = MENU[coffee]['ingredients']['coffee']

    if coffee == 'espresso':
        if machineWater > orderWater and machineCoffee > orderCoffee:
            return True
        else:
            return False
    elif coffee == 'latte' or coffee == 'cappuccino':
        orderMilk = MENU[coffee]['ingredients']['milk']
        if machineWater > orderWater and machineCoffee > orderCoffee and machineMilk > orderMilk:
            return True
        else:
            return False


# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def countCoins(price):
    global COINS
    global paymentCoins
    global paymentCoinsSum

    print(f"Please provide ${price} with inserting coins:\n"
          f"1: quarters (${COINS['quarter']})\n"
          f"2: dimes (${COINS['dime']})\n"
          f"3: nickles (${COINS['nickles']})\n"
          f"4: pennies (${COINS['pennies']})\n")

    continuePayment = True

    while price > paymentCoinsSum and continuePayment == True:
        print("For refund press 'M'")
        insertedCoin = input("Insert coins (1-4): ")
        if insertedCoin in ('m','M'):
            continuePayment == False
            paymentCoinsSum = 0
            paymentCoins = [0, 0, 0, 0]
            print("Coins refunded!")
            return
        elif insertedCoin in ('1','2','3','4'):
            insertedCoin = int(insertedCoin)-1
            paymentCoins[insertedCoin] += 1
            paymentCoinsSum = paymentCoins[0]*0.25 + paymentCoins[1]*0.1 + paymentCoins[2]*0.05 + paymentCoins[3]*0.01
            print(f"You've inserted: \n"
                  f"quarters: {paymentCoins[0]}\n"
                  f"dimes: {paymentCoins[1]}\n"
                  f"nickles: {paymentCoins[2]}\n"
                  f"pennies: {paymentCoins[3]}\n")
        else:
            print(f"Can't recognize the coin. The coin returned.\n")

        print(f"Inserted amount: ${round((paymentCoinsSum), 2)}. Required more: ${round((price-paymentCoinsSum), 2)}.")

    if paymentCoinsSum == price:
        print("Required amount payed!")
        return True
    elif paymentCoinsSum > price:
        print(f"Here is your change: ${round((paymentCoinsSum-price), 2)}")
        paymentCoinsSum = price
        return True
    else:
        print("Sorry, not enough inserted.")
        return False


# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “ Sorry that's not enough money. Money refunded. ”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.
def finishTransaction():

    global machineMoneySum
    global machineCoins
    global paymentCoins
    global paymentCoinsSum

    machineMoneySum += paymentCoinsSum
    machineCoins[0] += paymentCoins[0]
    machineCoins[1] += paymentCoins[1]
    machineCoins[2] += paymentCoins[2]
    machineCoins[3] += paymentCoins[3]

    paymentCoinsSum = 0
    paymentCoins = [0, 0, 0, 0]

    # print(machineMoneySum)
    # print(machineCoins)

# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
def makeCoffee(product):
    global resources
    # printReport()
    elements = len(product.keys())
    if elements == 2:
        resources['water'] -= product['water']
        resources['coffee'] -= product['coffee']
    elif elements == 3:
        resources['water'] -= product['water']
        resources['coffee'] -= product['coffee']
        resources['milk'] -= product['milk']
    # printReport()

# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.

while not maintenance:
    # Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    # a. Check the user’s input to decide what to do next.
    # b. The prompt should show every time action has completed, e.g. once the drink is
    # dispensed. The prompt should show again to serve the next customer.

    userChoice = input("What would you like? (espresso/latte/cappuccino): (E or L or C)\n").lower()
    if userChoice in ('e', 'espresso'):
        enoughResources = checkResources("espresso")
        if enoughResources == True:
            payment = countCoins(MENU['espresso']['cost'])
            if payment == True:
                finishTransaction()
                makeCoffee(MENU['espresso']['ingredients'])
                print(f"Enjoy your espresso!\n")
        else:
            print(f"Not enough resources. Choose another product.")

    elif userChoice in ('l', 'latte'):
        enoughResources = checkResources("latte")
        if enoughResources == True:
            payment = countCoins(MENU['latte']['cost'])
            if payment == True:
                finishTransaction()
                makeCoffee(MENU['latte']['ingredients'])
                print(f"Enjoy your latte!\n")
        else:
            print(f"Not enough resources. Choose another product.")

    elif userChoice in ('c', 'cappuccino'):
        enoughResources = checkResources("cappuccino")
        if enoughResources == True:
            payment = countCoins(MENU['cappuccino']['cost'])
            if payment == True:
                finishTransaction()
                makeCoffee(MENU['cappuccino']['ingredients'])
                print(f"Enjoy your cappuccino!\n")
        else:
            print(f"Not enough resources. Choose another product.")

    elif userChoice in ('o', 'off'):
        turnOff()
    elif userChoice in ('r', 'report'):
        printReport()
    else:
        print(f"There is no such product!")

#
#
#
# ############################ BOOTCAMP SOLUTION ############################
#
# profit = 0
#
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True
#
#
# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total
#
#
# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")
#
#
# is_on = True
#
# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
#
