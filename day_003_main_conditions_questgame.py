
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
#     else:
#         print("The ticket for adults is $12.0")
#         bill = 12
#
#     photo = input("Do you want a photo (Y or N)?\n")
#     if photo == 'Y':
#         bill += 3
#     print(f"The final price for ticket is ${bill}")
#
# else:
#     print("Sorry, You can't ride the rollercoster!")




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


############ order a pizza
print("Welcome to Online PIZZA!")
bill = 0
pizza_size = input("What size of pizza do you want (S, M, L)?):\n")

if pizza_size == "S" or "s":
    print("Small pizza is $15!")
    bill = 15
elif pizza_size == "M" or "m":
    print("Medium pizza is $20!")
    bill = 20
elif pizza_size == "L" or "l":
    print("Large pizza is $25!")
    bill = 25


    elif age < 18:
        print("The ticket for teens is $7.0")
        bill = 7
    else:
        print("The ticket for adults is $12.0")
        bill = 12


    pepperoni = input("Do you want to add pepperoni (Y or N)?\n")
    if pepperoni == 'Y':
    if pizza_size == "S" or "s":
        bill += 3
    print(f"Your bill is ${bill}")

else:
    print("Sorry, You can't ride the rollercoster!")