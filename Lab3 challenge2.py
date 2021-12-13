# In this challenge, we recreate a simple number guessing game. The rules are
# simple:
# • Python will generate a random answer between 1 and 99 inclusive.
# • The user then has a maximum of 10 attempts to guess the number.
# • If the user guesses correctly, the game is won.
# • If the user guesses too low, a “too low” message is generated.3
# • If the user guesses too high, a “too high” message is generated.
# • If the user enters a number that was previously input, a message “you
# tried that already” is generated and the turn count is not increased.
# • The user can quit the game by entering a guess of -1.
# All use guesses should be stored in a list for convenience.
# To build this game, divide the functionality up into some appropriate functions:
# • generateAnswer()
# • analyseGuess() : should take the user guess as a parameter and
# return -1 if it is too low, -2 is if it is too high and 0 if it is correct.
# • checkPrevious(): should take a list of user guesses and the current
# user guess and return True is the user guess is already in that list, False
# otherwise,
# • main() : to get the game working.
# • See earlier in this document for how to generate random numbers.

import random


def generateAnswer():
    return random.randint(1, 99)


def analyseGuess(guess, answer):
    if guess == answer:
        return 0
    else:
        return -2 if guess > answer else -1


def checkPrevious(guess, guessList):
    return True if guess in guessList else False


def main():
    answer = generateAnswer()
    attempts = 0
    allAttempts = []  # List of all guesses made
    gameOver = False
    guess = 0

    while gameOver == False:
        guess = int(input('Enter your guess: '))
        if guess == -1:
            print('Thanks for playing!')
            gameOver = True
            return

        if checkPrevious(guess, allAttempts) == False:
            allAttempts.append(guess)
            x = analyseGuess(guess, answer)
            if x == 0:
                print('Well done - you win!!')
                gameOver = True
            elif x == -2:
                print('Too high!!')
                attempts += 1
            elif x == -1:
                print('Too low!!')
                attempts += 1

        else:
            print('Tried that already!!!')

        if attempts == 10:
            print('Out of turns!')
            print('The correct answer was: ', answer)
            print('Better luck next time!')
            gameOver = True

if __name__ == '__main__':
    main()