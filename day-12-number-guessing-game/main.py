import random
EASY_TURNS = 10
HARD_TURNS = 5

def set_difficulty():
    user_input = input("Choose a difficulty. Type 'easy' or 'hard'.")
    if user_input.lower().startswith("e"):
        turns = EASY_TURNS
    else:
        turns = HARD_TURNS
    return turns

def check_guess(the_guess, the_answer, turns):
    """Check the guess against the answer, if guess is incorrect then return the number of turns - 1"""
    if the_guess > the_answer:
        print("Too high.")
        return turns - 1
    elif the_guess < the_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You guessed correctly! The number was {the_answer}.")
        return turns

def the_game():
    the_number = random.randint(1,100)
    your_guess = 0

    turns = set_difficulty()
    print(f"I am thinking of a number between 1 and 100. {the_number}")

    while your_guess != the_number and turns > 0:
        print(f"You have {turns} turns left")
        your_guess = int(input("Make a guess: "))
        turns = check_guess(your_guess,the_number,turns)

    if turns == 0:
        print(f"You ran out of turns. The number was {the_number}.")
        return

run_game = True

while run_game:
    user_input = input("Start game? Y/N\n")
    if user_input.lower().startswith("y"):
        the_game()
    else:
        run_game = False
