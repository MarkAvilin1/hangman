from homeWork.hangman.GameStatus import GameStatus
from homeWork.hangman.Game import Game


def joined_letters(ltr):
    return ''.join(ltr)


game = Game()
word = game.generate_word()
letters_count = len(word)
print(f'The word consists of {letters_count}')
print('Try to guess the word letter by letter.')
while game.game_status == GameStatus.IN_PROGRESS:
    letter = input("Pick a letter.\n")
    state = game.guess_letter(letter)
    print(joined_letters(state))
    print(f'Remaining tries = {game.remaining_tries}')
    print(f'Tried letters: {joined_letters(game.tried_letters)}')
if game.game_status == GameStatus.LOST:
    print("You're hanged!")
    print(f'The word was: {game.word}')
else:
    print('Congratulations! You won!')
