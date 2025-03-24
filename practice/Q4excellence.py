"""This program helps to figure out how many smart students their are in the class"""
#state constants
smart = 80
smart_students = 0
students = []
stop = 'done'
while True:
    try:
        score = input("Enter a score, or type 'done' to exit: ")
        score_lower = score.lower()
        if score_lower == stop:
            break
        else:
            score = int(score)
            students.append(score)
            if score >= smart:
                smart_students = smart_students + 1
    except ValueError:
        print('Invalid score!')
if smart_students != 1:
    print(f'This class has {smart_students} smart students!')
else:
    print(f'This class has {smart_students} smart student!')