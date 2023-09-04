
############ check if you can ride the rollercoaster and gives the price
# print("Welcome to rollercoster!")
# height = int(input("Enter your height in CM:\n"))
#
# if height >= 120:
#     print("You can ride the rollercoster!")
#     age = int(input("What is your age?\n"))
#     bill = 0
#     if age < 12:
#         print("The ticket for kids is $5.0")
#         bill = 5
#     elif age < 18:
#         print("The ticket for teens is $7.0")
#         bill = 7
#     elif age > 45 and age < 55:
#         print("The ticket for teens is $0")
#         bill = 0
#     else:
#         print("The ticket for adults is $12.0")
#         bill = 12
#
#     photo = input("Do you want a photo (Y or N)?\n")
#     if photo in ('Y','y'):
#         bill += 3
#     print(f"The final price for ticket is ${bill}")
#
# else:
#     print("Sorry, You can't ride the rollercoster!")

#######################################


############# check odd or even number
# number = int(input("Which number do you want to check? "))
#
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")



######################## BMI CALCULATOR WITH INTERPRETATION

# weight = input("Enter your weight(in kg):\n")
# height = input("Enter your height(in meters):\n")
#
# bmi = (float(weight) / (float(height) ** 2))
#
# if bmi < 18.5:
#     print(f"Your BMI is {round(bmi)}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {round(bmi)}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {round(bmi)}, you are obese.")
# else:
#     print(f"Your BMI is {round(bmi)}, you are clinically obese.")


######################## Check if the year is a Leap Year

# year = int(input("Enter year to check if it's a Leap year:\n"))

# if year % 4 == 0:
#     print(f"Checked: {year} % 4 = {year % 4}! - OK")
#     if year % 100 == 0:
#         print(f"Checked: {year} % 100 = {year % 100}! - OK")
#         if year % 400 == 0:
#             print(f"Checked: {year} % 400 = {year % 400}! - OK")
#             print(f"{year} is a LEAP YEAR")
#         else:
#             print(f"Checked: {year} % 400 = {year % 400}! - NOT OK")
#             print(f"{year} is not a Leap year!")
#     else:
#         print(f"Checked: {year} % 100 = {year % 100}! - OK")
#         print(f"{year}  is a LEAP YEAR")
# else:
#     print(f"Checked: {year} % 4 = {year % 4}! - NOT OK")
#     print(f"{year} is not a Leap year!")

################# Short version of the leap year check #################
# year = int(input("Enter year to check if it's a Leap year:\n"))
# if year % 4 == 0:
#     #print("Leap year.")
#     if year % 100 == 0:
#         #print("Not leap year.")
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

##################################


############ order a pizza
# while True:
#     # 🚨 Don't change the code below 👇
#     print("Welcome to Python Pizza Deliveries!")
#     size = input("What size pizza do you want? S, M, or L ")
#     add_pepperoni = input("Do you want pepperoni? Y or N ")
#     extra_cheese = input("Do you want extra cheese? Y or N ")
#     # 🚨 Don't change the code above 👆
#
#     #Write your code below this line 👇
#     bill = 0
#
#     if size in ('S','s'):
#         bill += 15
#         if add_pepperoni in ('Y','y'):
#             bill += 2
#
#
#     elif size in ('M','m'):
#         bill += 20
#         if add_pepperoni in ('Y','y'):
#             bill += 3
#
#
#     elif size in ('L','l'):
#         bill += 25
#         if add_pepperoni in ('Y','y'):
#             bill += 3
#
#
#     if extra_cheese in ('Y','y'):
#             bill += 1
#
#
#     print(f"Your final bill is: ${bill}.")
#     print(' ')

############ ############ ############

############ LOVE CALCULATOR ############
# while True:
#     # 🚨 Don't change the code below 👇
#     print("Welcome to the Love Calculator!")
#     name1 = input("What is your name? \n")
#     name2 = input("What is their name? \n")
#     # 🚨 Don't change the code above 👆
#
#     #Write your code below this line 👇
#     combined_names = name1 + name2
#     combined_names_lower = combined_names.lower()
#
#     calculate_t = combined_names_lower.count("t")
#     calculate_r = combined_names_lower.count("r")
#     calculate_u = combined_names_lower.count("u")
#     calculate_e = combined_names_lower.count("e")
#     first_number = calculate_t + calculate_r + calculate_u + calculate_e
#
#
#     calculate_l = combined_names_lower.count("l")
#     calculate_o = combined_names_lower.count("o")
#     calculate_v = combined_names_lower.count("v")
#
#     second_number = calculate_l + calculate_o + calculate_v + calculate_e
#
#     combined = int(str(first_number) + str(second_number))
#
#     if combined < 10 or combined > 90:
#         print(f"Your score is {combined}, you go together like coke and mentos.")
#     elif combined >= 40 and combined <= 50:
#         print(f"Your score is {combined}, you are alright together.")
#     else:
#         print(f"Your score is {combined}.")
#
#     print(" ")
########################


######################## TREASURE ISLAND ########################

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇


first_step = input('''You are at the road and came across a crossroad. 
You have only two diredctions: left and right. 
Where are you going? 
(L(left) or R(right))?''').lower()
print("")

if first_step in ('L','l','left'):
    print('''You turned left and continue journey for a few hours. 
    Finally you see the road goes to a enormous lake with an island in the middle at a long distance.''')
    print("")
else:
    print('''You turned right and in some time the road entered a dark forest. 
    You've decided to enter it and continue journey. Suddenly a band of bandits jumped at the road and attacked you. 
    You were one agains seven and you managed to kill three of them but was wounded and killed.''')
    print("")
    print("Game Over")


if first_step in ('L','l','left'):
    second_step = input('''You came to the lake shore. 
    You may wait for a boat or try to swim. 
    Where are you going to do? 
    (W(wait) or S(swim)?''').lower()
    print("")
    if second_step in ('W','w','wait'):
        print('''You waited for a days and finally the boat appeared.
              You entered the boat and sailed to the island in the middle of the huge lake.''')
        print("")
    else:
        print('''You tried to swim to the island, but all your weapons and armour pulled you to the bottom of the lake and you drowned.''')
        print("")
        print("Game Over")

if first_step in ('L','l','left') and second_step in ('W','w', 'wait'):
    third_step = input('''You entered a dungeon and passed long tunnel which ended in a hall with three doors: red, yellow, blue. 
    Which one you want to open? 
    (R(red), Y(yellow) or B(blue)?''').lower()
    print("")
    if third_step in ('Y','y','yellow'):
        print("You opened a yellow door and see a big chest with a lot of gold coins and gems in and near it.")
        print("Congratulations! You Win")
        print('''
        *******************************************************************************
                  |                   |                  |                     |
         _________|________________.=""_;=.______________|_____________________|_______
        |                   |  ,-"_,=""     `"=.|                  |
        |___________________|__"=._o`"-._        `"=.______________|___________________
                  |                `"=._o`"=._      _`"=._                     |
         _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
        |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
        |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                  |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
         _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
        |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
        |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
        ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
        /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
        ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
        /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
        ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
        /______/______/______/______/______/______/______/______/______/______/_____ /
        *******************************************************************************
        ''')
    else:
        print('''You tried to open the door. But it stuck. 
        You pulled as hard as you could and you broke it with part of the wall. 
        The stones fell down and one of them hit you at the head and killed. 
        You'd better used your helmet...''')
        print("")
        print("Game Over")





########################################################################