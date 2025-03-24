"""This program will figure out whether or not your dungeon party can  explore certain dungeons"""
#level of the party
p_level = 12
#dungeon names
dungeons = [""]
#level of dungeons
d_levels = []

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
             print('enter a positive')
            else:
                d_levels.append(dungeon_level)
                break
        except ValueError:
            print("please enter a valid number")