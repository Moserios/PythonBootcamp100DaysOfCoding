import os
# file = open("text.txt")
# content = file.read()
# print(content)
# file.close()


with open("C:/Users/Sergey/Desktop/text.txt") as file:
    content = int(file.read())
    print(content)

new_var = int(input("Enter a new number:"))
if new_var > content:
    content = new_var


with open("C:/Users/Sergey/Desktop/text.txt", mode="w") as file:
    file.write(str(content))
