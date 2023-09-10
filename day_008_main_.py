########## Functions ##############
#
# def greet():
#     print("First statement")
#     print("Second statement")
#     print("Third statement")
#     print(" ")
# greet()
#
#
# ################ Func with parameter ##############
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print(f"Have a nice offer {name}!")
#     print(" ")
#
# greet_with_name("Sergey")
#
#
# ################ Func with a few parameters ##############
#
# def greet_with_named_arg(name, location):
#     print(f"Hello {name}. Are you the first time in {location}?")
#     print(f"{name} how do you find {location} ?")
#     print(f"Have a nice offer in {location} {name}!")
#     print(" ")
#
# greet_with_named_arg(name = "Sergey", location = "Akvelon")
import math


############### paint hte wall #####################

# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
#
# number of cans = (wall height x wall width) ÷ coverage per can.
#
# e.g. Height = 2, Width = 4, Coverage = 5
# # number of cans = (2 * 4) / 5
# #                            = 1.6
#
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
#
# IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

# def paint_calc(height, width, cover):
#     number_of_cans = math.ceil((height * width) / cover)
#     print(f"You'll need {number_of_cans} cans of paint.")
#
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
#
# paint_calc(height=test_h, width=test_w, cover=coverage)


############## prime number checker #######################
# import math
# while True:
#     def prime_checker(number):
#         if number < 2:
#             print("It's not a prime number")
#
#         elif number >= 2:
#             for i in range(2, int(math.sqrt(number)) + 1):
#                 if  number % i == 0:
#                     print("It's not a prime number.")
#                     break
#             else:
#                 print("It's a prime number.")
#
#     n = int(input("Check this number: "))
#     prime_checker(number=n)
#


################### Ceaser Cipher ###########################


from day8_files.art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9','0', '.', ',', '!', ':', '-', '+', '/', '*', '_', '(', ')', '[', ']', '{', '}', '@', '#', '$', '%', '^', '&', '=', '<', '>', '~', '`']

request = True
while request == True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    #reorganyzing the code


    def ceaser(text, shift, direction):
        changed_text = ''
        fixed_shift = shift % len(alphabet)

        if direction == 'decode':
            fixed_shift = -fixed_shift

        for letter in text:
            if letter in alphabet:
                original_position = alphabet.index(letter)
                changed_index = (original_position + fixed_shift) % len(alphabet)

                # if changed_index > len(alphabet):
                #     changed_index = changed_index - len(alphabet)
                # elif changed_index < 0:
                #     changed_index = changed_index + len(alphabet)

                changed_text += alphabet[changed_index]

            else:
                changed_text += letter

        print(changed_text)

    ceaser(text, shift, direction)

    run_again = input("Do you want to restart the cipher program? (Y or N)")
    if run_again in ('Y','y'):
        request = True
    else:
        request = False

print("Goodbuy")


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#
# def encrypt(text, shift):
#     encrypted_text = ''
#     for letter in text:
#         original_position = alphabet.index(letter)
#         changed_index = original_position + shift
#         if changed_index > len(alphabet):
#             changed_index = changed_index - len(alphabet)
#         encrypted_text += alphabet[changed_index]
#     print(encrypted_text)
#
#
#
#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#     #e.g.
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"
#
#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#
#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#
# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
#
#
# def decrypt(text, shift):
#     decrypted_text = ''
#     for letter in text:
#         original_position = alphabet.index(letter)
#         changed_index = original_position - shift
#         if changed_index < 0:
#             changed_index = changed_index + len(alphabet)
#         decrypted_text += alphabet[changed_index]
#     print(decrypted_text)
#
# #TODO-4: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#
#   #TODO-5: Inside the 'decrypt' function, shift each letter of the 'text' *backwards*
#   # in the alphabet by the shift amount and print the decrypted text.
#   #e.g.
#   #cipher_text = "mjqqt"
#   #shift = 5
#   #plain_text = "hello"
#   #print output: "The decoded text is hello"
#
#
#
# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("You've entered improper command")
#TODO-6: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
# Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.



    # TODO-1: Import and print the logo from art.py when the program starts.

    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).

    # TODO-3: What happens if the user enters a number/symbol/space?
    # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    # e.g. start_text = "meet me at 3"
    # end_text = "•••• •• •• 3"

    # TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
    # e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
    # If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
    # Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

    #
    # if direction == "encode":
    #     for letter in text:
    #         original_position = alphabet.index(letter)
    #         changed_index = original_position + shift
    #         if changed_index > len(alphabet):
    #             changed_index = changed_index - len(alphabet)
    #         changed_text += alphabet[changed_index]
    #
    #
    # elif direction == "decode":
    #     for letter in text:
    #         original_position = alphabet.index(letter)
    #         changed_index = original_position - shift
    #         if changed_index < 0:
    #             changed_index = changed_index + len(alphabet)
    #         changed_text += alphabet[changed_index]


    # else:
    #     print("You've entered improper command")



