from random import randint
import brain_games.engine as engine
from math import gcd as gsd


def find_gcd(numbers: tuple) -> str:
    num1, num2 = numbers
    result = gsd(num1, num2)
    return str(result)


def game() -> tuple:
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    qwestion = f'{number_1} {number_2}'
    correct_answer = find_gcd((number_1, number_2))
    return qwestion, correct_answer


def main():
    description = 'Find the greatest common divisor of given numbers.'
    engine.run_game(game, description)


if __name__ == '__main__':
    main()
