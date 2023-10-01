from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps=0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    timer_label.config(text = "Timer")
    check_mark.config(text = "")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN *60
    # work_reps = [1,3,5,7]
    # short_reps = 8
    # long_break_rep = [2,4,6]
    # if reps in work_reps:
    #     count_down(5)
    #     reps = + 1
    # elif reps in short_reps:
    #     count_down(2)
    #     reps = + 1
    # elif reps in long_break_rep:
    #     count_down(1)
    #     reps = + 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text = "Break")
    elif reps % 2 == 0:
        count_down(2)
        timer_label.config(text="Break")
    else:
        count_down(2)
        timer_label.config(text="Work")



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    global check_mark_check
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)


    else:
        work_sessions = math.floor(reps / 2)
        marks = ""
        for i in range(work_sessions):
            marks += "+"
        check_mark.config(text= marks)

        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomadora")
window.config(padx= 100, pady=50, bg =YELLOW )

def something(thing):
    print(thing)



timer_label = Label(text = "Timer", fg = GREEN, bg = YELLOW, font= (FONT_NAME, 45, "bold"))
timer_label.grid(row=0 , column=1 )

canvas = Canvas(width = 200, height = 224, bg =YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image =tomato_img  )
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font =(FONT_NAME, 35, "bold"))
canvas.grid(row=1 , column=1 )



start_button = Button(text="Start", bg = "white", font =(FONT_NAME, 20, "bold"), command = start_timer)
start_button.grid(row=2 , column=0 )

reset_button = Button(text = "Reset", bg = "white", font =(FONT_NAME, 20, "bold"), command = reset_timer)
reset_button.grid(row=2 , column=2 )

check_mark = Label(fg = GREEN, bg = YELLOW, font =(FONT_NAME, 15, "bold"))
check_mark.grid(row=3 , column=1 )

window.mainloop()











