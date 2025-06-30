import pandas

def check_answer(answer, answer_list):
    result = answer.strip().lower()
    result = result.title() # Title-case instead of capitalize eg New York instead of New york.

    if result in answer_list:
        # Answer is correct
        return True
    elif not result:
        # Answer was blank.
        return False
    else:
        # Not a correct answer.
        return False


def get_xy(the_state):
    """Returns the X and Y coordinates for the_state from the 50_states.csv"""
    state_data = pandas.read_csv(filepath_or_buffer="50_states.csv")

    result = the_state.strip().lower()
    result = result.title()

    data_frame = state_data[state_data.state == result] # Get the data for selected state.
    x_coord = data_frame["x"].iloc[0] # Assign the X coordinate from the selected state.
    y_coord = data_frame["y"].iloc[0] # Assign the Y coordinate from the selected state.

    return [x_coord,y_coord]