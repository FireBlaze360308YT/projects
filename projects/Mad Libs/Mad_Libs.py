def get_input(word_type: str) -> str:
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input


def game_mode() -> int:
    while True:
        game_mode_choice = input("Enter 1 for fast, 2 for medium and 3 for slow game_mode!\n")
        if game_mode_choice.isdigit() and 1 <= int(game_mode_choice) <= 3:
            return int(game_mode_choice)
        print("Invalid choice! Try again.")
        print("#############################################################################")


def story(*args) -> str:
    story_str = f"""
        Once upon a time, there was a {args[5] if args[5] else ""} {args[0]} who loved to {args[1]} all day.

        One day, {args[2]} walked into the {args[4] if args[4] else "room"} and caught the {args[5] if args[5] else ""} {args[0]} in the act.

        {args[2]}: "What are you doing?"
        {args[0]}: "I'm just {args[1]}ing, what's the {args[7] if args[7] else "big"} deal?"
        {args[2]}: "Well, it's not every day that you see a {args[5] if args[5] else ""} {args[0]} {args[1]}ing in the middle of the {args[4] if args[4] else "day"}."
        {args[0]}: "I guess you're right {args[5] if args[5] else ""}. Maybe I should take a {args[6] if args[6] else "break"}."
        {args[2]}: "That's probably a {args[7] if args[7] else "good"} idea. Why don't we go {args[3]} instead?"
        {args[0]}: "Sure, that sounds like {args[6] if args[6] else "fun"}!"

        And so, {args[2]} and the {args[5] if args[5] else ""} {args[0]} went off to {args[3]} and had a great time.
        The end.
        """
    return story_str


def main() -> None:
    match game_mode():
        case 1:
            nuon1 = get_input("noun")
            verb1 = get_input("verb")
            nuon2 = get_input("noun")
            verb2 = get_input("verb")
            print(story(nuon1, verb1, nuon2, verb2))
        case 2:
            nuon1 = get_input("noun")
            verb1 = get_input("verb")
            nuon2 = get_input("noun")
            verb2 = get_input("verb")
            nuon3 = get_input("noun")
            adjective = get_input("adjective")
            print(story(nuon1, verb1, nuon2, verb2, nuon3, adjective))
        case 3:
            nuon1 = get_input("noun")
            verb1 = get_input("verb")
            nuon2 = get_input("noun")
            verb2 = get_input("verb")
            nuon3 = get_input("noun")
            adjective = get_input("adjective")
            idk = get_input("Get creative")
            dad = get_input("???")
            print(story(nuon1, verb1, nuon2, verb2, nuon3, adjective, idk, dad))


if __name__ == "__main__":
    main()
