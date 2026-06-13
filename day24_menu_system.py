def show_menu():
    """Display sample manager menu available for user."""
    print()
    print("Sample Manager Menu")
    print("1. Add sample")
    print("2. View samples")
    print("3. Search sample")
    print("4. Exit")


def add_sample():
    print("Add sample selected.")


def view_samples():
    print("View samples selected.")


def search_sample():
    print("Search sample selected.")


def get_user_choice(prompt):
    while True:
        value = input(prompt).strip()

        if value != "":
            return value

        print("Field cannot be empty.")


def interpret_user_menu_option(value):
    if value == "1":
        add_sample()
    elif value == "2":
        view_samples()
    elif value == "3":
        search_sample()
    elif value == "4":
        print("Goodbye.")
        return False
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

    return True


def main():
    while True:
        show_menu()
        choice = get_user_choice("Choose an option: ")

        should_continue = interpret_user_menu_option(choice)

        if should_continue == False:
            break


if __name__ == "__main__":
    main()