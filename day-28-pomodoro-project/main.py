import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#379b46"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

start_timing = False
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global start_timing
    start_timing = False
    canvas.itemconfig(timer_text, text=f"{WORK_MIN}:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global start_timing

    if not start_timing: #ie: If the timer isn't already started.
        start_timing = True
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global start_timing
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    if count >= 0 and start_timing:
        canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds:02d}")
        window.after(1000, count_down, count - 1)
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

button_start = Button(text="Start",highlightthickness=0,command=start_timer)
button_start.grid(column=0,row=2)

button_reset = Button(text="Reset",highlightthickness=0, command=reset_timer)
button_reset.grid(column=2,row=2)

checkmarks = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME,18,"bold"))
checkmarks.grid(column=1,row=2)

window.mainloop()