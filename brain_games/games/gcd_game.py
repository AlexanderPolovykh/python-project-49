from brain_games.cli import (
    welcome_user,
    ask_user_int_answer,
    show_uncorrect_answer,
)
from random import randint
from math import gcd

MIN_RND_NUMBER = 1  # min random number
MAX_RND_NUMBER = 100  # max random number
NUM_ATTEMPTS = 3  # number of attempts in the game


def get_gcd_answer(num1: int, num2: int) -> int:
    return gcd(num1, num2)


def get_random() -> int:
    return randint(MIN_RND_NUMBER, MAX_RND_NUMBER)


def gcd_game():
    user_name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    for _ in range(NUM_ATTEMPTS):
        number1 = get_random()
        number2 = get_random()
        print(f"Question: {number1} {number2}")
        user_answer = ask_user_int_answer()
        game_answer = get_gcd_answer(number1, number2)
        if user_answer != game_answer:
            show_uncorrect_answer(user_answer, game_answer, user_name)
            return
        print("Correct!")
    print(f"Congratulation, {user_name}!")
