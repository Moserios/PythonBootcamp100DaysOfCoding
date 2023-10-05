# ################ Bootcamp solution ##############
# from tkinter import *
# import math
# # ---------------------------- CONSTANTS ------------------------------- #
# PINK = "#e2979c"
# RED = "#e7305b"
# GREEN = "#9bdeac"
# YELLOW = "#f7f5dd"
# FONT_NAME = "Courier"
# WORK_MIN = 1
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
# reps = 0
# timer = None
#
# # ---------------------------- TIMER RESET ------------------------------- #
# def reset_timer():
#     window.after_cancel(timer)
#     canvas.itemconfig(timer_text, text="00:00")
#     title_label.config(text="Timer")
#     check_marks.config(text="")
#     global reps
#     reps = 0
#
# # ---------------------------- TIMER MECHANISM ------------------------------- #
# def start_timer():
#     global reps
#     reps += 1
#
#     work_sec = WORK_MIN * 60
#     short_break_sec = SHORT_BREAK_MIN * 60
#     long_break_sec = LONG_BREAK_MIN * 60
#
#     if reps % 8 == 0:
#         count_down(long_break_sec)
#         title_label.config(text="Break", fg=RED)
#     elif reps % 2 == 0:
#         count_down(short_break_sec)
#         title_label.config(text="Break", fg=PINK)
#     else:
#         count_down(work_sec)
#         title_label.config(text="Work", fg=GREEN)
#
# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# def count_down(count):
#
#     count_min = math.floor(count / 60)
#     count_sec = count % 60
#     if count_sec < 10:
#         count_sec = f"0{count_sec}"
#
#     canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
#     if count > 0:
#         global timer
#         timer = window.after(1000, count_down, count - 1)
#     else:
#         start_timer()
#         marks = ""
#         work_sessions = math.floor(reps/2)
#         for _ in range(work_sessions):
#             marks += "✔"
#         check_marks.config(text=marks)
#
# # ---------------------------- UI SETUP ------------------------------- #
# window = Tk()
# window.title("Pomodoro")
# window.config(padx=100, pady=50, bg=YELLOW)
#
#
# title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
# title_label.grid(column=1, row=0)
#
# canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# tomato_img = PhotoImage(file="tomato.png")
# canvas.create_image(100, 112, image=tomato_img)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.grid(column=1, row=1)
#
# start_button = Button(text="Start", highlightthickness=0, command=start_timer)
# start_button.grid(column=0, row=2)
#
# reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
# reset_button.grid(column=2, row=2)
#
# check_marks = Label(fg=GREEN, bg=YELLOW)
# check_marks.grid(column=1, row=3)
#
# window.mainloop()
#
#

############## My solution ################

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
# Use color sets from https://colorhunt.co/ if need other colors
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_text = "✔"
result = ""
long_breaks_count = 0
short_breaks_count = 0
reset = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def click_reset():
    global reset
    global reps
    reset = 1
    result = ""
    top_lable.config(text="Click Start", fg=RED)
    bottom_count_lable.config(text=(f"{result}"))
    canvas.itemconfig(timer_text, text=f"00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def click_start():
    global reset
    global long_breaks_count
    reset = 0
    long_breaks_count = 0
    count_down(0)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(amount):
    # global count
    global reps
    global long_breaks_count
    global short_breaks_count
    global reset
    global result
    count = amount * 1
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")

    print(f"{count}, reps: {reps}, LBC: {long_breaks_count}, SBC: {short_breaks_count}, result: {result}")

    if reset == 1:
        reps = 0
        count = 0
        long_breaks_count = 1
        canvas.itemconfig(timer_text, text=f"00:00")
    elif count == 0 and long_breaks_count == 1:
        reps = 0
        long_breaks_count = 0
        short_breaks_count = 0
        result = ""
        canvas.itemconfig(timer_text, text=f"00:00")
        top_lable.config(text="Click Start", fg=RED)
    elif count == 0 and reps == 7:
        count_down(LONG_BREAK_MIN * 1)
        long_breaks_count = 1
        result += check_text
        bottom_count_lable.config(text=(f"{result}"))
        top_lable.config(text="Long break", fg=RED)
    elif count == 0 and reps == 0 and short_breaks_count == 0 and long_breaks_count == 0:
        count_down(WORK_MIN * 1)
        reps += 1
        top_lable.config(text="Work", fg=GREEN)
    elif count == 0 and reps % 2 == 0:
        count_down(WORK_MIN * 1)
        reps += 1
        top_lable.config(text="Work", fg=GREEN)
    elif count == 0 and reps % 2 != 0:
        count_down(SHORT_BREAK_MIN * 1)
        short_breaks_count += 1
        reps += 1
        result += check_text
        bottom_count_lable.config(text=(f"{result}"))
        top_lable.config(text="Short break", fg=PINK)
    elif count > 0:
        win.after(100, count_down, count -1)

# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title("Pomodoro Timer")
win.config(padx=100,pady=100, bg=YELLOW)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
bg_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=bg_image)

timer_text = canvas.create_text(100,130, text = "00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

top_lable = Label(text="Click Start", bg=YELLOW, fg=RED, font=(FONT_NAME, 20, "bold"))
top_lable.grid(column=1, row=0)

bottom_count_lable = Label(text=(f"{result}"), bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
bottom_count_lable.grid(column=1, row=3)

stat_button = Button(text="Start", width=5, command=click_start)
stat_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=5, command=click_reset)
reset_button.grid(column=3, row=2)

win.mainloop()