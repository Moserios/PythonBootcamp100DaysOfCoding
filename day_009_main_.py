# DICTIONARIES

# Andrey = ''
#
# programmers = {
#     "Sergey": "Python programmer",
#     "Alexey": "C# and .NET programmer",
#     Andrey: "C# and JS programmer"
# }
#
# print(programmers["Sergey"])
# print(programmers[Andrey])


########### convert grades -> results ##############

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
Harry = student_scores["Harry"]

for student in student_scores:
    print(student)

print("----")
print(student_scores['Harry'])
# print(student_scores[Harry])






# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     if student_scores[key] in range(0, 71):
#         student_grades[key] = "Fail"
#     elif student_scores[key] in range(71, 81):
#         student_grades[key] = "Acceptable"
#     elif student_scores[key] in range(81, 91):
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] in range(91, 101):
#         student_grades[key] = "Outstanding"
#
# # 🚨 Don't change the code below 👇
# print(student_grades)

###############################

########## Nesting ###########

# travel_log = {
#     "France":
#         {
#             "cities": ["Paris", "Lille", "Marsel"],
#             "times_visited": 6
#         }
# }
#
# print(travel_log)

################# add dictionary to the list ##################
#
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above
#
# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
#
#
# def add_new_country(country, visits, cities):
#    # travel_log.append({"country": country, "visits": visits, "cities":cities}) # alternative way!!!
#    new_country = {}
#    new_country["country"] = country
#    new_country["visits"] = visits
#    new_country["cities"] = cities
#    travel_log.append(new_country)
#
#
#
#
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

###########################

# dict = {
#     "a" : 1,
#     "b" : 2,
#     "c" : 3,
#         }
#
# # dict["c"] = [1 ,2 , 3]
#
# # for key in dict:
# #     dict[key] += 1
#
# # dict[1] = 4
# print(dict[1])

##########################

# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []},
# }
#
# print(order["main"][2])
# print(order["main"][2][0])

#########################

############ Secret auction ##############


# import os
# clear = lambda: os.system('cls')

# #HINT: You can call clear() to clear the output in the console.
# import random
# random_lot = random.randint(3000, 4500)
#
# print("Welcome to the secret auction!")
# print(f"The lot #{random_lot} is about a street art by Banksy located in London known as:\n 'Girls with a red balloon!'")
#
# lot_bids = []
#
# new_participant = True
# while new_participant == True:
#     name = input("Write your name: \n")
#     bid_size = float(input("Write your bid: \n"))
#
#     new_bid = {'name': name, 'bid': bid_size}
#     lot_bids.append(new_bid)
#
#     more_bids = input("Are there other participants? (Y of N)\n")
#     if more_bids in ('Y','y'):
#         print("\n" * 50)
#         new_participant = True
#     else:
#         print("\n" * 50)
#         new_participant = False
#         break
#
#
#
# max_bid = 0
# winner_name = None
# for participant in lot_bids:
#     if participant['bid'] > max_bid:
#         max_bid = participant['bid']
#         winner_name = participant['name']
#
#
# print(f"The winner is {winner_name} with a bid of {max_bid}$.")




