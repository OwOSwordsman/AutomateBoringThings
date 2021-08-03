# guess the number
import random

def main():
    displayIntro()
    startGame()


def displayIntro():
    name = input('What is your name? ')
    print(f'Hello, {name}!')


def startGame():
    print('Try and guess my number that is between 1 and 20.')
    num = random.randint(1, 20)
    game(num, 1)


def game(num, attempts):
    # guessed too many times
    if attempts > 5:
        print(f'You ran out of attempts. The correct number was {num}')
        return

    # get guess and check for valid guess
    guess = 0
    while guess < 1 or guess > 20:
        try:
            guess = int(input('Enter your guess: '))
        except ValueError:
            guess = 0

    if guess == num:    # correct guess
        print(f'You have guessed my number in {attempts} attempts')
    elif guess > num:   # guess too high
        print('Your guess was too high')
        game(num, attempts + 1)
    else:   # guess too low
        print('Your guess was too low')
        game(num, attempts + 1)


if __name__ == '__main__':
    main()
