import random

def play_game():
    player = input("Enter your name: ")
    while True:
        print("Rock, Paper, Scissors!")
        rock = input("Enter your choice (r for rock, p for paper, s for scissors): ")
        if rock == "r":
            computer = random.choice(["p", "s"])
        elif rock == "p":
            computer = random.choice(["r", "s"])
        else:
            computer = random.choice(["r", "p", "s"])
        if computer == "r" or computer == "p":
            if random.random() < 0.5:
                print(f"{player} wins!")
            else:
                print(f"Computer wins!")
        elif computer == "s":
            if random.random() < 0.5:
                print(f"Computer wins!")
            else:
                print(f"{player} wins!")
        else:
            print("Invalid choice. Try again.")
        
play_game()