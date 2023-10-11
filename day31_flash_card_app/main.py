BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
# import activate
import openpyxl
time = 6
timer = None
rand_card = {}
word1 = ""
word2 = ""
words_to_learn = {}
vacabulary = {}
# lang_new = "French"
# lang_main = "English"

def repeat_word():
    global words_to_learn
    words_to_learn.append(rand_card)
    if len(vacabulary) > 0:
        vacabulary.remove(rand_card)
    df = pandas.DataFrame(words_to_learn)
    df.to_csv("words_to_learn.csv", encoding='utf-8', index=False)
    new_word()

def remembered_word():
    global vacabulary, words_to_learn, timer
    if len(vacabulary) > 0:
        vacabulary.remove(rand_card)
        new_word()
    else:
        front_card_canvas.itemconfig(card_cover, image=card_front_img)
        front_card_canvas.itemconfig(card_top_text, text="All words were learned.")
        front_card_canvas.itemconfig(card_bottom_text, text="Choose another vacabulary.", font=("Arial", 40, "bold"))
        # timer = win.after_cancel(timer)

def new_word():
    global timer, rand_card, vacabulary, words_to_learn, word1, word2
    if timer != None:
        timer = win.after_cancel(timer)

    if len(vacabulary) > 0:
        rand_card = random.choice(vacabulary)
        # print(vacabulary)
        # print(words_to_learn)
        # print(rand_card)
    elif len(vacabulary) == 0 and len(words_to_learn) > 0:
        vacabulary.extend(words_to_learn)
        words_to_learn = []
        new_word()
    else:
        front_card_canvas.itemconfig(card_cover, image=card_front_img)
        front_card_canvas.itemconfig(card_top_text, text="All words were learned.")
        front_card_canvas.itemconfig(card_bottom_text, text="Choose another vacabulary.", font=("Arial", 40, "bold"))

    # print(rand_card)
    word1 = rand_card[lang_new]
    word2 = rand_card[lang_main]
    front_card_canvas.itemconfig(card_cover, image=card_front_img)
    front_card_canvas.itemconfig(card_top_text, text=lang_new)
    front_card_canvas.itemconfig(card_bottom_text, text=word1)
    count_down(time)


def count_down(count):
    global timer
    # print(f"C:{count}, T:{timer}")

    if count > 0:
        timer = win.after(1000, count_down, count - 1)
        if count == 6:
            front_card_canvas.itemconfig(card_cover, image=card_front_img)
            front_card_canvas.itemconfig(card_top_text, text=lang_new, fill="black")
            front_card_canvas.itemconfig(card_bottom_text, text=word1, fill="black")
        elif count == 2:
            front_card_canvas.itemconfig(card_cover, image=card_back_img)
            front_card_canvas.itemconfig(card_top_text, text=lang_main, fill="white")
            front_card_canvas.itemconfig(card_bottom_text, text=word2, fill="white")
    else:
        timer = win.after_cancel(timer)


# df = pandas.read_csv("data/french_words.xlsx")
df = pandas.read_excel("data/serbian-russian-50000-words.xlsx")
vacabulary = df.to_dict(orient="records")
# print(vacabulary)
keys = list(vacabulary[0].keys())
lang_new = keys[0]
lang_main = keys[1]
# print(lang_new)
# print(lang_main)

win = Tk()
win.title("Flash studying")
win.config(padx=50, pady=50, bg=BACKGROUND_COLOR) #width=800, height=526,

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")
right_img=PhotoImage(file="images/right.png")
wrong_img=PhotoImage(file="images/wrong.png")


## CARDS
front_card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_cover = front_card_canvas.create_image(400, 262, image=card_front_img)
card_top_text = front_card_canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")
card_bottom_text = front_card_canvas.create_text(400, 250, text="", font=("Arial", 60, "bold"), fill="black")
front_card_canvas.grid(row = 1, column = 0, rowspan = 3,  columnspan=5)



### BUTTONS
button_wrong = Button(height=100, width=100, image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=repeat_word)
button_wrong.grid(row = 4, column = 1)

button_right = Button(height=100, width=100, image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=remembered_word)
button_right.grid(row = 4, column = 3)

if timer == None:
    try:
        selected_words_list = pandas.read_csv("words_to_learn.csv")
        words_to_learn = selected_words_list.to_dict(orient="records")
        vacabulary += words_to_learn
        words_to_learn = []
    except FileNotFoundError:
        words_to_learn = []
    new_word()


win.mainloop()


################ BOOTCAMP SOLUTION #######
#
# from tkinter import *
# import pandas
# import random
#
# BACKGROUND_COLOR = "#B1DDC6"
# current_card = {}
# to_learn = {}
#
# try:
#     data = pandas.read_csv("data/words_to_learn.csv")
# except FileNotFoundError:
#     original_data = pandas.read_csv("data/french_words.csv")
#     print(original_data)
#     to_learn = original_data.to_dict(orient="records")
# else:
#     to_learn = data.to_dict(orient="records")
#
#
# def next_card():
#     global current_card, flip_timer
#     window.after_cancel(flip_timer)
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(card_title, text="French", fill="black")
#     canvas.itemconfig(card_word, text=current_card["French"], fill="black")
#     canvas.itemconfig(card_background, image=card_front_img)
#     flip_timer = window.after(3000, func=flip_card)
#
#
# def flip_card():
#     canvas.itemconfig(card_title, text="English", fill="white")
#     canvas.itemconfig(card_word, text=current_card["English"], fill="white")
#     canvas.itemconfig(card_background, image=card_back_img)
#
#
# def is_known():
#     to_learn.remove(current_card)
#     print(len(to_learn))
#     data = pandas.DataFrame(to_learn)
#     data.to_csv("data/words_to_learn.csv", index=False)
#     next_card()
#
#
# window = Tk()
# window.title("Flashy")
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
#
# flip_timer = window.after(3000, func=flip_card)
#
# canvas = Canvas(width=800, height=526)
# card_front_img = PhotoImage(file="images/card_front.png")
# card_back_img = PhotoImage(file="images/card_back.png")
# card_background = canvas.create_image(400, 263, image=card_front_img)
# card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
# card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)
#
# cross_image = PhotoImage(file="images/wrong.png")
# unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
# unknown_button.grid(row=1, column=0)
#
# check_image = PhotoImage(file="images/right.png")
# known_button = Button(image=check_image, highlightthickness=0, command=is_known)
# known_button.grid(row=1, column=1)
#
# next_card()
#
# window.mainloop()



