""""ts program will check to see if the user has entered a valid intger in a specific range of values"""
#use constants for low n high values
LOW = 1
HIGH = 10
#ask user to type num 
num = input('input an integer')
#check to see if num is valid
if num.lstrip("-").isnumeric():
    num = int(num)
    if num < LOW:
        print(f'{num} is lwer than {LOW}')
    elif num > HIGH:
        print(f'{num} is higher than {HIGH}')
    else:
        print(f'ur number is {num}')
else:
    print('ur num isnt an integer')
