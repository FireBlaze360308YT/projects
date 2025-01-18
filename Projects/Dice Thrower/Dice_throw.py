from random import randint
from time import perf_counter


def dice_thrower(num_of_dices: int) -> None:
    result: list[int] = list()
    for _ in range(0, num_of_dices):
        result.append(randint(1, 6))
    print(*result, sep=", ")
    del result


def main() -> None:
    while True:
        print("####################################################")
        number_of_dices: str = input("How many likes would u like to throw? (positive int)\n>>> ").lower()

        if number_of_dices == "exit":
            print("\nThanks for playing!\n")
            break

        if number_of_dices.isdigit() and not int(number_of_dices) == 0:
            number_of_dices: int = int(number_of_dices)
            time_start = perf_counter()
            dice_thrower(num_of_dices=number_of_dices)
            time_end = perf_counter()
            print(f"It took {time_end - time_start:.5f} sec")
            del time_end
            del time_start
            del number_of_dices
            print()
            continue
        print("\n\nInvalid choice!")
    return None


if __name__ == "__main__":
    main()
