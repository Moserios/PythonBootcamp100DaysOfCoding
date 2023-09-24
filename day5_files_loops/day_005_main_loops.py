############### AVG HEIGHT ################


#
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#
# sum = 0
# quantity = 0
# for height in student_heights:
#     sum += height
#     quantity += 1
#
# avg = sum / quantity
# print(round(avg))

#################################

################## find max value in the list #######################


# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# max_value = 0
# for score in student_scores:
#     if score > max_value:
#         max_value = score
#
# print(f"The highest score in the class is: {max_value}")

####################################

###################### summ of all even numbers from 1 to 100 (including 100) ###########

# even_sum = 0
# for even in range(2, 101, 2):
#     even_sum += even
#
# print(even_sum)

####################################

###################### FizzBuzz game from 1 to 100 ###########

# RULES:
#
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# for number in range (1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#
#     else:
#         print(number)


###########################################################

################ password generator ######################

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


chosen_letters = []
chosen_numbers = []
chosen_symbols = []

random_letters_indexes = []
random_symbols_indexes = []

for number in range(0, nr_letters):
    random_letters_indexes.append(random.randint(0, 51))

for index in random_letters_indexes:
    chosen_letters.append(letters[index])

# print(chosen_letters)


for number in range(0, nr_numbers):
    chosen_numbers.append(random.randint(0, 9))

# print(chosen_numbers)


for number in range(0, nr_symbols):
    random_symbols_indexes.append(random.randint(0, 8))

for index in random_symbols_indexes:
    chosen_symbols.append(symbols[index])

# print(chosen_symbols)

all_selected = []
all_selected.extend(chosen_letters)
all_selected.extend(chosen_numbers)
all_selected.extend(chosen_symbols)

# print(all_selected)

password_list = all_selected
random.shuffle(password_list)
# print(password_list)


password = ''
for letter in password_list:
    password += str(letter)

print(password)


###########################################################