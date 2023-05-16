import random
def play_game():
    player = random.choice(["rock", "paper", "scissors"])
    opponent = random.choice(["rock", "paper", "scissors"])
    while True:
        if player == opponent:
            print("It's a tie!")
        elif (player == "rock" and opponent == "scissors") or \
             (player == "paper" and opponent == "rock") or \
             (player == "scissors" and opponent == "paper"):
            print("You win!")
        else:
            print("You lose!")
        player = opponent
        opponent = random.choice(["rock", "paper", "scissors"])
    print("Game over.")
play_game()