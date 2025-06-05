import art
import game_data
import random

def compare(first_contender, second_contender):
    """Compare the follower counts from the two arguments and returns
    a list with contenders in order of follower count."""
    first_contender_followers = int(first_contender["follower_count"])
    second_contender_followers = int(second_contender["follower_count"])

    if first_contender_followers > second_contender_followers:
        return [first_contender,second_contender]
    else:
        return [second_contender,first_contender]

def get_random_contender():
    """Returns a random dictionary entry from game_data.data
    with fields: name, follower_count, description, country"""
    chosen_data = random.choice(game_data.data)
    return chosen_data

def the_game():
    print(art.logo)
    score = 0
    previous_contender = []

    while True:
        # Check if there is a previous contender and set it to contender_a if there is.
        # otherwise get one randomly using the get_info() function.
        # Set contender b to a random contender as well.

        if len(previous_contender) < 1: #i.e. If the list is empty.
            contender_a = get_random_contender()
        else:
            contender_a = previous_contender

        contender_b = get_random_contender()

        print(len(previous_contender))

        # Check if they are both the same and if they are keep getting a new one until they are not.
        while contender_a == contender_b:
            contender_b = get_random_contender()
            print("Both contenders were the same, getting a new contender.")
        print(f"Your score: {score}")
        print(f"Compare A: {contender_a["name"]}, {contender_a["description"]}, from {contender_a["country"]}")
        print(art.vs)
        print(f"Against B: {contender_b["name"]}, {contender_b["description"]}, from {contender_b["country"]}")


        #print(f"{compare(contender_a, contender_b)[0]["name"]} has more followers than {compare(contender_a, contender_b)[1]["name"]}")

        player_choice = input("Who has more followers? Type 'A' or 'B':\n")
        if player_choice.lower() == "a":
            player_choice = contender_a
        else:
            player_choice = contender_b

        if compare(contender_a, contender_b)[0] == player_choice:
            # If player_choice is the same as the contender in the first position [0] of the
            # returned list from compare() then the choice is correct. Otherwise....it's not.
            print("Well done! You got it right.")
            previous_contender = contender_b
            score += 1
        else:
            print(f"Bad luck. You got it wrong.\n Final Score: {score}")
            break

while True :
    the_game()
    play_again = input("Do you want to play again? Y/N\n")

    if play_again.lower() not in ("y", "yes"):
        break
