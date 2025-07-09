from tkinter import *
from tkinter import messagebox
import pandas
from random import choice
from pandas.errors import EmptyDataError

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
BLACK = "#000000"
D_GREEN = "#91c2af"
FONT_1 = ("Arial",40,"italic")
FONT_2 = ("Arial",60,"bold")

try:
    with open("data/to_learn.csv", "r"): #If the to_learn.csv file exists then use that data.
        data = pandas.read_csv("data/to_learn.csv") # Read the CSV.
        print("Started using saved data from previous session.")
except FileNotFoundError: #If the file does not exist then use all the words in french_words.csv as data.
    data = pandas.read_csv("data/french_words.csv")
    print("Started using full list of French words.")
except EmptyDataError:
    data = pandas.read_csv("data/french_words.csv")
    print("No words found in existing to_learn.csv. Starting again.")

df = pandas.DataFrame(data) # Create a DataFrame from the CSV.
word_dict = df.to_dict(orient="records") # Turn the DataFrame into a list of dictionaries.

screen = Tk()
screen.title("Flashy")
screen.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
button_unknown_img = PhotoImage(file="images/wrong.png")
button_known_img = PhotoImage(file="images/right.png")

canvas = Canvas(width=800,height=528,highlightthickness=0,bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(0,0, image=card_front_img, anchor="nw")

label_language = Label(font=FONT_1, bg=WHITE)
label_word = Label(font=FONT_2, bg=WHITE)

card_flipped = False
timer = None
current_words = {}

#------FUNCTIONS-------#
def flip_timer():
    global timer
    timer = screen.after(3000, flip_card) # After 3 seconds call the flip_card() function.

def flip_card():
    global card_flipped
    global current_words

    english_word = current_words["English"]
    card_flipped = True
    canvas.itemconfig(canvas_image, image=card_back_img)
    set_bg_colours(D_GREEN)

    label_language.config(text="English", fg=WHITE)
    label_word.config(text=english_word, fg=WHITE)

def set_bg_colours(colour):
    label_language.config(bg=colour)
    label_word.config(bg=colour)

def button_known_pressed():
    global card_flipped, timer, word_dict

    if len(word_dict) <= 0:
        #If there are no more words left to learn, display a message and then repopulate the word_dict with all the words.
        word_dict = df.to_dict(orient="records")  # Turn the DataFrame into a list of dictionaries.
        new_df = pandas.read_csv("data/french_words.csv")
        word_dict = new_df.to_dict(orient="records")
        messagebox.showinfo("Congratulations","There are no more words.\nStarting Again.")
    else:
        is_known()
        card_flipped = False

        screen.after_cancel(timer)
        flip_timer()
        set_bg_colours(WHITE)
        label_language.config(fg=BLACK)
        label_word.config(fg=BLACK)
        canvas.itemconfig(canvas_image, image=card_front_img)
        new_word()

def is_known():
    word_dict.remove(current_words)
    df = pandas.DataFrame(word_dict)
    df.to_csv("data/to_learn.csv", index=False)

def button_unknown_pressed():
    global card_flipped
    card_flipped = False

    screen.after_cancel(timer)
    flip_timer()
    set_bg_colours(WHITE)
    label_language.config(fg=BLACK)
    label_word.config(fg=BLACK)
    canvas.itemconfig(canvas_image, image=card_front_img)
    new_word()

def new_word():
    global current_words
    result = choice(word_dict)
    english_word = result["English"]
    french_word = result["French"]

    label_language.config(text="French")
    label_word.config(text=french_word)

    current_words = result

    return result # Returns a dictionary.

#---------UI LAYOUT----------#
canvas.grid(column=0,row=0, columnspan=2)
button_unknown = Button(command=button_unknown_pressed, image=button_unknown_img, bd=0, relief="flat", highlightthickness=0, activebackground=BACKGROUND_COLOR)
button_known = Button(command=button_known_pressed, image=button_known_img, bd=0, relief="flat", highlightthickness=0, activebackground=BACKGROUND_COLOR)
label_language.place(x=400,y=150,anchor="center")
label_word.place(x=400,y=264,anchor="center")
button_unknown.grid(column=0, row=1)
button_known.grid(column=1, row=1)

#------FUNCTIONALITY--------#
if not card_flipped:
    flip_timer()
    new_word()

screen.mainloop()