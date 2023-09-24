############ Global variables ##############
#
# flowers = 10
#
# def garden():
#     global flowers
#     print(flowers)
#     flowers =30
#     print(flowers)
#
# garden()
# print(flowers)

##############################################




########### Guess the number ###############
import random
from day12_files.art import logo

def guess_the_number():
    print(logo)
    user_has_guessed_correctly = False
    random_number = random.randint(1, 100)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty: 'Easy' or 'Hard'? (e or h)")
    attempts = 0
    if difficulty in ('Easy', 'easy', 'e'):
        attempts = 10
    else:
        attempts = 5

    print(f"Number is {random_number}")

    while attempts > 0:
        print(f"You have {attempts} remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess > random_number:
            print("Too high")
            attempts -= 1
        elif user_guess < random_number:
            print("Too low")
            attempts -= 1
        else:
            attempts = 0
            user_has_guessed_correctly = True

    if user_has_guessed_correctly == True:
        print(f"You got it! The number was {random_number}")
    elif user_has_guessed_correctly == False:
        print(f"You've run out of guesses, you lose! The number was {random_number}")

    another_game = input("Wanna take another chance? (Y or N)")
    if another_game in ('Y','y','yes','Yes'):
        guess_the_number()
    else:
        exit()

guess_the_number()