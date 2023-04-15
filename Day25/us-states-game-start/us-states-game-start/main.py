import turtle
import pandas

states = pandas.read_csv("./50_states.csv")
screen = turtle.Screen()
screen.title("States of the United States")

image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# screen.bgpic(image)
user_score = 0
guessed_states = []
state_list = states.state.tolist()


while user_score != len(states):
    user_input = screen.textinput(f"{user_score}/{len(states)} Make a Guess : ", prompt="Name the state : ").title()
    # print(user_input)

    if user_input == "Exit":
        break
    if user_input in state_list:
        guessed_states.append(user_input)
        user_state = states[states.state == user_input]
        x = user_state["x"].item()
        y = user_state.y.item()
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x, y)
        t.write(user_input)
        user_score += 1


missed_states = []
for state in state_list:
    if state not in guessed_states:
        missed_states.append(state)

missed_states_dict = {
    "missed states": missed_states
}

missed_states = pandas.DataFrame(missed_states_dict)
missed_states.to_csv("missed_states.csv")

