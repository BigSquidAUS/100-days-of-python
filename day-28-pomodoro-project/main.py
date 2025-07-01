import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#379b46"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = float(25)
SHORT_BREAK_MIN = float(5)
LONG_BREAK_MIN = float(20)

start_pressed = False
timer = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    try:
        global reps
        global start_pressed
        window.after_cancel(timer)
        reps = 0
        canvas.itemconfig(timer_text, text="00:00")
        main_title.config(text="Timer",fg=GREEN)
        checkmarks.config(text="")
        start_pressed = False
    except ValueError:
        print("Timer wasn't initiated")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def button_start_pressed():
    """Function used to stop the start button from starting the timer multiple times."""
    print("Start button pressed")
    global start_pressed

    if not start_pressed:
        start_timer()
        start_pressed = True
    else:
        print("Timer already started")

def start_timer():
    global reps
    reps += 1

    if reps % 2 != 0 and reps < 8:
        #Is 1st, 3rd, 5th or 7th rep.
        print("Work Time")
        main_title.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60) # Work Time

    elif reps % 2 == 0 and reps < 8:
        #Is 2nd, 4th or 6th rep.
        print("Short Break")
        main_title.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60) # Short Break

    elif reps == 8:
        print("Long Break")
        main_title.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60) # Long Break
        reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60


    if count > 0:
        global timer
        canvas.itemconfig(timer_text, text=f"{count_minutes}:{int(count_seconds):02d}")
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer() #Timer ran out. Start it again.
        marks = ""
        work_sessions = math.floor(reps/2)
        for check in range(work_sessions):
            marks += "✔"

        checkmarks.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) #highlightthickness removes border around canvas
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

main_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,42,"bold"))
main_title.grid(column=1,row=0)

button_start = Button(text="Start",highlightthickness=0,command=button_start_pressed)
button_start.grid(column=0,row=2)

button_reset = Button(text="Reset",highlightthickness=0, command=reset_timer)
button_reset.grid(column=2,row=2)

checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME,18,"bold"))
checkmarks.grid(column=1,row=2)

window.mainloop()