import random
import time


def print_welcome_message() -> None:
    """Display a welcoming message and get the player's name."""
    name = input("What's your name?\n>>> ").strip().title()
    print(f"Welcome to Hangman, {name}!\n")
    time.sleep(1)
    return name


def select_word() -> str:
    """Randomly select a word for the game."""
    words = ["abck", "dlakberh", "porta", "amincho", "citrus", "daje"]
    word = random.choice(words)
    return word


def display_word(obscured_word: list) -> None:
    """Display the current state of the word with blanks."""
    print(" ".join(obscured_word))


def get_guess() -> str:
    """Prompt the player to enter a letter and validate the input."""
    while True:
        guess = input("Enter a letter: ").lower().strip()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Please enter a valid single letter.")


def update_obscured_word(word: str, obscured_word: list, guess: str) -> bool:
    """Update the obscured word if the guess is correct and return whether the guess was correct."""
    correct_guess = False
    for i, letter in enumerate(word):
        if letter == guess and obscured_word[i] == "_":
            obscured_word[i] = guess
            correct_guess = True
    return correct_guess


def hangman_graphic(attempts_left: int) -> None:
    """Display a hangman graphic based on the number of attempts left."""
    graphics = [
        """
         ------
         |    |
              |
              |
              |
              |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
              |
              |
              |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
         |    |
              |
              |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
        /|    |
              |
              |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
        /|\   |
              |
              |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
        /|\   |
        /     |
              |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
        /|\   |
        / \   |
              |
              |
        =========
        """
    ]
    print(graphics[6 - attempts_left])


def main() -> None:
    """Main function to run the Hangman game."""
    name = print_welcome_message()
    word = select_word()
    attempts_left = 6
    obscured_word = ["_" for _ in word]
    guessed_letters = set()

    while attempts_left > 0:
        display_word(obscured_word)
        print(f"Attempts remaining: {attempts_left}")
        hangman_graphic(attempts_left)

        # Get the player's guess
        guess = get_guess()

        # If the guess has already been made, prompt again
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'! Try another letter.\n")
            continue

        guessed_letters.add(guess)

        # Update the word and check if the guess was correct
        if update_obscured_word(word, obscured_word, guess):
            print("Correct guess!\n")
        else:
            attempts_left -= 1
            print(f"Wrong guess! '{guess}' is not in the word.\n")

        # Check if the player has guessed all the letters
        if "_" not in obscured_word:
            print(f"Congratulations {name}, you win!")
            display_word(obscured_word)
            break
    else:
        print(f"You've run out of attempts, {name}. The word was: {word}")
        hangman_graphic(attempts_left)


if __name__ == "__main__":
    main()
