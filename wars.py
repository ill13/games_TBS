import random
print("\n\n")

money=100
current_inventory=0
max_inventory=100
locations=["gym", "playground","cafeteria","hallway","classroom"]
products ={"hard candy":"2","chocolate bars":"5","gummmies":"3","munchkins":"4","peanut butter cups":"7"}
player_inv ={"hard candy":0,"chocolate bars":0,"gummmies":0,"munchkins":0,"peanut butter cups":0}


current_turn = 1

while current_turn <= 3:

    def gen_prices(products):
        # copy the product dict
        tmp_item_dict=products.copy()
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

    def check_inventory(_quantity):
        pass
        print('checking your inventory...')
        # do we have enough space for the purchase?
        # what's the maximum we can have in the inv?
        available_inventory = max_inventory - current_inventory

        if available_inventory <= 0:
            print("not enough inventory space to carry")
            return False
        # how many products are to be purchaesd?    
        if available_inventory - _quantity <= 0:
            print("quantity is too high")
            return False
        print('...you have space!')
        return available_inventory
        
    def check_money(subtotal,money):
        pass
        # do we have enough money for the purchase?
        print('checking your money...')
        money_remaining = money - subtotal

        if money_remaining < 0:
            print(f"you can't afford {subtotal} \n")
            return False
        else:
            print(f"you spent {subtotal} \n")
            money=money_remaining
        return money

    def sell():
        print("selling..")

    def buy(money):
        selected_product= (input("What would you like to purchase?  "))
        selected_product=int(selected_product)
        
        quantity = int(input(f"How much {product_keys[selected_product]} would you like to purchase?  "))      
        
        if check_inventory(quantity) == True:
            product_cost=int(products[product_keys[selected_product]])
            subtotal=product_cost * quantity
            money_remaining=check_money(subtotal,money)
            if money_remaining != False:
                money=money_remaining#"$TEST"
                print(f"you selected: {product_keys[selected_product]} at {product_cost}, Your subtotal is {subtotal}, you would have ${money} \n"  )
        else:
            get_input(money)
        return money

    def get_input(money):
        action=(input("\n[B]uy, [S]ell, or [E]nd turn?"))
        match action.split():
            case ['b']:
                print("buying")
                money=buy(money)
            case ['s']:
                sell()
            case ['e']:
                print("skipping turn...")
            case ['x']:
                print("quitting...")
                exit()
        return money


    high_item,low_item= gen_prices(products)
    product_keys = list(products)

    i=0
    for item,price in products.items():
        print(i,item,price)
        i+=1

    print("\n")
    print(f"Turn #: {current_turn}")
    print(f"Money: ${money}") 
    print(f"Inventory: {current_inventory}/{max_inventory}\n ") 
    print(f"high: {high_item} low: {low_item}")

    money=get_input(money)

    #print(f"\n test money: ${money}\n")


    # buy stuff. choose a number , then type a quantity
    # test quantity x price, then subtract total cash. If amount works continure otherwise tell max ans request input again
    # once success, addd to current_inventory
    # find the item that matches the number entered by converting to a list
        
    #item_keys = list(products)

    

    current_turn +=1















"""



 # 'reset' the product dict by copying the temp item_dict back to the original dict


    #verify=money -int(selected_product_coat)

    # for i, item,price in enumerate(items):
    #     print(i,item,price)



# this shoild hold the total count of all items


    # def check_for_exit():
    #     if selected_product == "x":
    #         print("quitting")
    #         exit()



# other items need to fluc
# so iterate through remaining or all? and do a little more random

# for item,price in items.items():
#     # only one random item should change a lot, others, only a small amount
#     price = int(price) + random.randint(0,3)

#     print(item,price)



# print("\n\n")


    # float to int, round up
#    print( len(items))
   # high_item=random.randint(1,len(items))
   # low_item=random.randint(1,len(items))

#    high_item_price=int(price) * random.randint(2,4)
#    lowitem_price=int(price) * random.randint(2,4)
#    price=random.randint(1,21)



#copy the dict, then pop the item, then select randome from teh copied dict then discard the temp dict

# for l in locations:
#     print(l)


#rnd_int= random.randint(0,65535)


# print(rnd_int)

# high_item=random.randint(1,len(items))
# low_item=random.randint(1,len(items))

# high_item_price=int(price) * random.randint(2,4)
# low_item_price=int(price) * random.randint(2,4)

#high_item=random.choice(items.keys())

"""