import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    builtins = ["echo", "exit", "type"]

    while True:
        sys.stdout.write("$ ")
        user_input = sys.stdin.readline()
        if user_input.strip() == "exit":
            break
        elif user_input.startswith("echo "):
            print(user_input.strip()[5:])
        elif user_input.startswith("type "):
            if user_input.strip()[5:] in builtins:
                print(user_input.strip()[5:] + " is a shell builtin")
            else:
                print(user_input.strip()[5:] + ": not found")
        else:
            print(user_input.strip() + ": command not found")

        pass


if __name__ == "__main__":
    main()
