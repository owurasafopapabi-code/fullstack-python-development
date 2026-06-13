def greet_user(name):
    return f"Hello, {name}"


def main():
    user_name = input("Enter your name: ")
    message = greet_user(user_name)
    print(message)


if __name__ == "__main__":
    main()