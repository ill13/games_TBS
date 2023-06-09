import random
import copy

from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)
print("\n\n")

locations=["gym", "playground","cafeteria","hallway","classroom"]
products ={"hard candy":1,"chocolate bars":2,"donuts":3,"macaroons":5,"peanut butter cups":8}

class Player:
    # define our class
    money=0
    available_inventory=0
    max_inventory=100
    current_inventory=0
    current_location=[]
    # Trick #1: deepcopy to make a copy not a 'reference'
    player_inv = copy.deepcopy(products)
    # Trick #2: Reset all values in dict to '0'
    player_inv = dict.fromkeys(player_inv, 0)


    def check_inventory_space(self,_quantity=0):
        print('checking your inventory...')
        # what is the total space available to the player
        self.current_inventory=sum(self.player_inv.values())
        # Does the player have enough space for the purchase?
        self.available_inventory = self.max_inventory - self.current_inventory
        # how many products are able to be purchased?    
        if self.available_inventory - _quantity < 0:
            print(Fore.RED + f" {self.current_inventory}/{self.max_inventory}. You only have {self.available_inventory} free. {_quantity} is too much")
            return False
        print(Fore.GREEN + f'you have space for {self.available_inventory}/{self.max_inventory} items!')   
        return self.available_inventory

    def check_account_balance(self,subtotal):
        # Does the player have enough money for the purchase?
        print('checking your money...')
        money_remaining = self.money - subtotal
        if money_remaining < 0:
            print(Fore.RED +  f"you can't afford ${subtotal} \n")
            return False
        else:
            print(Fore.GREEN + f"you will spend ${subtotal} \n")
            #self.money=money_remaining
        return True


def gen_prices(_products):
        # copy the product dict
        tmp_item_dict=copy.deepcopy(_products)
        # randomly select a high item from the temp dict
        high_item=random.choice(list(tmp_item_dict.keys()))
        # then pop [remove] the high item from the temp dict
        _unused_element = tmp_item_dict.pop(high_item)
        # randomly select a low item from remaining items in the temp dict
        low_item=random.choice(list(tmp_item_dict.keys()))
        # reset the temp dict to the original
        tmp_item_dict=copy.deepcopy(_products)
        
        _products[high_item]=int(int(tmp_item_dict[high_item]) + random.randint(1,10) * 1.72)
        _products[low_item]=int(((tmp_item_dict[low_item])  + random.randint(1,10) * 1.72) / random.randint(2,4))

        if _products[low_item] <= 0:
            _products[low_item]=1


        count=0
        for product,price in _products.items():
            # only one random item should change a lot, others, only a small amount
            price = int(price) + random.randint(0,3)
            price = int(price) - random.randint(0,3)
            #print(count,product,price)
            count += 1
        
        return high_item,low_item

def transaction(player,action,quantity,selected_product):
    print(f"{action}: {quantity} of {product_keys[selected_product]}")
    if action=='buy':
        player.player_inv[product_keys[selected_product]] += quantity
        player.money = player.money - (quantity * int(products[product_keys[selected_product]]) )
    if action=='sell':
        player.player_inv[product_keys[selected_product]] -= quantity
        player.money = player.money + (quantity * int(products[product_keys[selected_product]]) )
    return

     
def get_input(player,turn_number):
        action=(input("\n[B]uy, [S]ell, [E]nd turn, or [Q]uit? "))
        match action.split():
            case ['b']:
                selected_product= (input("What would you like to buy? "))
                if selected_product.isdigit():
                    selected_product=int(selected_product)
                    if selected_product not in range(0, len(products)):
                        print(f"product number '{selected_product}' does not exist")
                        return turn_number
                    else:
                        buy_quantity = int(input(f"How much {product_keys[selected_product]} would you like to purchase? ").isdigit())   
                else:
                    print(f"product '{selected_product}' does not exist")
                    return turn_number

                # Does the player have space?
                if player.check_inventory_space(buy_quantity):
                    subtotal=buy_quantity * int(products[product_keys[selected_product]])
                    # Does the player have money?
                    if player.check_account_balance(subtotal):
                       # buy(player,buy_quantity,selected_product)
                        transaction(player,"buy",buy_quantity,selected_product)
                        turn_number += 1
                        #return turn_number
                    else:
                        return turn_number
                else:
                    return turn_number
                return turn_number

            case ['s']:
                selected_product= (input("What would you like to sell? "))
                if selected_product.isdigit():
                    selected_product=int(selected_product)
                    if int(selected_product) not in range(0, len(products)):
                        print(f"product number '{selected_product}' does not exist")
                        return turn_number
                    else:
                        sell_quantity = int(input(f"How much {product_keys[selected_product]} would you like to sell? "))   
                # else:
                #     print(f"product '{selected_product}' does not exist")
                #     return turn_number



                # selected_product= int(input("What would you like to sell? "))
                # if selected_product not in range(0, len(products)):
                #     print(f"product number '{selected_product}' does not exist")
                #     return turn_number
                # Does the player have the product if so, how many do they have?
                owned=player.player_inv[product_keys[selected_product]]
                if owned <=0:
                    print("You cannot sell what you do not own!")
                    return turn_number
               # sell_quantity = int(input(f" You have {owned}, how much {product_keys[selected_product]} would you like to sell? "))   
                if sell_quantity <= owned:
                    transaction(player,"sell",sell_quantity,selected_product)
                    turn_number += 1
                    return turn_number
                else:
                    print("You cannot sell more than you have!")
                    return turn_number

            case ['e']:
                print("ending turn...")
                turn_number +=1
                return turn_number
            case ['q']:
                print("quitting...")
                exit()
            case _:
                pass
                print("invalid choice")
                return turn_number
    

