from random import randint


def is_prime(question: int) -> bool:
    count = 0
    for i in range(1, question // 2 + 1):
        if question % i == 0:
            count += 1
    return count == 1


def generate_data() -> tuple:
    '''
    Generates random number and check if it is prime.
    '''
    question = randint(1, 100)
    right_answer = 'yes' if is_prime(question) else 'no'
    return str(question), right_answer


DESCRIPTION = ('Answer "yes" if given number is prime.'
               ' Otherwise answer "no".')
