from milestone_2 import word

def ask_for_input_letter():
    while True:
        guess = input('Please provide a single letter')
        if len(guess) == 1 and guess.isalpha():
            break
        print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

if __name__ == '__main__':
    ask_for_input_letter()
