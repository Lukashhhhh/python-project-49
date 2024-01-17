from random import randint, choice


def correct_answer(qwestion: str) -> str:
    num1, action, num2 = qwestion.split()
    num1, num2 = int(num1), int(num2)
    action_dict = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2
    }
    return str(action_dict[action])


def generate_qwestion() -> str:
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    action = choice(['+', '-', '*'])
    return f'{number_1} {action} {number_2}'


description = 'What is the result of the expression?'
