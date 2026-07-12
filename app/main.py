import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        user_input = sys.stdin.readline()
        if user_input.strip() == "exit":
            break
        if user_input.startswith("echo "):
            print(user_input.strip()[5:])
        else:
            print(user_input.strip() + ": command not found")

        pass


if __name__ == "__main__":
    main()