myguy=  Player()
myguy.money=100
product_keys = list(products)

# Main loop
prev_turn_number=0
turn_number = 1
while turn_number <= 30:

    #save turn number, 
    # if turn number hasn't changed
    # dont regen
    # else: 
    # regen
    # 
    
    if prev_turn_number is not turn_number:
        high_item,low_item= gen_prices(products)

    prev_turn_number=turn_number

    myguy.current_inventory=sum(myguy.player_inv.values())
    
    print(f"\nTurn #: {turn_number}")
    i=0
    for item,price in products.items():
        print(Fore.YELLOW + f'{i}: {item} at ${price}')
        i+=1
    print(Fore.RED + f"\nhigh: {high_item} " + Fore.GREEN + f"low: {low_item} \n")
    print(Fore.YELLOW + f"You have ${myguy.money} and {myguy.current_inventory}/{myguy.max_inventory}")
    print(Fore.YELLOW + f"{myguy.player_inv}")
    
    turn_number=int(get_input(myguy,turn_number))

print("GAME OVER!") 
print(Fore.YELLOW + f"You made ${myguy.money}!")
print(Fore.YELLOW + f"{myguy.player_inv}")
    












'''

# def sell(player,quantity,selected_product):
#     print(f"selling {quantity} of {product_keys[selected_product]}")
#     player.player_inv[product_keys[selected_product]] -= quantity
#     player.money= player.money + (quantity * int(products[product_keys[selected_product]]) )
#     return

# def buy(player,quantity,selected_product):
#     print(f"buying {quantity} of {product_keys[selected_product]}")
#     player.player_inv[product_keys[selected_product]] += quantity
#     player.money= player.money - (quantity * int(products[product_keys[selected_product]]) )
#     return



def transaction(player,action,quantity,selected_product):
    selected_product= (input(f"What would you like to {action}? "))
    selected_product=int(selected_product)
    if action=="buy":
        buy_quantity = int(input(f"How much {product_keys[selected_product]} would you like to purchase? "))
        # Does the player have space?
        if player.check_inventory_space(buy_quantity):
            subtotal=buy_quantity * int(products[product_keys[selected_product]])
            # Does the player have money?
            if player.check_account_balance(subtotal):
                buy(player,buy_quantity,selected_product)
                turn_number += 1
                #return turn_number
            else:
                return turn_number
        else:
            return turn_number
        return turn_number   
    if action=="sell":
        # Does the player have the product if so, how many do they have?
        owned=player.player_inv[product_keys[selected_product]]
        sell_quantity = int(input(f" You have {owned}, how much {product_keys[selected_product]} would you like to sell? ")) 
        sell(player,sell_quantity,selected_product)
        turn_number += 1
        return turn_number 
                    
                #subtotal=quantity * int(products[product_keys[selected_product]])
               # player.check_money(subtotal)
                # if check_inv and check_money are both True
                #buy(player,quantity,selected_product)
                #else error
    

    # selected_product= (input("What would you like to purchase?  "))
    # selected_product=int(selected_product)
    
    # quantity = int(input(f"How much {product_keys[selected_product]} would you like to purchase?  "))      
    
    # if player.check_inventory(player.money) != False:
    #     product_cost=int(products[product_keys[selected_product]])
    #     subtotal=product_cost * quantity

    #     if player.check_money(subtotal):
    #         print(f"you selected: {product_keys[selected_product]} at {product_cost}, Your subtotal is ${subtotal}, you now have ${player.money} \n"  )
    #         player.current_inventory += quantity
    # else:
    #     get_input(player)
    #return money



# print(myguy.check_inventory(121))

# print(myguy.check_money(26))
   #money=get_input(money)

#money=100
#current_inventory=0
#max_inventory=100


'''