from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0,password)
    pyperclip.copy(password)
    label_feedback.config(text="Password copied to clipboard.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_user_input():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    fields = {
        "Website" : website,
        "Email" : email,
        "Password" : password
    }

    blank_fields = [name for name, value in fields.items() if not value.strip()]
    if blank_fields:
        message = ""
        for field in blank_fields:
            message += f"{field} was left blank.\n"

        messagebox.showerror(title="Required fields are blank.", message=message)
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Details for {website}:\nEmail: {email}\nPassword: {password}\nDo you want to add these?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

            label_feedback.config(text="Password Added Successfully!",fg="#379b46")
            entry_website.delete(0,END)
            entry_password.delete(0,END)
        else:
            label_feedback.config(text="Input cancelled by user", fg="#ff0000")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
canvas = Canvas(width=200,height=200,highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
entry_website = Entry(width=35)
label_email = Label(text="Email / Username:")
entry_email = Entry(width=35)
label_password = Label(text="Password:")
entry_password = Entry(width=21)
button_generate = Button(text="Generate Password", command=generate_password)
button_add = Button(width=36, text="Add",command=get_user_input)
label_feedback = Label(text="")

label_website.grid(column=0, row=1,sticky="w")
entry_website.grid(column=1,row=1,columnspan=2,sticky="ew")
entry_website.focus()
label_email.grid(column=0,row=2,sticky="w")
entry_email.grid(column=1,row=2,columnspan=2,sticky="ew")
entry_email.insert(0,"me@myemail.com")
label_password.grid(column=0,row=3,sticky="w")
entry_password.grid(column=1,row=3,sticky="ew")
button_generate.grid(column=2,row=3,sticky="ew")
button_add.grid(column=1,row=4,columnspan=2,sticky="ew")
label_feedback.grid(column=1,row=5,columnspan=2)

window.mainloop()