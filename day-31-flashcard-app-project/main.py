from tkinter import *
#---------UI DESIGN----------#
BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
FONT_1 = ("Arial",40,"italic")
FONT_2 = ("Arial",60,"bold")

screen = Tk()
screen.config(padx=50, pady=50,bg=BACKGROUND_COLOR)
screen.title("Flashy")

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
button_wrong_img = PhotoImage(file="images/wrong.png")
button_right_img = PhotoImage(file="images/right.png")

canvas = Canvas(width=800,height=528,highlightthickness=0,bg=BACKGROUND_COLOR)
canvas.create_image(0,0, image=card_front_img, anchor="nw")
canvas.grid(column=0,row=0, columnspan=2)

label_language = Label(text="French", font=FONT_1, bg=WHITE)
label_word = Label(text="trouve", font=FONT_2, bg=WHITE)
button_wrong = Button(image=button_wrong_img,bd=0,relief="flat",highlightthickness=0,activebackground=BACKGROUND_COLOR)
button_right = Button(image=button_right_img,bd=0,relief="flat",highlightthickness=0,activebackground=BACKGROUND_COLOR)

label_language.place(x=400,y=150,anchor="center")
label_word.place(x=400,y=264,anchor="center")
button_wrong.grid(column=0,row=1)
button_right.grid(column=1,row=1)

screen.mainloop()