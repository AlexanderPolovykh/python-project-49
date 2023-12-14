from brain_games.cli import (
    welcome_user,
    ask_user_int_answer,
    show_uncorrect_answer,
)
from random import randint

MIN_RND_NUMBER = 1  # min random number
MAX_RND_NUMBER = 10  # max random number
NUM_PROGRESS = 10  # progression length
NUM_ATTEMPTS = 3  # number of attempts in the game


def get_random() -> int:
    return randint(MIN_RND_NUMBER, MAX_RND_NUMBER)


def progression_game():
    user_name = welcome_user()
    print("What number is missing in the progression?")
    for _ in range(NUM_ATTEMPTS):
        position = get_random()
        start = get_random()
        step = get_random()
        progr = [el for el in range(start, start + step * NUM_PROGRESS, step)]
        progr_str = ""
        idx = 0
        while idx < NUM_PROGRESS:
            progr_str += " .." if idx == position - 1 else f" {progr[idx]}"
            idx += 1
        print(f"Question:{progr_str}")
        user_answer = ask_user_int_answer()
        game_answer = progr[position - 1]
        if user_answer != game_answer:
            show_uncorrect_answer(user_answer, game_answer, user_name)
            return
        print("Correct!")
    print(f"Congratulation, {user_name}!")
