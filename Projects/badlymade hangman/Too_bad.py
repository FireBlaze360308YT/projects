from random import choice


def main() -> None:
    print(f"Welcome to hangman, {input("Whats ur name?\n>>> ").lower()}!")
    word: str = choice(["abck", "dlakberh", "porta", "amincho", "citrus", "daje"])
    num_of_attempts: int = 3
    obscure_word = ["_" for _ in word]

    while True:
        if not obscure_word.count("_"):
            print("you win!")
            break
        print(*obscure_word, sep="")
        choice_d = input("Enter a letter! ")
        if choice_d in word:
            print("Correct")
            obscure_word[word.index(choice_d)] = choice_d
            continue
        num_of_attempts -= 1
        print(f"Wrong, {num_of_attempts} remaining.")
        if num_of_attempts <= 0:
            print("You lost")
            print(word)
            break
    return None


if __name__ == "__main__":
    main()
