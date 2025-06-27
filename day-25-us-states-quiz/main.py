import turtle
import pandas

def get_mouse_coords(x,y):
    """Use to determine X and Y position for labels by clicking on the map."""
    print(x,y)

state_data = pandas.read_csv("50_states.csv") #Columns = state, x, y

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = state_data["state"]

game_is_on = True
while game_is_on:
    answer_state = screen.textinput("Guess the state","Enter the name of state").lower()
    for entry in states:
        if answer_state == entry.lower():
            print(f"{answer_state.capitalize()} is correct.")
            break
        else:
            pass

    turtle.onscreenclick(get_mouse_coords)

turtle.mainloop()

