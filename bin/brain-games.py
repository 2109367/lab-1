#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.engine import run_game
import brain_games.LCM as lcm_game
import brain_games.progression as progression_game

def main():
    player_name = welcome_user()  # Сохраняем имя пользователя
    print("Choose the game:")
    print("1. Least Common Multiple (LCM)")
    print("2. Geometric Progression")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        run_game(lcm_game.get_question_and_answer, lcm_game.DESCRIPTION, player_name)
    elif choice == '2':
        run_game(progression_game.get_question_and_answer, progression_game.DESCRIPTION, player_name)

if __name__ == '__main__':
    main()
