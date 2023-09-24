### day 7: hangman game ####
import random
from day7_files import hangman_art
from day7_files import hangman_words
# from replit import clear

logo = hangman_art.logo
stages = hangman_art.stages
words = hangman_words.word_list

print(logo)

#TODO-1.0: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
# word_list = ["aardvark", "baboon", "camel"]

word_list = words

#TODO-1.1. - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1.2: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for letter in range(len(chosen_word)):
    # display.append("_")
    display += '_'
# print(display)

#TODO-1.3: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.

lives = 6
guessed_letters = []

end_of_game = False
# while "_" in display:
while end_of_game == False:

    #TODO-2.1 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess the letter?\n").lower()
    # clear()

    #TODO-3.1 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

    #TODO-3.2: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

    # TODO-3.3: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."

    i = 0
    for letter in chosen_word:
        if guess == letter:
            display[i] = guess
            i = i + 1
        else:
            i = i + 1


    if guess not in chosen_word:
        print(f"This is no such letter in the word: {guess}")
        lives -= 1


    if guess in guessed_letters:
        print(f"You already tried this letter: {guess}")
    if guess not in guessed_letters:
        guessed_letters.append(guess)


    #TODO-4: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in next step.

    #TODO-5: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
    print(display)
    print(f'Guessed letters: {guessed_letters}')
    print(f"Lives left: {lives}")

    if "_" not in display:
       print("You WIN.")
       end_of_game = True

    if lives == 0:
       print("You lose.")
       end_of_game = True



print("The End.")