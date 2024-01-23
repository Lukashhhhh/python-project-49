import random
from math import sqrt


DESCRIPTION = ('Answer "yes" if given number is prime.'
               ' Otherwise answer "no".')


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def generate_data() -> tuple:
    '''
    Generates random number and check if it is prime.
    '''
    question = random.randint(1, 100)
    right_answer = 'yes' if is_prime(question) else 'no'
    return str(question), right_answer
