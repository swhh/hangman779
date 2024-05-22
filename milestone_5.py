
import random

class Hangman:
    '''Hangman class lets you guess a word'''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['-'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = list()

    def _check_guess(self, guess):
        '''Check if guess in word; if in word, decrement num_letters; else, decrement num_lives'''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        
    def ask_for_input(self):
        '''Asks user for a letter via standard input and checks if in self.word'''
        while True:
            guess = input('Guess a letter in the word: ')
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self._check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    """Plays game using the Hangman class"""
    num_lives = 5
    game = Hangman(word_list=word_list, num_lives=num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and game.num_letters == 0:
            print('Congratulations. You won the game!')
            break

if __name__ == '__main__':
    word_list = ['apple', 'pear', 'banana', 'mango']
    play_game(word_list)







