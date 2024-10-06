import math
import random

DESCRIPTION = "In this game you have to find the LCM! The LCM of two numbers is the smallest number that can be divided evenly by both of the original numbers."

def get_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(math.lcm(num1, num2))
    return question, correct_answer
