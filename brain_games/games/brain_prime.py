from random import randint


def correct_answer(qwestion: str) -> str:
    count = 0
    qwestion = int(qwestion)
    for i in range(1, qwestion // 2 + 1):
        if qwestion % i == 0:
            count += 1
    if count == 1:
        return 'yes'
    return 'no'


def generate_qwestion() -> str:
    return str(randint(1, 100))


description = ('Answer "yes" if given number is prime.'
               ' Otherwise answer "no".')
