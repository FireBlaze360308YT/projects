import string
import secrets


def contains_upper(password: str) -> bool:
    for char in password:
        if char in string.ascii_uppercase:
            return True
    return False


def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False


def generate_password(parameter: list) -> str:
    if parameter[0] < 2:
        raise ValueError("Length cannot be lower than 2")

    combination: str = string.ascii_lowercase + string.digits
    password: list[str] = list()

    if parameter[2]:
        password.append(secrets.choice(string.ascii_uppercase))
        combination += string.ascii_uppercase
    if parameter[1]:
        password.append(secrets.choice(string.punctuation))
        combination += string.punctuation

    for _ in range(parameter[0] - len(password)):
        password.append(secrets.choice(combination))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def parameters() -> list:
    length: int = int(input("Enter a length\n>>> "))
    symbols: bool = bool(input("Do u want symbols? 1 for yes, 0 for no\n>>> "))
    uppercase: bool = bool(input("Do u want symbols? 1 for yes, 0 for no\n>>> "))
    num_passwords: int = int(input("How many passwords do u need?\n>>> "))
    return [length, symbols, uppercase, num_passwords]


def main() -> None:
    parameters_list: list = parameters()
    for i in range(1, parameters_list[3] + 1):
        new_pass: str = generate_password(parameters_list)
        specs: str = f"U: {contains_upper(new_pass)}, S: {contains_symbols(new_pass)}"
        print(f"{i} -> {new_pass} ({specs})")
    return None


if __name__ == "__main__":
    main()
