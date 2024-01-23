import random


DESCRIPTION = 'What number is missing in the progression?'


def generate_data() -> tuple:
    '''
    Generates an arithmetic progression and skips one number.
    '''
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    question = [str(start + i * step) for i in range(10)]
    miss_index = random.randint(1, 9)
    right_answer, question[miss_index] = question[miss_index], '..'
    question_str = ' '.join(question)
    return question_str, right_answer
