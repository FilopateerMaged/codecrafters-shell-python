import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    loop = True
    while loop == True:
        sys.stdout.write("$ ")
        user_input = sys.stdin.readline()
        if user_input.strip() == "exit":
            loop = False
        else:
            print(user_input.strip() + ": command not found")

        pass


if __name__ == "__main__":
    main()
