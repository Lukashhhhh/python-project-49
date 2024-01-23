import random
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_data() -> tuple:
    '''
    Generates random numbers and gcd.
    '''
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f'{number_1} {number_2}'
    right_answer = str(gcd(number_1, number_2))
    return question, right_answer
