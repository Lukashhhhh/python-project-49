from random import randint


def is_even(question: int) -> str:
    if question % 2 == 0:
        return 'yes'
    return 'no'


def generate_data() -> tuple:
    '''
    Generates random number and checks if it is even.
    '''
    question = randint(1, 100)
    right_answer = is_even(question)
    return str(question), right_answer


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
