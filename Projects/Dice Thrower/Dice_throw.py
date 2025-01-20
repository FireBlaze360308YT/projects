from random import randint
from time import perf_counter


def dice_thrower(num_of_dices: int) -> None:
    result = [randint(1, 6) for _ in range(num_of_dices)]  # List comprehension for efficiency
    print(*result, sep=", ")

    
def main() -> None:
    while True:
        print("####################################################")
        number_of_dices = input("How many dice would you like to throw? (positive int or 'exit' to quit)\n>>> ").strip().lower()

        if number_of_dices == "exit":
            print("\nThanks for playing!\n")
            break

        # Check for valid positive integer input
        if number_of_dices.isdigit() and int(number_of_dices) > 0:
            number_of_dices = int(number_of_dices)
            time_start = perf_counter()
            dice_thrower(num_of_dices=number_of_dices)
            time_end = perf_counter()
            print(f"It took {time_end - time_start:.5f} sec\n")
        else:
            print("\nInvalid choice! Please enter a positive integer or 'exit' to quit.\n")


if __name__ == "__main__":
    main()
