import turtle
screen = turtle.Screen()
screen.title("US States Game")
screen.setup(725, 491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
import pandas

data = pandas.read_csv("50_states.csv")
df = pandas.DataFrame(data)
# print(df)

states = data['state'].to_list()
# x_cor = data['x'].to_list()
# y_cor = data['y'].to_list()

def turn_off():
    screen.bye()

def add_state(state_name, x_cor, y_cor):
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    # print(state_name, x_cor, y_cor)
    new_turtle.penup()
    new_turtle.goto(x_cor, y_cor)
    new_turtle.write(f"{state_name}", align="center", font=("courier", 10, "normal"))
    screen.update()

def all_states():
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(0, 0)
    new_turtle.write("ALL STATES ARE GUESSED!\n  CONGRATULATIONS!", align="center", font=("courier", 20, "normal"))
    screen.update()

screen.listen()
screen.onkey(turn_off,"c")

guessed_states = []
correct_guesses = 0
while correct_guesses < 50:
    user_guess = screen.textinput(title=f"{correct_guesses}/50 States Correct", prompt="What's another state name?").title()
    if user_guess == 'Exit':
        # turn_off()
        break
    elif user_guess in df['state'].values:
        if user_guess in guessed_states:
            pass
        else:
            state_record = data[data["state"] == user_guess]
            state_name = state_record.state.values[0]
            state_x_cor = state_record.x.values[0]
            state_y_cor = state_record.y.values[0]
            correct_guesses += 1
            guessed_states.append(state_record.state.values[0])
            add_state(state_name, state_x_cor, state_y_cor)

            states.remove(state_name)
            dfn = pandas.DataFrame(states)
            # print(dfn)
            dfn.to_csv("missing_states.csv")
