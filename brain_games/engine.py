from brain_games.cli import welcome_user
import prompt


def run_game(game, description: str):
    name = welcome_user()
    print(description)
    flag = False
    for _ in range(3):
        qwestion, correct_answer = game()
        print(f'Question: {qwestion}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            flag = True
            continue
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was "
                f"'{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            flag = False
            break
    if flag:
        print(f"Congratulations, {name}!")
