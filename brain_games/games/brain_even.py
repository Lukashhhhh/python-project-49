from random import randint
import brain_games.engine as engine


def is_even(number: int) -> str:
    if number % 2 == 0:
        return 'yes'
    return 'no'


def generate_condition() -> int:
    return randint(1, 100)


def game() -> tuple:
    qwestion = generate_condition()
    correct_answer = is_even(qwestion)
    return qwestion, correct_answer


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    engine.run_game(game, description)


if __name__ == '__main__':
    main()
