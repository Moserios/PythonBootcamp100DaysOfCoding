from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT = ("Arial", 8, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]


    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()


    if len(website) == 0:
        messagebox.showwarning(title="Empty field warning", message=f"Website field is empty")
    elif len(email) == 0:
        messagebox.showwarning(title="Empty field warning", message=f"Email field is empty")
    elif len(password) == 0:
        messagebox.showwarning(title="Empty field warning", message=f"Password field is empty")
    else:
        save_confirmations = messagebox.askokcancel(title="Save info",
                                                    message=f"Save provided info? \nWebsite: {website} \nEmail: {email} \nPassword: {password}")

    if save_confirmations == True:
        file = open("data.txt", "a")
        file.write(f"\n{website} | {email} | {password}")
        file.close()
        web_entry.delete(0, END)
        email_entry.delete(0, END)
        pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title("Password manager")
win.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=5, highlightbackground="black")
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=1)

## LABELS
web_label = Label(text="Website:", font=FONT, bg="white")
web_label.config(padx=5, pady=5)
web_label.grid(column=0, row=2)

email_label = Label(text="Email/Username:", font=FONT, bg="white")
email_label.config(padx=5, pady=5)
email_label.grid(column=0, row=3)

pass_label = Label(text="Password:", font=FONT, bg="white")
pass_label.config(padx=5, pady=5)
pass_label.grid(column=0, row=4)


## ENTRIES
web_entry = Entry(width=52)
web_entry.grid(column=1, row=2, columnspan=2)
web_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(column=1, row=3, columnspan=2)
email_entry.insert(0, "@gmail.com")

pass_entry = Entry(width=34)
pass_entry.grid(column=1, row=4)



## BUTTONS

gen_button = Button(text="Generate Password", font=FONT, command=generate_password)
# gen_button.config(padx=5, pady=5)
gen_button.grid(column=2, row=4)

add_button = Button(text="Add", font=FONT, width=36, command=add_data)
# add_button.config(padx=5, pady=5)
add_button.grid(column=1, row=5, columnspan=2)


win.mainloop()