list = []
#state constants
stop = -1
cold = 34
hot = 42
while True:
    try:
        #test the things
        temp = int(input('Enter the temperature: '))
        if temp >= cold and temp <= hot:
            list.append('just right')
        if temp < cold and temp != stop:
            list.append('too cold')
        if temp > hot:
            list.append('too hot')
        if temp == stop:
            break
    except ValueError:
        #if it is not an integer it will pritn this and then restart the loop
        print('Invalid temperature.')

for wasd in list:
    #print the too hot or too cold or just right
    print(wasd)