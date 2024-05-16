
import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['-'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = list()

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        
    def ask_for_input(self):
        while True:
            guess = input('Guess a letter in the word')
            if not len(guess) == 1 and guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


if __name__ == '__main__':
    hangman = Hangman(word_list=['apple', 'pair'])
    hangman.ask_for_input()





