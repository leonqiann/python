list = []
low = 0
bep = 1.2
#start the while loop to check for inputs of 1.2 or lower
try:
    num = float(input('Enter your input: '))
    #while number is bigger or equal to zero
    while num >= low:
        #check for numbers equal or bigger than 1.2
        if num >= bep:
            list.append('Beep')
        else:
            list.append('Boop')
        num = float(input('Enter your input: '))
except ValueError:
    print('Not robot compliant!')
for was in list:
    print(was)
    