import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    sys.stdout.write("$ ")
    user_input = sys.stdin.readline()
    print(user_input.strip() + " command not found")

    pass


if __name__ == "__main__":
    main()
