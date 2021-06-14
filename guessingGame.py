secret_word = 'techstudio'
guess = ''
guess_count = 0
guess_limit = 3
outOfGuesses = False

while guess != secret_word and not (outOfGuesses):
    if guess_count < guess_limit:
        guess = input('Enter a guess: ').lower()
        guess_count += 1

    else:
        outOfGuesses = True

if outOfGuesses:
    print('You Lose!')
else:
    print('You Win!')