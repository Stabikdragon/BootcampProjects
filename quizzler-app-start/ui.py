from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")

        self.question_text = self.canvas.create_text(150, 125, text="test", width=280, font=("arial", 20, "italic"),
                                                     fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

        false_photo = PhotoImage(file="./images/false.png")
        true_photo = PhotoImage(file="./images/true.png")
        self.false_button = Button(image=false_photo, highlightthickness=0, command=self.false)
        self.false_button.grid(row=2, column=0)
        self.true_button = Button(image=true_photo, highlightthickness=0, command=self.true)
        self.true_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="you've reached the end")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right is True:
            self.canvas.configure(bg="green", highlightthickness=0)

        else:
            self.canvas.configure(bg="red", highlightthickness=0)
        self.window.after(1000, self.get_next_question)