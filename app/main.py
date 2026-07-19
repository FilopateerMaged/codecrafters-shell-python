import os
import sys
import subprocess

builtins = ["echo", "exit", "type","pwd","cd"]
bullitins_actions = {
    "echo": lambda args: print(" ".join(args)),
    "exit": lambda args: sys.exit(0),
    "pwd": lambda args: print(current_directory()),
    "type": lambda args: check_builtins("type " + " ".join(args)),
    "cd": lambda args: os.chdir(args[0]) if os.path.isdir(args[0]) else print(f"cd: {args[0]}: No such file or directory")
}


### Base Shell

def read_input():
    sys.stdout.write("$ ")
    sys.stdout.flush()
    command = sys.stdin.readline()
    return command

def execute_command(command):
    if command.strip() == "":
        return
    command_parts = command.strip().split()
    if command_parts[0] in builtins:
        bullitins_actions[command_parts[0]](command_parts[1:])
    else:
        run_executable(command.strip())
    

def check_builtins(command):
    if command.startswith("type "):
        if command.strip()[5:] in builtins:
            print(command.strip()[5:] + " is a shell builtin")
        else:
            if not check_path(command.strip()[5:]):
                print(command.strip()[5:] + ": not found")

def check_path(command,silent=False):
    for dir in os.environ["PATH"].split(os.pathsep):
        file = os.path.join(dir, command.strip())
        if os.path.isfile(file) and os.access(file, os.X_OK):
            if not silent:
                print(command.strip() + " is " + file)
            return file
    return False

        
def run_executable(command):
    command_parts = command.strip().split()
    file_path = check_path(command_parts[0], silent=True)
    if not file_path:
        print(command_parts[0] + ": command not found")
    else:
        # print("Program was passed " + str(len(command_parts)) + " args (including program name).")
        subprocess.run(command_parts)

def exit_shell():
    sys.exit(0)

## Navigation 

def current_directory():
    return os.getcwd()



def main():
    # TODO: Uncomment the code below to pass the first stage

    while True:
        user_input = read_input()
        execute_command(user_input)
            

# 
if __name__ == "__main__":
    main()
