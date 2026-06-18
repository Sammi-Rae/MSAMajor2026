import random
random_generator = random.Random()
def levels():
    while (True):
        try:
            level = int(input("Enter level 1, 2, or 3: "))
        except:
            print("Error: Invalid input!")
            continue
        if level > 3 or level < 1:
            print("Error: Invalid input!")
            continue
        else:
            break
    return level
    


def questions():
    while (True):
        try:
            number_of_questions = int(input("Enter the number of questions to ask (3-10): "))
        except:
            print("ERROR: Please enter an integer value between 3 and 10!")
            continue
        if number_of_questions > 10 or number_of_questions < 3:
            print("ERROR: Please enter an integer value between 3 and 10!")
        else:
            break
    return number_of_questions
    

def main():
    random_generator = random.Random()
    level = levels()
    number_of_questions = questions()
    correct_answers = 0
    for question in range(number_of_questions):
        if level == 1:
            X = random_generator.randint(0, 10)
            Y = random_generator.randint(0, 10)
            
        elif level == 2: 
            X = random_generator.randint(10, 99)
            Y = random_generator.randint(10, 99)

        elif level == 3:
            X = random_generator.randint(10, 99)
            Y = random_generator.randint(10, 99)

        correct_answer = X + Y
        number_of_attempts = 0
        while True:
            try:
                response = int(input(f"{X} + {Y} = "))
            except:
                print("WRONG!!!")
                number_of_attempts += 1
                continue

            if response == correct_answer:
                print("CORRECT!!!")
                correct_answers += 1
                break
            else:
                print("WRONG!!!")
                number_of_attempts += 1
            
            if number_of_attempts == 3:
                print(f"Correct Answer: {X} + {Y} = {correct_answer}")
                break

    percent = correct_answers / number_of_questions
    print(f"You got {correct_answers} out of {number_of_questions} correct: {percent * 100:.2f}%")
    

main()