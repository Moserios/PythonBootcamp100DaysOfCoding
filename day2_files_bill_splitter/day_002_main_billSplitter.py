# Calculate how much each of 5 should pay when splitting the bill with tips included

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print('Welcome to the Tip calculator')
theBill = input("What is the total bill:\n$")
theTips = float(1) + float(1 / 100 * float((input("How much tips do you want to pay additionaly in %:\n"))))
totalBillAndTips = float(theBill) * (float(theTips))
numberOfPersons = input("At what number of parts the bill should be splited:\n")
paymentPerPerson = (totalBillAndTips / int(numberOfPersons))
print("Each person should pay: " + '${:,.2f}'.format(paymentPerPerson))







# Calculate how many years/months/weeks/days left till your 90th anniversary

# age = input("Enter your age in years:\n")
# yearsLeft = 90 - int(age)
# monthsLeft = yearsLeft*12
# weeksLeft = yearsLeft*52
# daysLeft = yearsLeft*365
# print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")






# Calculate Body Mass Index (BMI) using formula: BMI = (weight/height**2)

# weight = input("Enter your weight(in kg):\n")
# height = input("Enter your height(in meters):\n")
# bmi = float(weight) / (float(height)**2)
# print(f"Your BMI is {round(bmi, 2)}.")


# print(1/10)
# print(1//10)
# print(1%10)

# print("Hello"[4])
# print((1500 + 3250) == (1_500 + 3_250))
#
# a = "Sergey"
# b = len("Sergey")
# c = "Sergey" == "Sergey"
# d = 3.14
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print("")
# print(type(str(15)))
#
#
# # 🚨 summ of two digits from two-digit number 👇
# two_digit_number = input("Type a two digit number: ")
# a = two_digit_number[0]
# b = two_digit_number[1]
# print(int(a) + int(b))

