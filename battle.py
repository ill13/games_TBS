import random
from enum import Enum
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)


Weapon = Enum("Weapon", "Sword, Damage_Spell, Elemental_Fire")
Shield = Enum("Shield", "Armor, Magic, Elemental_Water")

# 'blocks' is a set or whatever. 
# 'blocks' could be replaced with 'stops' or 'defends' - the word itself has no reserved meaning
#  Whatever is in this set
Shield.Armor.blocks = { Weapon.Sword }
Shield.Magic.blocks = { Weapon.Damage_Spell }
Shield.Elemental_Water.blocks = { Weapon.Elemental_Fire }

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

    def __init__(self, name):
        self.name = name
        self.health = 50

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
        print(Fore.RED + f"\n***   Round: {self.round}   ***\n")  

    # Check if either or both Players is below zero health
    # change this to a loop that iterates all players and their health
    def check_win(self, player, enemy):
        if player.health < 1 and enemy.health > 0:
            self.game_over = True
            print("You Lose")
        elif enemy.health < 1 and player.health > 0:
            self.game_over = True
            print("You Win")
        elif player.health < 1 and enemy.health < 1:
            self.game_over = True
            print("*** Draw ***")



    def take_turn(self, player, enemy):

        if player.weapon not in enemy.shield.blocks:
            points=enemy.damage()
           # current_game.display_result(player, enemy,points)
            print(f"{player.name} attacks {enemy.name} with their {player.weapon.name}, {enemy.name} defended with their Shield of {enemy.shield.name} \n")
            print(f"{player.name} caused {points} damage to {enemy.name}\n")
        else:
            print(f"{player.name} attacks {enemy.name} with their {player.weapon.name}, {enemy.name} defended with their Shield of {enemy.shield.name} \n")
            print(f"{enemy.name} blocked {player.name}'s attack!\n")

        print (f"{player.name} : {player.health} | {enemy.name} : {enemy.health}")

# Setup Game Objects
current_game = Game()
human = AiPlayer("ill13")
ai = AiPlayer("PureEvil")
ai2 = AiPlayer("Nootrell")

players = [human, ai,ai2]

# Main Game Loop
while not current_game.game_over:

    i = 0
    
    battling = True

    while battling:
        current_game.new_round()
        for player in players:
            player.select_weapon()
            player.select_shield()
        current_player = players[i]
        i = (i + 1) % len(players)
        challenger = players[i]
        # change to random attack. After first attack, 
        # the defender will attack the player / aggressor who last attacked them
        # 
        current_game.take_turn(current_player, challenger)
        
        
        for player in players:
            #print (f"{player.name} : {player.health}")
            if player.health <= 0:
                print(f"{player.name} has been defeated!")
                players.remove(player)
                i=0

        if len(players)<=1:
            print("The battle is over!")
            battling=False
            current_game.check_win(current_player, challenger)
            

    

    # weapon select
    # for player in players:
    #     player.select_weapon()
    #     player.select_shield()
    
    #current_game.new_round()

    # current_game.take_turn(human, ai)
    # current_game.take_turn(ai, human)

    # for player in players:
    #     print(f"{player.name}'s health = {player.health}")

    #current_game.check_win(human, ai)


















'''



 
    # current_game.new_round()  
    # battling = True
    # idx = 0

    # while battling:
    #     for player in players:
    #         player.select_weapon()
    #         player.select_shield()
    #     current_player = players[idx]
    #     idx = (idx + 1) % len(players)
    #     challenger = players[idx]
    #     current_game.take_turn(current_player, challenger)

    #     if idx <= len(players)+1:
    #         battling=True
    #     else:
    #         battling=False
              
        
    #     for player in players:
    #         print (f"{player.name} : {player.health}")
            
    #         if player.health <= 0:
    #             battling=False
    #             current_game.game_over=True
        









    # def display_result(self, player, enemy,points):
    #         print(f"{player.name} attacks {enemy.name} with their {player.weapon.name}, {enemy.name} defended with their Shield of {enemy.shield.name} \n")
    #         print(f"{player.name} caused {points} damage to {enemy.name}\n")

        # if idx <= len(players)+1:
        #     battling=True
        #     current_game.new_round()
        # else:
        #     battling=False
            
              


    # for player in players:
    #     player.select_weapon()
    #     player.select_shield()
    #    



    #print(f"{human.name} : {human.health} | {ai.name} : {ai.health} | {ai2.name} : {ai2.health}")

    # change below into a loop that check for any player to be 0 health ro less
    #current_game.check_win(human, ai)




        # print(f"{human.name}'s health = {human.health}")
        # print(f"{ai.name}'s health = {ai.health}")
        # print(f"{ai2.name}'s health = {ai2.health}")
        #print(idx,len(players))


print(f"{human.name}'s health = {human.health}")
    print(f"{ai.name}'s health = {ai.health}")
    print(f"{ai2.name}'s health = {ai2.health}")



        # for player in players:
        #     if player.health <= 0:
        #         running=False


    # current_game.take_turn(human, ai)
    # current_game.take_turn(ai, human)
    # current_game.take_turn(ai, ai2)





'''