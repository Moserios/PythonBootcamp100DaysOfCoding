### EXCEPTIONS HANDLING ###

### File not found error:
# file = open("dock.txt")
# file.read()

### handling exception ###

try:
    file = open("dock.txt")
    a_dictionary = {"key":"value"}
    key = (a_dictionary["key"])
    print((key))
except FileNotFoundError: ## this section will run if error Filenotfound occurs in try block
    file = open("dock.txt", "w")
    file.write("New Line\n")
except KeyError as error_message: ### this section will run if key error occurs in try block
    print(f"Key {error_message} doesn't exist")
else: ### this section will ru only if try block succeed without errors
   content = file.read()
   print(content)
finally: ## this block will run no matter what happens before
    file.close()
    print("file was closed")

# ### Key error
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existing_key"]
#
# ### Index error
# start_list = ["sun", "proxima", "sirius"]
# star = start_list[3]


# ####type error
# text = "ABCD"
# print(text + 5)

###########################################
# Convert formatted string to list
# fruits = eval(input())
fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as ex_message:
        print("Fruit pie")
    else:
        print(fruit + " pie")

make_pie(4)  # Raises IndexError on list with less than 5 items.

#####################

# eval() function will create a list of dictionaries using the input
# facebook_posts = eval(input())
facebook_posts = [{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]
total_likes = 0
# TODO: Catch the KeyError exception

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError as er_message:
        total_likes = total_likes + 0
        # print("No likes for this post")

print(total_likes)