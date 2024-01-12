from random import randint
import brain_games.engine as engine


def generate_progression():
    start = randint(1, 10)
    step = randint(1, 10)
    result = []
    for i in range(10):
        result.append(start + i * step)
    miss_index = randint(1, 9)
    miss, result[miss_index] = result[miss_index], '..'
    return result, str(miss)


def game() -> tuple:
    qwestion, correct_answer = generate_progression()
    return qwestion, correct_answer


def main():
    description = 'What number is missing in the progression?'
    engine.run_game(game, description)


if __name__ == '__main__':
    main()
