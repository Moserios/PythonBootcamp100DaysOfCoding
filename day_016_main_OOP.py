# from day16_files import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
# tortilla = Turtle()
# print(tortilla)
# tortilla.shape("turtle")
# tortilla.color('blue')
# tortilla.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

#############################################

# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Coffee",['espresso','latte','cappuccino'])
# table.add_column("Price",['$1.5','$2.5','$3.0'])
# table.align = 'l'
# print(table)

############# COFFEE MACHINE WITH OOP ##############################

from day16_files.menu import Menu, MenuItem
from day16_files.coffee_maker import CoffeeMaker
from day16_files.money_machine import MoneyMachine

cm_menu = Menu()
cm_coffee_maker = CoffeeMaker()
cm_money_machine = MoneyMachine()


continue_working = True
while continue_working == True:
    choice = input(f'What would you like? : {(cm_menu.get_items())}').lower()


    if choice in ('off', 'o'):
        continue_working = False
        break


    if choice in ('report', 'r'):
        cm_coffee_maker.report()
        cm_money_machine.report()
        continue
    else:
        drink = cm_menu.find_drink(choice)
        response = cm_coffee_maker.is_resource_sufficient(drink)
        if response == True:
            payment = cm_money_machine.make_payment(drink.cost)
            if payment == True:
                make_coffe = cm_coffee_maker.make_coffee(drink)
            # else:
            #     print("Sorry, not enough money. Money refunded.")
        # else:
        #     print(f"{response}")
        # print(response)
        # print(payment)