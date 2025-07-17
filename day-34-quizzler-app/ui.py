from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 16, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=340,height=500)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", font=("Arial",16),fg="WHITE", bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)

        self.canvas_w = 300
        self.canvas_h = 300
        self.canvas = Canvas(width=self.canvas_w,height=self.canvas_h,bg="WHITE")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.questions_text = self.canvas.create_text(
            (self.canvas_w/2),
            (self.canvas_h/2),
            text="the_question",
            anchor="center",
            fill=THEME_COLOR,
            font=FONT,
            width=(self.canvas_w - 20)
        )

        img_true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=img_true, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        img_false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=img_false, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def reset_canvas(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.questions_text, fill=THEME_COLOR)
        self.score_label.config(text=f"Score: {self.quiz.score}")  # Update the score.
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")

    def get_next_question(self):
        self.reset_canvas()

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questions_text, text=q_text)
        else:
            self.canvas.itemconfig(self.questions_text, text="No more questions.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#29b677")
        else:
            self.canvas.config(bg="#ee665d")
        self.canvas.itemconfig(self.questions_text, fill="white")
        self.window.after(1000, self.get_next_question)

