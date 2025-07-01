from tkinter import *
#Use this to import every class from tkinter, rather than using
#import tkinter, means typing tkinter. before classes is not necessary.

# Layout Managers: pack, place, grid.
# An element must have one, and only one, of these specified, or it won't be displayed in the window.

def button_clicked():
    new_text = input_box.get()
    my_label.config(text=new_text)
    print("I got clicked")

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

#Label
my_label = Label(text="I am a label",font=("Arial",12))
my_label.config(text="New Text")
my_label.grid(column=0,row=0)

# Button
button = Button(text="Click Me",command=button_clicked)
button.grid(column=1,row=1)

button2 = Button(text="Click Me",command=button_clicked)
button2.grid(column=2,row=0)

# Entry / Input Component
input_box = Entry(width=20)
input_box.grid(column=3,row=3)



window.mainloop() #Keeps window open, must be at the very end.