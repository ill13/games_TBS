import random


items=["potion1","potion2","potion3","potion4","potion5","potion6","potion7","potion8","potion9","potion10"]

#weights=[1,2,3,4,5,4,3,2,1,1]
#weights = [0.5, 0.3, 0.2, 0.1, 0.1]

import random
def weighted_shuffle(items):
    weights = [item[1] for item in items] # get all weights from items
    return sorted([random.choice(weights) for _ in range(len(weights))], key=lambda x :x)[::-1] # sort using the weights as keys then reverse the result

randomized_list = weighted_shuffle(['apple', 'banana', 'cherry'])


shuffled_items = weighted_shuffle(items)
print(shuffled_items)
