from brain_games.cli import (
    welcome_user,
    ask_user_str_answer,
    show_uncorrect_answer,
)
from random import randint

MIN_RND_NUMBER = 1  # min random number
MAX_RND_NUMBER = 100  # max random number
NUM_ATTEMPTS = 3  # number of attempts in the game


def is_prime(num: int) -> bool:
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False
    div = 3
    while div <= num / 2:
        if num % div == 0:
            return False
        div += 2
    return True


def get_prime_answer(num: int) -> str:
    return "yes" if is_prime(num) else "no"


def get_random() -> int:
    return randint(MIN_RND_NUMBER, MAX_RND_NUMBER)


def prime_game():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(NUM_ATTEMPTS):
        number = get_random()
        print(f"Question: {number}")
        user_answer = ask_user_str_answer()
        game_answer = get_prime_answer(number)
        if user_answer != game_answer:
            show_uncorrect_answer(user_answer, game_answer, user_name)
            return
        print("Correct!")
    print(f"Congratulations, {user_name}!")
