from tkinter import *
import pandas
from random import choice

data = pandas.read_csv("data/french_words.csv") # Read the CSV.
df = pandas.DataFrame(data) # Create a DataFrame from the CSV.
word_dict = df.to_dict(orient="records") # Turn the DataFrame into a list of dictionaries.

#------FUNCTIONS-------#
def button_known_pressed():
    print(new_word()["English"])

def button_unknown_pressed():
    print(new_word())

def new_word():
    result = choice(word_dict)
    english_word = result["English"]
    french_word = result["French"]

    label_language.config(text="French")
    label_word.config(text=french_word)

    return result # Returns a dictionary.


#---------UI DESIGN----------#
BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
FONT_1 = ("Arial",40,"italic")
FONT_2 = ("Arial",60,"bold")

screen = Tk()
screen.title("Flashy")
screen.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
button_unknown_img = PhotoImage(file="images/wrong.png")
button_known_img = PhotoImage(file="images/right.png")

canvas = Canvas(width=800,height=528,highlightthickness=0,bg=BACKGROUND_COLOR)
canvas.create_image(0,0, image=card_front_img, anchor="nw")
canvas.grid(column=0,row=0, columnspan=2)

label_language = Label(text="Title", font=FONT_1, bg=WHITE)
label_word = Label(text="word", font=FONT_2, bg=WHITE)
button_unknown = Button(command=button_unknown_pressed, image=button_unknown_img, bd=0, relief="flat", highlightthickness=0, activebackground=BACKGROUND_COLOR)
button_known = Button(command=button_known_pressed, image=button_known_img, bd=0, relief="flat", highlightthickness=0, activebackground=BACKGROUND_COLOR)

label_language.place(x=400,y=150,anchor="center")
label_word.place(x=400,y=264,anchor="center")
button_unknown.grid(column=0, row=1)
button_known.grid(column=1, row=1)

screen.mainloop()