import random

# List of predefined words
words = ["python", "computer", "program", "keyboard", "mouse"]

# Choose a random word
word = random.choice(words)

# Game settings
max_wrong_guesses = 6
wrong_guesses = 0
guessed_letters = []

print("Welcome to Hangman Game!")

# Create hidden word display
display = ["_"] * len(word)

while wrong_guesses < max_wrong_guesses:
    print("\nWord:", " ".join(display))
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)
    print("Guessed letters:", guessed_letters)

    guess = input("Guess a letter: ").lower()

    # Check valid input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if letter is in word
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong guess!")
        wrong_guesses += 1

    # Check win condition
    if "_" not in display:
        print("\nCongratulations! You guessed the word:", word)
        break

# Lose condition
if "_" in display:
    print("\nGame Over! The word was:", word)
