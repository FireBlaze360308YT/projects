import random as rm
import time as tm
import os


def sleep_(seconds: float) -> None:
    """Sleep for the given number of seconds."""
    tm.sleep(seconds)


def clear() -> None:
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_valid_input(min_val: int, max_val: int) -> int:
    """Helper function to get valid user input within the given range."""
    while True:
        user_input = input(f"Enter a number between {min_val} and {max_val}: ").strip()
        if user_input.isdigit() and min_val <= int(user_input) <= max_val:
            return int(user_input)
        print(f"Invalid input! Please enter a valid number between {min_val} and {max_val}.")
        sleep_(0.5)
        clear()


def game(difficulty: int) -> None:
    """Game logic where user guesses a number."""
    max_number = difficulty ** 4 + 25
    print("##############################################")
    print(f"As you selected, the maximum number will be {max_number}")
    print("##############################################\n")

    random_int = rm.randint(0, max_number)
    attempts = 0

    while True:
        user_guess = get_valid_input(0, max_number)
        attempts += 1

        if user_guess < random_int:
            print("Too low! Try again.\n")
        elif user_guess > random_int:
            print("Too high! Try again.\n")
        else:
            print(f"You win in {attempts} attempts!")
            break


def main() -> None:
    """Main function to select game difficulty and start the game."""
    while True:
        game_mode = input("Select difficulty (1 to 5): ").strip()

        if game_mode.isdigit() and 1 <= int(game_mode) <= 5:
            game(difficulty=int(game_mode))
            break

        print("Invalid answer, try again!")
        sleep_(0.5)
        clear()


if __name__ == "__main__":
    main()
