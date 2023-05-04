

'''
Solve this using Python

You are given a list of 3 or more items like

players = [human, bad_guy1,bad_guy2]

Choose one items from that list at random. However, the selected item cannot be the first item in the list
Now call a function that prints the names of the items using the first item from the list and the randomly chosen item as parameters
Then call the same function with the previous random item and the first item in reverse parameter order.
Choose another item from that list at random. However, this selected item cannot be the first item in the list or any of the previously selected items
Now call a function that prints the names of the items using the the random item from the list that was just selected and any one item from that list at random as a parameter.

'''

#players = [human, bad_guy1,bad_guy2]


# Import the random module
import random

# Define a list of 3 or more items
players = ["human", "bad_guy1", "bad_guy2", "bad_guy3", "bad_guy4"]

# Define a function that prints the names of the items
def print_names(item1, item2):
    print(f"{item1} and {item2}")

# Choose one item from the list at random, excluding the first item
random_item1 = random.choice(players[1:])

# Call the function with the first item and the random item as parameters
print_names(players[0], random_item1)

# Call the function with the random item and the first item in reverse order
print_names(random_item1, players[0])

# Choose another item from the list at random, excluding the first item and the previous random item
random_item2 = random.choice([item for item in players[1:] if item != random_item1])

# Call the function with the new random item and any one item from the list at random as parameters
print_names(random_item2, random.choice(players))