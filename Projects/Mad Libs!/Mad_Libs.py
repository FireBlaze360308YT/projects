def get_input(word_type: str) -> str:
    return input(f"Enter a {word_type}: ").strip()


def game_mode() -> int:
    while True:
        game_mode_choice = input("Enter 1 for fast, 2 for medium, and 3 for slow game mode: ").strip()
        if game_mode_choice.isdigit() and 1 <= int(game_mode_choice) <= 3:
            return int(game_mode_choice)
        print("Invalid choice! Try again.\n" + "#" * 77)


def story(*args) -> str:
    # Provide default values for missing args directly in the story string
    default_values = {
        5: "",
        4: "room",
        7: "big",
        6: "break",
        3: "fun"
    }
    
    # Replace any missing arguments with default values
    args = [arg if arg else default_values.get(i, "") for i, arg in enumerate(args)]
    
    # Construct the story
    return f"""
        Once upon a time, there was a {args[5]} {args[0]} who loved to {args[1]} all day.

        One day, {args[2]} walked into the {args[4]} and caught the {args[5]} {args[0]} in the act.

        {args[2]}: "What are you doing?"
        {args[0]}: "I'm just {args[1]}ing, what's the {args[7]} deal?"
        {args[2]}: "Well, it's not every day that you see a {args[5]} {args[0]} {args[1]}ing in the middle of the {args[4]}."
        {args[0]}: "I guess you're right {args[5]}. Maybe I should take a {args[6]}."
        {args[2]}: "That's probably a {args[7]} idea. Why don't we go {args[3]} instead?"
        {args[0]}: "Sure, that sounds like {args[6]}!"

        And so, {args[2]} and the {args[5]} {args[0]} went off to {args[3]} and had a great time.
        The end.
    """


def main() -> None:
    game_mode_choice = game_mode()
    
    inputs_needed = [
        ("noun", "verb", "noun", "verb"),
        ("noun", "verb", "noun", "verb", "noun", "adjective"),
        ("noun", "verb", "noun", "verb", "noun", "adjective", "creative", "???")
    ]

    # Loop through the corresponding input fields based on the selected game mode
    inputs = [get_input(word_type) for word_type in inputs_needed[game_mode_choice - 1]]
    
    # Print the story based on the inputs collected
    print(story(*inputs))


if __name__ == "__main__":
    main()
