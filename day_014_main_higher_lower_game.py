################ Game Higher Lower ###############
# imports
import random
from day12_files.art import logo
from day14_files.game_data import data

def compare(a, b, user_variant):
    if a > b:
        if user_variant in ('A', 'a'):
            return 1
        else:
            return 0
    elif b > a:
        if user_variant in ('B', 'b'):
            return 1
        else:
            return 0

still_playing = True
while still_playing == True:
    counter = 0
    print(logo)

    variant_a = data[random.randint(0, len(data)-1)]
    variant_b = data[random.randint(0, len(data)-1)]

    def check_if_equals():
        """Cheks if A == B and if True > regenerate B"""
        global variant_a
        global variant_b
        if variant_a == variant_b:
            variant_b = data[random.randint(0, len(data)-1)]

    check_if_equals()

    game_continues = True
    while game_continues == True:
        print('Compare:')
        print(f"A: {variant_a['name']}, {variant_a['description']}, {variant_a['country']}")
        # print(variant_a['follower_count'])
        print('vs')
        print(f"B: {variant_b['name']}, {variant_b['description']}, {variant_b['country']}\n")
        # print(variant_b['follower_count'])
        print(f"Total correct compares: {counter}!")
        #request a user's variant
        user_variant = input("Who has more followers in Instagram? (A or B): ")

        result = compare(a=variant_a['follower_count'], b=variant_b['follower_count'], user_variant=user_variant)

        if result == 1:
            counter += 1
            print(f"You are right!\n")
        elif result == 0:
            print(f"You are wrong! You lose.\n")
            # print(f"Your total correct compares result is {counter}!")
            game_continues = False

        #load next couple for comparison: B => A, new_record => B
        variant_a = variant_b
        variant_b = data[random.randint(0, len(data))]
        check_if_equals()

    print(f"Total correct compares: {counter}!\n")
    another_game = input("Do you want to try one more time? (Y or N)")
    if another_game in ('Y','y','yes'):
        still_playing = True
    else:
        still_playing = False