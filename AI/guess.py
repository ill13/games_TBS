
# Initialize the game
player_num_guesses = 0
correct_guess = False

# Define the rules for the game
defines = {
    "start": ["I am thinking of a number between 1 and 10.", "", ""],
    "guess": ["You have X number of guesses to find the number I am thinking of.", "", ""],
    "hint": ["The number I am thinking of is odd.", "", ""],
    "too_low": ["Too low!", "Your guess is too low. Try again.", ""],
    "too_high": ["Too high!", "Your guess is too high. Try again.", ""],
    "good_job": ["Good job! You found the number I was thinking of.", "", ""],
    "game_over": ["Game over! You won!" if correct_guess else "Game over! You lost."]
}

# Play the game
while True:
    # Determine what action to take based on the current state of the game
    action = None
    if defines["start"][0].startswith("I am thinking of a number between 1 and 10."):
        action = [defines["guess"][0], defines["hint"][0]]
    elif player_num_guesses < 3:
        action = [defines["guess"][0], defines["hint"][0]]
    else:
        action = [defines["game_over"][0], None]
    
    # Print the current state of the game
    print(action)
    
    # Check if the user wants to continue playing or quit the game
    response = input("Do you want to continue? (y/n) ")
    if response == "n":
        break
    
    # Update the game state based on the user's choice
    if action[0] == defines["guess"][0]:
        player_num_guesses += 1
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < 1 or guess > 10:
            print(defines["too_low"])
        elif guess < 5:
            print(defines["too_low"])
        else:
            correct_guess = True
            if guess == 5:
                print(defines["good_job"])
            else:
                print(defines["game_over"][1])
    elif action[1] == defines["hint"][0]:
        print(defines["hint"][1])
    else:
        print(defines["game_over"][1])
