import prompt
from random import randint
from brain_games.cli import welcome_user


def even_number(number: int):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def main():
    flag = False
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string(f'Your answer: ')
        if answer == even_number(number):
            print('Correct!')
            flag = True
            continue
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{even_number(number)}'.")
            print(f"Let's try again, {name}!")
            flag  = False
            break
    if flag:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()

