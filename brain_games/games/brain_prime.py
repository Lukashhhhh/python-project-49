from random import randint
import brain_games.engine as engine


def is_prime(number: int) -> str:
    count = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            count += 1
    if count == 1:
        return 'yes'
    return 'no'


def generate_condition() -> int:
    return randint(1, 100)


def game() -> tuple:
    qwestion = generate_condition()
    correct_answer = is_prime(qwestion)
    return qwestion, correct_answer


def main():
    description = ('Answer "yes" if given number is prime.'
                   ' Otherwise answer "no".')
    engine.run_game(game, description)


if __name__ == '__main__':
    main()
