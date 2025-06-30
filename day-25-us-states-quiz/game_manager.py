import pandas

def check_answer(answer, answer_list, guessed_states_list):
    result = answer.strip().lower()
    result = result.title() # Title-case instead of capitalize eg New York instead of New york.

    if result in guessed_states_list:
        print(f"You already guessed {result}.")
        return False

    elif result in answer_list:
        print(f"{result} is correct.")
        return True
    elif not result:
        print(f"Your guess was blank.")
        return False
    else:
        print(f"{result} is not a U.S State.")
        return False


def get_xy(the_state):
    """Returns the X and Y coordinates for the_state from the 50_states.csv"""
    state_data = pandas.read_csv(filepath_or_buffer="50_states.csv")

    result = the_state.strip().lower()
    result = result.title()

    data_frame = state_data[state_data.state == result] # Get the data for selected state.
    x_coord = data_frame.x.item() # Assign the X coordinate from the selected state.
    y_coord = data_frame.y.item() # Assign the Y coordinate from the selected state.

    return [x_coord,y_coord]


def unguessed_states_to_csv(states_list, guessed_states_list):
    # Define a function that takes two lists: all states, and the states that have already been guessed.

    unguessed_states = [state for state in states_list if state not in guessed_states_list]
    # Use a list comprehension to check which states were not guessed and add them to an unguessed_states list.

    unguessed_states_dict = {
        'State': unguessed_states,
    }
    # Create a dictionary where the key is 'State' and the value is the list of unguessed states.
    # This structure is suitable for converting into a pandas DataFrame.

    data_frame = pandas.DataFrame(unguessed_states_dict)
    # Convert the dictionary into a pandas DataFrame for tabular data representation.

    data_frame.to_csv('Unguessed States.csv')
    # Export the DataFrame to a CSV file named 'Unguessed States.csv'.
    # This will contain a single column labelled 'State' with each unguessed state on a new row.
