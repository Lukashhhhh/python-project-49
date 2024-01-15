from random import randint, choice
import brain_games.engine as engine


def answer(num1: int, num2: int, action: str) -> str:
    action_dict = {'+': num1 + num2, '-': num1 - num2, '*': num1 * num2}
    return str(action_dict[action])


def generate_condition() -> tuple:
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    action = choice(['+', '-', '*'])
    cor_answer = answer(number_1, number_2, action)
    return f'{number_1} {action} {number_2}', cor_answer


def game() -> tuple:
    qwestion, correct_answer = generate_condition()
    return qwestion, correct_answer


def main():
    description = 'What is the result of the expression?'
    engine.run_game(game, description)


if __name__ == '__main__':
    main()
