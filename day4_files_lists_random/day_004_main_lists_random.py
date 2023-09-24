import random

# random_int = random.randint(0, 1)
#
#
# if random_int == 0:
#     print("Tails")
# elif random_int == 1:
#     print("Heads")



# ############# Who will pay for the meal ?
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
#
# random_int = random.randint(0, (len(names)-1))
#
# print(f"{names[random_int]} is going to buy the meal today!")


# fruits = ['apple', 'grapes', 'peach', 'cherry']
# vegetables = ['potato', 'tomato', 'onion', 'spinach']
#
# groceries = [fruits, vegetables]
#
# print(groceries[0  ][1])

################ treasure map ###################

# while True:
#     a = ['⬜️','⬜️','⬜️']
#     b = ['⬜️','⬜️','⬜️']
#     c = ['⬜️','⬜️','⬜️']
#
#     map = [a,b,c]
#     position = input("Where do you want to place a pointer?")
#     map[int(position[1])][int(position[0])] = 'X'
#     print(f"{a}\n{b}\n{c}\n")



##################################################

#######################  Rock Paper Scissors #################
#
# Rules:
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# while True:
pc_player_random = random.randint(1, 3)
pc_player = pc_player_random - 1
you = int(input("What is your choice? 0(rock), 1(paper), 2(scissors)\n"))



if pc_player == 0 and you == 0:
    print(rock)
    print(f"Computer chose:\n{rock}")
    print("Draw")

if pc_player == 1 and you == 1:
    print(paper)
    print(f"Computer chose:\n{paper}")
    print("Draw")

if pc_player == 2 and you == 2:
    print(scissors)
    print(f"Computer chose:\n{scissors}")
    print("Draw")


if pc_player == 0 and you == 1:
    print(paper)
    print(f"Computer chose:\n{rock}")
    print("You WIN")

if pc_player == 0 and you == 2:
    print(scissors)
    print(f"Computer chose:\n{rock}")
    print("PC WINs")

if pc_player == 1 and you == 0:
    print(rock)
    print(f"Computer chose:\n{paper}")
    print("PC WINs")

if pc_player == 1 and you == 2:
    print(scissors)
    print(f"Computer chose:\n{paper}")
    print("You WIN")

if pc_player == 2 and you == 0:
    print(rock)
    print(f"Computer chose:\n{scissors}")
    print("You WIN")

if pc_player == 2 and you == 1:
    print(paper)
    print(f"Computer chose:\n{scissors}")
    print("PC WINs")

