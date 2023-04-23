#wars_class.py


import random
import copy

from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)
print("\n\n")


locations=["gym", "playground","cafeteria","hallway","classroom"]
products ={"hard candy":10,"chocolate bars":5,"donuts":3,"macaroons":4,"peanut butter cups":7}

class Player:
    # define our class
    money=0
    available_inventory=0
    max_inventory=10
    current_inventory=0
    current_location=[]


    # Trick #1: deepcopy to make a copy not a 'reference'
    player_inv = copy.deepcopy(products)
    # Trick #2: Reset all values in dict to '0'
    player_inv = dict.fromkeys(player_inv, 0)


    def check_inventory_space(self,_quantity=0):
        print('checking your inventory...')
        # what is the total space available to the player
        #change all of this to total the values in self.player_inv
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


def gen_prices(products):
        # copy the product dict
        tmp_item_dict=copy.deepcopy(products)
        # randomly select a high item from the temp dict
        high_item=random.choice(list(tmp_item_dict.keys()))
        # then pop [remove] the high item from the temp dict
        _unused_element = tmp_item_dict.pop(high_item)
        # randomly select a low item from remaining items in the temp dict
        low_item=random.choice(list(tmp_item_dict.keys()))
        # reset the temp dict to the orginal
        tmp_item_dict=products.copy()
        
        products[high_item]=int(int(tmp_item_dict[high_item]) + random.randint(1,10) * 1.72)
        products[low_item]=int(int(tmp_item_dict[low_item])  / 3)

        count=0
        for products,price in products.items():
            # only one random item should change a lot, others, only a small amount
            price = int(price) + random.randint(1,3)
            #print(count,products,price)
            count+=1
        
        return high_item,low_item

def sell(player,quantity,selected_product):
    print(f"selling {quantity} of {product_keys[selected_product]}")
    player.player_inv[product_keys[selected_product]] -= quantity

    player.money= player.money + (quantity * int(products[product_keys[selected_product]]) )
    return

def buy(player,quantity,selected_product):
    print(f"buying {quantity} of {product_keys[selected_product]}")
    player.player_inv[product_keys[selected_product]] += quantity

    player.money= player.money - (quantity * int(products[product_keys[selected_product]]) )
    #print(player.player_inv)
    #myguy.current_inventory=sum(myguy.player_inv.values())
    #player.check_inventory_space(player)
    return




def get_input(player,turn_number):
        action=(input("\n[B]uy, [S]ell, or [E]nd turn?"))
        match action.split():
            case ['b']:
                selected_product= (input("What would you like to purchase? "))
                selected_product=int(selected_product)
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

            case ['s']:
                selected_product= (input("What would you like to sell? "))
                selected_product=int(selected_product)
                # Does the player have the product if so, how many do they have?
                owned=player.player_inv[product_keys[selected_product]]

                sell_quantity = int(input(f" You have {owned}, how much {product_keys[selected_product]} would you like to sell? "))   
                
                sell(player,sell_quantity,selected_product)
                turn_number += 1
                return turn_number
            case ['e']:
                print("skipping turn...")
                turn_number +=1
                print(f" turn: {turn_number}")
                return turn_number
            case ['x']:
                print("quitting...")
                exit()
        print(player.player_inv)
        return



myguy=  Player()
myguy.money=29


# Main loop
turn_number = 1

while turn_number <= 10:

    high_item,low_item= gen_prices(products)
    product_keys = list(products)

    print("\n")
    print(f"Turn #: {turn_number}")

    i=0
    for item,price in products.items():
        print(Fore.YELLOW + f'{i}: {item} at ${price}')
        i+=1


    print(Fore.RED + f"\nhigh: {high_item} " + Fore.GREEN + f"low: {low_item} \n")
    myguy.current_inventory=sum(myguy.player_inv.values())
    print(Fore.YELLOW + f"You have ${myguy.money} and {myguy.current_inventory}/{myguy.max_inventory}")
    print(Fore.YELLOW + f"{myguy.player_inv}")
    
    turn_number=int(get_input(myguy,turn_number))



 


    












'''

                    
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