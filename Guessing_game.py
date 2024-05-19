#Generate a random number between 1 and 10000 (including 1 and 10000). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random
# Generate a random number
a = random.randint(1,10001)

#Initiate the variables

guess = 0
count = 0

while guess != a and guess != 'exit':
    guess = input('enter your guess between 1 to 10000:')

    if guess == 'exit':
        break
    
    guess = int(guess)
    count += 1

    if guess < a:
        print(' guess is too low')
    elif guess > a:
        print(' guess is too high')
    else:
        print('Guess is correct')
        print(' You took only', count , "attemps to guess a number")

