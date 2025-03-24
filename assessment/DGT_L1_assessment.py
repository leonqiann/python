"""This program will figure out whether or not your dungeon party can  explore certain dungeons"""
#level of the party
p_level = 12
#dungeon names
dungeons = []
#level of dungeons
d_levels = []
#stop condition
stop = "The Moon"

#ask the user dungeon name and dungeon level until The Moon is entered. 
while True:
    if stop in dungeons:
        break
    dungeon_name = input("Enter the dungeon name: ")
    dungeons.append(dungeon_name)
    while True:
        try:
            dungeon_level = int(input("Enter the dungeon level: "))
            if dungeon_level < 0:
             print('Enter a positive number.')
            else:
                d_levels.append(dungeon_level)
                break
        except ValueError:
            print("Please enter a valid number.")

#count how many items are in the list
count = len(dungeons)
count2 = count
#will loop as many times as there are items in the list
for i in range(count):
    if d_levels[count2 - count] > p_level:
        print(f'We cannot easily explore {dungeons[count2 - count]}')
    else:
        print(f'We can easily explore {dungeons[count2 - count]}')
    count2 += 1