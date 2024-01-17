from random import randint


def correct_answer(qwestion: str) -> str:
    if int(qwestion) % 2 == 0:
        return 'yes'
    return 'no'


def generate_qwestion() -> str:
    return str(randint(1, 100))


description = 'Answer "yes" if the number is even, otherwise answer "no".'
