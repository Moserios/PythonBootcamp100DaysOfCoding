# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
    #Access key and value
    # pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

########### NATO alphabet #############
import pandas
list = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(list)

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
alphabet = {}
for (index, row) in df.iterrows():
    alphabet[row.letter] = row.code
# print(alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter your word:").upper()
letters = [n for n in word]
# print(letters)
codes_and_words = {letter:word for (letter, word) in alphabet.items() if letter in letters}
# print(codes_and_words)
words = [word for word in codes_and_words.values()]
print(words)


# ########## bootcamp solution ###########
# import pandas
# list = pandas.read_csv("nato_phonetic_alphabet.csv")
# dictionary = {row.letter: row.code for (index, row) in list.iterrows()}
#
# word = input("Enter your word:").upper()
# output_list = [dictionary[letter] for letter in word]
# print(output_list)


