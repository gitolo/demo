from greeting import greet


def main() -> None:
    user = input("What's your name? ")
    greet(user)


if __name__ == "__main__":
    main()
