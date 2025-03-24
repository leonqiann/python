"""this program will output beep or boop depending on the numbers input"""
list = []
low = 0
high = 1.2
#start while loop 
while True:
    try:
        num = float(input('Enter your input: '))
        if num >= high:
            list.append('Beep')
        if num >= low and num < high:
            list.append('Boop')
        if num < low:
            break
    except ValueError:
        print('Not robot compliant!')
for wasd in list:
    print(wasd)