import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(700, 500)

correct_answer = 0
correct_answer_list = []

states_file = "50_states.csv"
data = pandas.read_csv(states_file)
states_list = data.state.to_list()


def write_state(state, coor):
    state_name = turtle.Turtle()
    state_name.ht()
    state_name.penup()
    state_name.goto(coor)
    state_name.write(f"{state}",align = "center", font=('Arial', 8, 'normal'))

def states_to_learn():
    incorrect_answer_list = [i for i in states_list if i not in correct_answer_list]
    # for i in states_list:
    #     if i not in correct_answer_list:
    #         incorrect_answer_list.append(i)
    with open("learn.csv", mode= "w") as file:
        file.write(f"{incorrect_answer_list}")

while correct_answer != 50:

    answer_state = screen.textinput(title=f"{correct_answer}/50 States Correct", prompt="whats another state?").title()
    if answer_state == "Exit":
        states_to_learn()
        break
    if answer_state in states_list and answer_state not in correct_answer_list:
        state_coor = int(data.x[data.state == answer_state]), int(data.y[data.state == answer_state])
        correct_answer += 1
        correct_answer_list.append(answer_state)
        write_state(answer_state,state_coor)

