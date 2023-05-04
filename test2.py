# Import the random module
import random

# Define a list of 3 or more players
players = ["human", "bad_guy1", "bad_guy2", "Eville","Gud", "Newtral","Fooper"]

# Define a function that prints the names of the players
def print_names(player1, player2):
    print(f"{player1} vs {player2}")

random_player = random.choice(players[1:])

# Encapsulate this in a neat loop for 4 turns
for i in range(4):
    # Choose one player from the list at random
    # However, the selected player cannot be the first player in the list
    
    print(i)
    # Call the function that prints the names of the players
    # Using the first player from the list and the randomly chosen player as parameters
    print_names(players[0], random_player)

    # Call the same function with the previous random player and the first player in reverse parameter order
    print_names(random_player, players[0])

    # Choose another player from the list at random
    # However, this selected player cannot be the first player in the list or any of the previously selected players
    remaining_players = [player for player in players if player not in (players[0], random_player)]
    another_random_player = random.choice(remaining_players)
    new_random_player = random.choice(players)

    # Call the function that prints the names of the players
    # Using the random player from the list that was just selected and any one player from that list at random as a parameter
    print_names(another_random_player,new_random_player)
    print_names(new_random_player, another_random_player)
    
