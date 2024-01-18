from random import randint


def generate_data() -> tuple:
    '''
    Generates an arithmetic progression and skips one number.
    '''
    start = randint(1, 10)
    step = randint(1, 10)
    question = []
    for i in range(10):
        question.append(str(start + i * step))
    miss_index = randint(1, 9)
    right_answer, question[miss_index] = question[miss_index], '..'
    return question, right_answer


DESCRIPTION = 'What number is missing in the progression?'
