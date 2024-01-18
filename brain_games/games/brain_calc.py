from random import randint, choice


def generate_data() -> tuple:
    '''
    Generates two random numbers and result of the action.
    '''
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    action = choice(['+', '-', '*'])
    action_dict = {
        '+': number_1 + number_2,
        '-': number_1 - number_2,
        '*': number_1 * number_2
    }
    question = f'{number_1} {action} {number_2}'
    rigth_answer = str(action_dict[action])
    return question, rigth_answer


DESCRIPTION = 'What is the result of the expression?'
