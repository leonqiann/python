#ts prgram will ask how many pizzas and print the amoutn of pizaas

#list of pizza options (storage)
pizzalist = []
stop = 0 
# ask how many of each piza (storage)
while True:
    try:
        cheese = int(input("How many cheese pizzas do we want? "))
        if cheese == stop:
            pizzalist.append(cheese)
            break
        if cheese < stop:
            print('Please enter a valid amount')
        else:
            pizzalist.append(cheese)
            break
    except ValueError:
        print('Please enter a valid amount')

while True:
    try:
        chicken = int(input("How many chicken pizzas do we want? "))
        if chicken == stop:
            pizzalist.append(chicken)
            break
        if chicken < stop:
            print('Please enter a valid amount')
        else:
            pizzalist.append(chicken)
            break
    except ValueError:
        print('Please enter a valid amount')

while True:
    try:
        pepperoni = int(input("How many pepperoni pizzas do we want? "))
        if pepperoni == stop:
            pizzalist.append(pepperoni)
            break
        if pepperoni < stop:
            print('Please enter a valid amount')
        else:
            pizzalist.append(pepperoni)
            break
    except ValueError:
        print('Please enter a valid amount')

while True:
    try:
        veggie = int(input("How many veggie pizzas do we want? "))
        if veggie == stop:
            pizzalist.append(veggie)
            break
        if veggie < stop:
            print('Please enter a valid amount')
        else:
            pizzalist.append(veggie)
            break
    except ValueError:
        print('Please enter a valid amount')

#print the customer order
# go thru list of pizzas (repetition)
#exclude orders of 0 pizzas (selection)

if pizzalist[0] != stop:
    print(f'Cheese: {pizzalist[0]}')
if pizzalist[1] != stop:
    print(f'Chicken: {pizzalist[1]}')   
if pizzalist[2] != stop:
     print(f'Pepperoni: {pizzalist[2]}')
if pizzalist[3] != stop:
    print(f'Veggie: {pizzalist[3]}')
