def run_game(get_question_and_answer, description, player_name):
    print(description)
    for _ in range(3):
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        answer = input("Your answer: ")
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"answer '{answer}' is wrong. Correct answer was '{correct_answer}'. Try again later, {player_name}!")
            return
    print(f"Congratulations, {player_name}!")
