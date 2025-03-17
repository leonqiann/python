#ts prgram will ask how many pizzas and print the amoutn of pizaas

#list of pizza options (storage)
pizzalist = []
stop = 0 
# ask how many of each piza (storage)
while True:
    try:
        cheese = int(input("How many cheese pizzas do we want?"))
        if cheese == stop:
            break
        if cheese > stop:
            pizzalist.append(cheese)
            break
    except ValueError:
        print('Please enter a valid amount')

while True:
    try:
        chicken = int(input("How many chicken pizzas do we want?"))
        if cheese == stop:
            break
        if cheese > stop:
            pizzalist.append(cheese)
            break
    except ValueError:
        print('Please enter a valid amount')

while True:
    try:
        pepperoni = int(input("How many pepperoni pizzas do we want?"))
        if cheese == stop:
            break
        if cheese > stop:
            pizzalist.append(cheese)
            break
    except ValueError:
        print('Please enter a valid amount')

while True:
    try:
        veggie = int(input("How many veggie pizzas do we want?"))
        if cheese == stop:
            break
        if cheese > stop:
            pizzalist.append(cheese)
            break
    except ValueError:
        print('Please enter a valid amount')


# go thru list of pizzas (repetition)

#exclude orders of 0 pizzas (selection)