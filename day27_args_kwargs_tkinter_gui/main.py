from tkinter import *

def button_calculate_click():
    miles = float(input.get())
    km = round(miles * 1.60934, 2)
    lable4.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 400, height = 240)
window.config(padx=10, pady=40)

#Label1
lable1 = Label(text = "Miles", font=("Arial", 14, "bold"))
lable1.grid(column=2, row=0)
lable1.config(padx=20, pady=20)

#Label2
lable2 = Label(text = "Km", font=("Arial", 14, "bold"))
lable2.grid(column=2, row=1)
lable2.config(padx=20, pady=20)

#Label3
lable3 = Label(text = "is equal to", font=("Arial", 14, "bold"))
lable3.grid(column=0, row=1)
lable3.config(padx=20, pady=20)

#Label4
lable4 = Label(text = "0", font=("Arial", 14, "bold"))
lable4.grid(column=1, row=1)
lable4.config(padx=20, pady=20)

#Entry
input = Entry(width=10, font=("Arial", 14, "bold"))
input.grid(column=1, row=0)
# input.config(padx=10, pady=10)

# Button
button_calculate = Button(text="Calculate", command=button_calculate_click, width=10, font=("Arial", 12, "bold"))
button_calculate.grid(column=1, row=2)
button_calculate.config(padx=10, pady=10)

window.mainloop()