import random

# Create a random number between 1 and 100
num = random.randint(1, 100)
# Set the guess value to -1
guess = -1

print('Welcome to HI - LO game')

while guess != num:
    guess_text = input('Guess a number between 1 & 100: ')
    guess = int(guess_text)

    if guess < num:
        print('Too low!')
    elif guess > num:
        print('Too high!')
    else:
        print('Got it: The number is ' + str(num))
