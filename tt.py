# Define the rules of the game
def get_move(player):
    if player == "X":
        return "left"
    else:
        return "right"
# Initialize the game board
board = [0] * 10
# Play the game
while True:
    # Determine who goes first based on whether the board is empty or not
    if board[0]:
        player = "O"
    else:
        player = "X"
    
    # Print the current state of the board
    print("Current State:")
    for row in board:
        print("Row {}: {}".format(row, row))
    
    # Get the move from the current player
    move = get_move(player)
    
    # Make a move on the board
    if move == "up":
        row = int(input("Move up:"))
        row -= 1
    elif move == "down":
        row = int(input("Move down:"))
        row += 1
    elif move == "left":
        col = int(input("Move left:"))
        col -= 1
    elif move == "right":
        col = int(input("Move right:"))
        col += 1
    
    # Check if the move is valid
    if not (0 <= row < 10 and 0 <= col < 10):
        print("Invalid move! Try again.")
        continue
    
    # Check if the move is a win
    if board[row][col] == " ":
        winner = player
        break
    
    # Toggle the player
    if player == "X":
        player = "O"
    else:
        player = "X"
    
    # Flip the cell on the board
    board[row][col] = player
    
    # Check if the game has ended
    if check_win():
        print("Game over!", winner, "wins!")
        break
    
    # Ask if the current player wants to play again
    play_again = input("Do you want to play again? (y/n) ")
    if play_again!= "y":
        break