import random
random_generator = random.Random()
def level():
    while (True):
        try:
            level = int(input("Enter level 1, 2, or 3: "))
            if level == 1:
                level_1 = level
                break
            elif level == 2:
                level_2 = level
                break
            elif level == 3:
                level_3 = level
                break
            else:
                print("Error: Invalid input!")
                continue
        except:
            print("Error: Invalid input!")
            continue
    return

def questions():
    while (True):
        try:
            question = int(input("Enter the number of questions to ask (3-10): "))
        except:
            print("ERROR: Please enter an integer value between 3 and 10!")
            continue
        if question > 10 or question < 3:
            print("ERROR: Please enter an integer value between 3 and 10!") 
        if question == 3:
            question_3 = question
        if question == 4:
            question_4 = question
        if question == 5:
            question_5 = question
        if question == 6:
            question_7 = question
        if question == 7:
            question_8 = question
        if question == 8:
            question_8 = question
        if question == 9:
            question_9 = question
        












level()

