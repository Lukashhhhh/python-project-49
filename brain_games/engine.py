import prompt


MAX_GAME_ROUNDS = 3


def run(game):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{game.DESCRIPTION}')
    for _ in range(MAX_GAME_ROUNDS):
        question, correct_answer = game.generate_data()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
