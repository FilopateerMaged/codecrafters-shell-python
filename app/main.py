import os
import sys

builtins = ["echo", "exit", "type"]


def read_input():
    sys.stdout.write("$ ")
    sys.stdout.flush()
    command = sys.stdin.readline()
    return command

def execute_command(command):
    if command.startswith("echo "):
        print(command.strip()[5:])
    elif command.startswith("exit"):
        exit_shell()
    elif command.startswith("type "):
        check_builtins(command)
    else:
        run_executable(command.strip())
    

def check_builtins(command):
    if command.startswith("type "):
        if command.strip()[5:] in builtins:
            print(command.strip()[5:] + " is a shell builtin")
        else:
            if not check_path(command.strip()[5:]):
                print(command.strip()[5:] + ": not found")

def check_path(command):
    for dir in os.environ["PATH"].split(os.pathsep):
        file = os.path.join(dir, command.strip())
        if os.path.isfile(file) and os.access(file, os.X_OK):
            print(command.strip() + " is " + file)
        else:
            return False

        
def run_executable(command):
    command_parts = command.strip().split()
    if not check_path(command_parts[0]):
        print(command_parts[0] + ": command not found")
    else:
        os.execv(command_parts[0], command_parts)


def exit_shell():
    return False



def main():
    # TODO: Uncomment the code below to pass the first stage

    while True:
        user_input = read_input()
        execute_command(user_input)
            

# 
if __name__ == "__main__":
    main()
