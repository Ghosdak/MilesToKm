from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(300,100)
window.config(padx=50,pady=50)

def calculate():
    answer['text'] = float(input.get()) * 1.609 
    
miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

km = Label(text="Km")
km.grid(column=2,row=1)

answer = Label(text="0")
answer.grid(column=1, row=1)

calculate_btn = Button(text="Calculate", command=calculate)
calculate_btn.grid(column=1, row=2)

input = Entry(width=8)
input.focus()
input.grid(column=1, row=0)

window.mainloop()