from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card={}

# ---------------------------------Function---------------------------------------------
try:
    french = pandas.read_csv("./data/words_to_learn.csv")
    french_frame = french.to_dict(orient="records")
except:
    french = pandas.read_csv("./data/french_words.csv")
    french_frame= french.to_dict(orient="records")

# french = [word["French"] for word in french_frame]
# english = [word["English"] for word in french_frame]
# print(english)
# print(french_frame)

def random_french():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(french_frame)
    new_french_word = current_card["French"]
    new_english_word = current_card["English"]
    canvas.itemconfig(french_label,text=f"{new_french_word}", fill = "black")
    canvas.itemconfig(french_title, text="French", fill="black")
    flip_timer = window.after(3000, flip_card, new_english_word)
    canvas.itemconfig(card, image = card_image)


def flip_card(new_english_word):
    canvas.itemconfig(card, image= card_back)
    canvas.itemconfig(french_label, text=f"{new_english_word}", fill="white")
    canvas.itemconfig(french_title, text= "English", fill= "white")


def print_card():
       french_frame.remove(current_card)
       new = pandas.DataFrame(french_frame)
       new.to_csv("./data/words_to_learn.csv", index = False)

# # ---------------------------------UI---------------------------------------------
window = Tk()
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

x_image = PhotoImage(file="./images/wrong.png" )
check_image = PhotoImage(file= "./images/right.png")


canvas = Canvas(width=800, height=526, bg = BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file= "./images/card_front.png")
card = canvas.create_image(400,263, image= card_image)
canvas.grid(row=0, column=0, columnspan=2)
french_title = canvas.create_text(400,163, text = "French", font = ("arial",25, "italic"))
french_label = canvas.create_text(400,263, text = "Word", font = ("arial",45, "bold"))
card_back = PhotoImage(file= "./images/card_back.png")




x_button = Button(image=x_image,  highlightthickness=0, command=random_french and print_card)
x_button.grid(row= 1, column=0)
check_button = Button(image=check_image, highlightthickness=0,command=random_french)
check_button.grid(row= 1, column=1)


print(french_frame)
random_french()
























window.mainloop()