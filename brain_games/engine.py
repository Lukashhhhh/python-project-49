import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run(game):
    name = welcome_user()
    print(game.DESCRIPTION)
    MAX_GAME_ROUNDS = 3
    for _ in range(MAX_GAME_ROUNDS):
        question, correct_answer = game.generate_data()
        print(f'Question: {question}')
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
