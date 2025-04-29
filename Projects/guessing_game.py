import random
rand = random.randint(1, 100)
attempt = 0
while True:
    guess = int(input('select a number between 1 to 100: '))
    attempt += 1
    if rand > guess:
        print('Wrong! Guess Higher.')
    elif rand < guess:
        print('Wrong! Guess Lower.')
    else:
        print(f'congratulations! Correct Guess in {attempt} times.')
        break