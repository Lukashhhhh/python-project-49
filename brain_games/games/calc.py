import random


DESCRIPTION = 'What is the result of the expression?'


def generate_data() -> tuple:
    '''
    Generates two random numbers and result of the action.
    '''
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    action = random.choice(['+', '-', '*'])
    action_dict = {
        '+': number_1 + number_2,
        '-': number_1 - number_2,
        '*': number_1 * number_2
    }
    question = f'{number_1} {action} {number_2}'
    right_answer = str(action_dict[action])
    return question, right_answer
