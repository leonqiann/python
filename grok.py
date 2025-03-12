# Get user input to use in the for loop range arguments
# and savings calculations
savings = 0
months = 0
item = input("What item do you want to buy? ")
cost = int(input("Item cost $: "))
save_amount = int(input("Savings amount $: "))
duration = int(input("How many months? "))
step_increment = int(input("How often will you save? "))

# Use a for loop with range arguments to calculate how many
# months are needed to save to reach the item price
start = 0
stop = duration
step = step_increment
for months in range(start, stop, step):
    savings = savings + save_amount
    print(f'After {months + step_increment} month(s) you will have ${savings}')


# Print the results of the savings time calculations
if cost < ((months + step_increment) * save_amount):
  print(f'You have saved {(months + step_increment) * save_amount} and have enough to buy your {item}!')
else:
  print(f'You need to save more to buy your {item}.')
                     
