### Functions with output ##########

#
# def format_name(first_name, last_name):
#   f_name = first_name.title()
#   l_name = last_name.title()
#
#   return f"{f_name} {l_name}"
#
# print(format_name("seRgeY", "MolChUn"))
#
# print(format_name(input("What is your first name?"), input("What is your last name?")))


############################ How many days in a month of a particular year ######################

#
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True #print("Leap year.")
#       else:
#         return False #print("Not leap year.")
#     else:
#       return True #print("Leap year.")
#   else:
#     return False #print("Not leap year.")
#
#
# def days_in_month(year, month):
#   """Takes arguments year and month to return how many days in selected month. Checks if it's the Leap year also"""
#   converted_month = month-1
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   leap_year = is_leap(year)
#   if converted_month == 1 and leap_year == True:
#     return month_days[1] + 1
#   elif converted_month == 1 and leap_year == False:
#     return month_days[1]
#   else:
#     return month_days[converted_month]
#
#
#
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))-1
# days = days_in_month(year, month)
# print(days)

#################### CALCULATOR #########################

# def result(num1, num2, operation_symbol):
#   if operation_symbol == '+':
#     oper_result = add(num1, num2)
#     return oper_result
#   if operation_symbol == '-':
#     oper_result = sub(num1, num2)
#     return oper_result
#   if operation_symbol == '*':
#     oper_result = multi(num1, num2)
#     return oper_result
#   if operation_symbol == '/':
#     oper_result = divide(num1, num2)
#     return oper_result

# print(f"{num1} {operation_symbol} {num2} = {result(num1, num2, operation_symbol)}")
from day10_files.art import logo

def calculator():
  print(logo)

  #Add
  def add(n1,n2):
    return n1 + n2

  #Subs
  def sub(n1,n2):
    return n1 - n2

  #Multi
  def multi(n1,n2):
    return n1 * n2

  #Divide
  def divide(n1,n2):
    return float(n1 / n2)




  operations = {"+": add, "-": sub, "*": multi, "/": divide}

  num1 = float(input("What is the first number?:"))

  continue_calculation = True
  while continue_calculation == True:
    num2 = float(input("What is the second number?:"))

    for key in operations:
      print(key)

    operation_symbol = input("What operation?:")

    calculation_function = operations[operation_symbol]
    result = float(calculation_function(num1, num2))

    print(f"{num1} {operation_symbol} {num2} = {result}")

    continue_reply = input("Continue calculation using current result? (y or n)\n")
    if continue_reply in ("Y", "y"):
      continue_calculation = True
      num1 = result
    else:
      continue_calculation = False
      calculator()

calculator()