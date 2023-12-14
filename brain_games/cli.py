import prompt


def welcome_user() -> str:
    """
    Ask for the user's name and greet him

    return: user's name
    """

    print("Welcome to the Brain Games!")
    user_name = prompt.string(prompt="May I have your name? ")
    print(f"Hello, {user_name}!")
    return user_name


def ask_user_str_answer() -> str:
    return prompt.string(prompt="Your answer: ").lower()


def ask_user_int_answer() -> str:
    return prompt.integer(prompt="Your answer: ")


def show_uncorrect_answer(user_answer: str, game_answer: str, user_name: str):
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{game_answer}'.")
    print(f"Let's try again, {user_name}!")
