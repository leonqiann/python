""" This program will ask the user for their name and favourite numbers
and then perform some simple maths on the numbers."""

# Ask the user for their name and favourite numbers
name = input('whats your name ')
n1 = int(input('whats your favourite number '))
n2 = int(input('whats your second favourite number '))

#Perform some simple maths on the numbers
add = n1 + n2
multiply = n1 * n2

#greet the user and print the results
print(f'{name}, here are some calculations with your numbers')
print(f'{add}, {multiply}')