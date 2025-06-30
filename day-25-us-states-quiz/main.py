import turtle
import pandas
import game_manager
from label import Label
from scoreboard import Scoreboard

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

states = state_data["state"].tolist() # Convert dataframes to a Python list.
guessed_states = []
scoreboard = Scoreboard()

while scoreboard.the_score() < 50:
    answer_state = screen.textinput("Guess the state","Enter the name of state or type 'exit' to quit.")

    if answer_state == "exit":
        game_manager.unguessed_states_to_csv(states_list=states, guessed_states_list=guessed_states)
        break

    if game_manager.check_answer(answer=answer_state,answer_list=states,guessed_states_list=guessed_states): #If check_answer is true then get the X,Y coordinates.
        x_coord = int(game_manager.get_xy(the_state=answer_state)[0])
        y_coord = int(game_manager.get_xy(the_state=answer_state)[1])
        Label(answer_state,x_coord,y_coord)
        guessed_states.append(answer_state.strip().title()) #Adds the correct guess to a list of guessed states.
        scoreboard.increase_score()

    else:
        pass

    turtle.onscreenclick(get_mouse_coords)