#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_text = letter.read()
# print(letter_text)


with open("./Input/Names/invited_names.txt") as names_list:
    names = []
    for name in names_list:
        names.append(name.rstrip("\n"))
    # print(names)

#Replace the [name] placeholder with the actual name.
for name in names:
# Replace the target string
    new_letter_text = letter_text.replace('[name]', name)
    # print(new_letter_text)

    #Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode='w') as processed_letter:
        processed_letter.write(str(new_letter_text))

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp