from random import randint
from math import gcd as gcd


def generate_data() -> tuple:
    '''
    Generates random numbers and gcd.
    '''
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    question = f'{number_1} {number_2}'
    right_answer = str(gcd(number_1, number_2))
    return question, right_answer


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
