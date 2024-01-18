from random import randint


def is_prime(question: int) -> str:
    count = 0
    for i in range(1, question // 2 + 1):
        if question % i == 0:
            count += 1
    if count == 1:
        return 'yes'
    return 'no'


def generate_data() -> tuple:
    '''
    Generates random number and check if it is prime.
    '''
    question = randint(1, 100)
    right_answer = is_prime(question)
    return str(question), right_answer


DESCRIPTION = ('Answer "yes" if given number is prime.'
               ' Otherwise answer "no".')
