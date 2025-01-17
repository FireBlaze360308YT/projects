import random as rm
import time as tm
import os

sleep_ = lambda x: tm.sleep(x)
clear = lambda: os.system('cls')

count: int = 0


def game(difficulty: int) -> None:
    global count
    print("##############################################")
    print(f"As u selected, the maximum number will be {difficulty ** 4 + 25}")
    print("##############################################")
    print()
    random_int: int = rm.randint(0, difficulty ** 4 + 25)

    while True:
        choice_int: str = input("Enter a number!\n --> ")

        if not choice_int.isdigit() or int(choice_int) > difficulty ** 4 + 25 or int(choice_int) < 0:
            count += 1
            print("Invalid answer, try again!\n")

            sleep_(0.25)
            clear()
            continue
        if int(choice_int) < random_int:
            count += 1
            print("Too low!\n")

            continue
        if int(choice_int) > random_int:
            count += 1
            print("Too high!\n")

            continue
        if int(choice_int) == random_int:
            count += 1
            print(f"You win in {count} attempts!")
            break

    return None


def main() -> None:
    while True:
        game_mode = input("Select difficulty! (1 to 5): ")
        if not game_mode.isdigit() or not (1 <= int(game_mode) <= 5):
            print("Invalid answer, try again!\n")
            sleep_(0.25)
            clear()
            continue
        game(difficulty=int(game_mode))
        clear()
        break
    return None


if __name__ == "__main__":
    main()
