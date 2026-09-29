# Hangman Game 🎯

## Description

This project is a simple **Hangman Game** developed using Python. The player has to guess a hidden word by entering letters one at a time. The game randomly selects a word from a predefined list and provides a limited number of wrong guesses before the game ends.

The program keeps track of guessed letters, displays the progress of the hidden word, and informs the player about correct and incorrect guesses.

## Features

- Random word selection from a predefined word list
- Interactive letter guessing system
- Displays the current progress of the word
- Tracks wrong guesses and remaining attempts
- Prevents repeated guesses
- Validates user input
- Provides win and lose conditions

## Concepts Used

- Python variables and data types
- Lists and string operations
- Conditional statements
- Loops
- User input handling
- Random module
- Basic game logic implementation

## Game Logic

- A random word is selected from the available word list.
- The word is hidden using underscores (`_`).
- The player guesses letters one by one.
- Correct guesses reveal the letter positions in the word.
- Incorrect guesses reduce the remaining attempts.
- The player wins by guessing the complete word before running out of attempts.

## Technologies Used

- **Programming Language:** Python
- **Module Used:** Random
