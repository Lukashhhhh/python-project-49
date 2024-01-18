from random import randint


def is_even(question: int) -> bool:
    return question % 2 == 0


def generate_data() -> tuple:
    '''
    Generates random number and checks if it is even.
    '''
    question = randint(1, 100)
    right_answer = 'yes' if is_even(question) else 'no'
    return str(question), right_answer


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
