from random import randint
from math import gcd as gsd


def correct_answer(qwestion: str) -> str:
    num1, num2 = qwestion.split()
    num1, num2 = int(num1), int(num2)
    result = gsd(num1, num2)
    return str(result)


def generate_qwestion() -> str:
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    return f'{number_1} {number_2}'


description = 'Find the greatest common divisor of given numbers.'
