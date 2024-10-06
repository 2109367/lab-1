import random

DESCRIPTION = "In this game you have to find the missing number in the geometric progression!"


def get_question_and_answer():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)

    progression = [start * (ratio ** n) for n in range(length)]

    missing_index = random.randint(0, length - 1)
    correct_answer = str(progression[missing_index])
    progression[missing_index] = '..'
    question = " ".join(map(str, progression))
    return question, correct_answer
