from brain_games.cli import welcome_user
import prompt


def run_game(game):
    name = welcome_user()
    print(game.description)
    max_game_rounds = 3
    for _ in range(max_game_rounds):
        qwestion = game.generate_qwestion()
        correct_answer = game.correct_answer(qwestion)
        print(f'Question: {qwestion}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            continue
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was "
                f"'{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
