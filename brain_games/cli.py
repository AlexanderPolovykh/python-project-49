import prompt


def welcome_user():
    user_name = prompt.string(prompt='May I have your name? ')
    print(f'Hello, {user_name}!')