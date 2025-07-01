from tkinter import *

def calculate():
    try:
        the_input = float(user_input.get())
        the_result = (the_input * 1.60934)
        label_result.config(text=the_result)
        return True
    except ValueError:
        user_input.delete(0,END) # Clears the user_input box from beginning to end.
        print("Your input was invalid.")
        return False


window = Tk()
window.title("Miles to Kilometers Conversion")
window.config(padx=50,pady=50)

user_input = Entry(width=5)
label_miles = Label(text="Miles")
label_kms = Label(text="Kilometers")
label_equal = Label(text="is equal to")
label_result = Label(text="0")
button_calculate = Button(text="Calculate", command=calculate)

user_input.grid(column=1,row=0)
label_miles.grid(column=2,row=0)
label_equal.grid(column=0,row=1)
label_result.grid(column=1,row=1)
label_kms.grid(column=2,row=1)
button_calculate.grid(column=1,row=2)

window.mainloop()