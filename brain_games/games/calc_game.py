from brain_games.cli import (
    welcome_user,
    ask_user_int_answer,
    show_uncorrect_answer,
)
from random import randint

MIN_RND_NUMBER = 1  # min random number
MAX_RND_NUMBER = 100  # max random number
NUM_ATTEMPTS = 3  # number of attempts in the game
OPERATORS = ["+", "-", "*"]


def get_calc_answer(num1: int, num2: int, op: str) -> int:
    match op:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case _:
            return None


def get_random() -> int:
    return randint(MIN_RND_NUMBER, MAX_RND_NUMBER)


def get_operator() -> str:
    num_op = len(OPERATORS)
    return OPERATORS[randint(0, num_op - 1)]


def calc_game():
    user_name = welcome_user()
    print("What is the result of the expression?")
    for _ in range(NUM_ATTEMPTS):
        number1 = get_random()
        number2 = get_random()
        op = get_operator()
        print(f"Question: {number1} {op} {number2}")
        user_answer = ask_user_int_answer()
        game_answer = get_calc_answer(number1, number2, op)
        if user_answer != game_answer:
            show_uncorrect_answer(user_answer, game_answer, user_name)
            return
        print("Correct!")
    print(f"Congratulations, {user_name}!")
