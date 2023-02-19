from tkinter import *

THEME_COLOR = "#375362"



class QuizInterface:
    def __init__(self):

        self.window = Tk()
        self.window.title("quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)


        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas()
        self.canvas.create_image(250, 300)
        self.question_text =self.canvas.create_text(200, 135, text="test", font=("arial", 20, "italic"), fill = "black")
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20, padx=20)





        false_photo = PhotoImage(file="./images/false.png")
        true_photo = PhotoImage(file="./images/true.png")
        self.false_button = Button(image=false_photo, highlightthickness=0)
        self.false_button.grid(row=2, column=0)
        self.true_button = Button(image=true_photo, highlightthickness=0)
        self.true_button.grid(row=2, column=1)

        self.window.mainloop()
