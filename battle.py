import random
from enum import Enum

Weapon = Enum("Weapon", "Sword, Damage_Spell, Fire_Elemental")
Shield = Enum("Shield", "Armor, Magic, Water_Elemental")

Shield.Armor.blocks = { Weapon.Sword }
Shield.Magic.blocks = { Weapon.Damage_Spell }
Shield.Water_Elemental.blocks = { Weapon.Fire_Elemental }

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = None
        self.shield = None

    def damage(self):
        points = random.randint(10, 35)
        self.health -= points
        return points

    def select_weapon(self):
        weapons = [f"{weapon.value}-{weapon.name}" for weapon in Weapon]
        weapons = ", ".join(weapons[:-1]) + " or " + weapons[-1]
        choice = int(input(f"Choose your weapon {weapons}:  "))
        self.weapon = Weapon(choice)

    def select_shield(self):
        shields = [f"{shield.value}-{shield.name}" for shield in Shield]
        shields = ", ".join(shields[:-1]) + " or " + shields[-1]
        choice = int(input(f"Choose your shield {shields}:  "))
        self.shield = Shield(choice)

class AiPlayer(Player):

    def select_weapon(self):
        self.weapon = random.choice(list(Weapon))

    def select_shield(self):
        self.shield = random.choice(list(Shield))

class Game:
    def __init__(self):
        self.game_over = False
        self.round = 0

    def new_round(self):
        self.round += 1
        print(f"\n***   Round: {self.round}   ***\n")  

    # Check if either or both Players is below zero health
    # change this to a loop that iterates all players and their health
    def check_win(self, player, opponent):
        if player.health < 1 and opponent.health > 0:
            self.game_over = True
            print("You Lose")
        elif opponent.health < 1 and player.health > 0:
            self.game_over = True
            print("You Win")
        elif player.health < 1 and opponent.health < 1:
            self.game_over = True
            print("*** Draw ***")


    def display_result(self, player, opponent):
            print(f"{player.name} attacks {opponent.name} with their {player.weapon.name}, {opponent.name} defended with their Shield of {opponent.shield.name} \n")
            print(f"{player.name} caused damage to {opponent.name}\n")

    def take_turn(self, player, opponent):

        if player.weapon not in opponent.shield.blocks:
            opponent.damage()
            current_game.display_result(player, opponent)
        else:
            print(f"{player.name} attacks {opponent.name} with their {player.weapon.name}, {opponent.name} defended with their Shield of {opponent.shield.name} \n")
            print(f"{opponent.name} blocked {player.name}'s attack - No Damage\n")

# Setup Game Objects
current_game = Game()
human = Player("ill13")
ai = AiPlayer("PureEvil")
ai2 = AiPlayer("NooTrell")

players = [human, ai,ai2]

# Main Game Loop
while not current_game.game_over:
    for player in players:
        player.select_weapon()
        player.select_shield()
    current_game.new_round()
    current_game.take_turn(human, ai)
    current_game.take_turn(ai, human)
    current_game.take_turn(ai, ai2)
    print(f"{human.name}'s health = {human.health}")
    print(f"{ai.name}'s health = {ai.health}")
    print(f"{ai2.name}'s health = {ai2.health}")
    current_game.check_win(human, ai)