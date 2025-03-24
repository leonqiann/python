"""This program will help track your spending and bank account"""
#state constants and list
money_list = [200, ]
stop = 0
balance = 200
while True:
    try:
        spent = int(input('Enter the amount spent: '))
        balance = balance - spent
        if spent > stop:
            money_list.append(balance)
        if spent == stop:
            break
        if balance <= 0:
            break
    except ValueError:
        #will print this when invalid number entered
        print('That is not a valid transaction.')
money_list.sort()
money_list.reverse()
print('My bank balances have been:')
for was in money_list:
    print(was)