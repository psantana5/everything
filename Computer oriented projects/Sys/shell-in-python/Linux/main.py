import os
import stat
import subprocess
import shlex
from cmd import Cmd

class SecureAdvancedShell(Cmd):
    prompt = '> '

    def __init__(self):
        super().__init__()
        self.command_history = []

    def default(self, line):
        """Executes command in a safer manner."""
        commands = line.split('&&')
        for command in commands:
            try:
                self.onecmd(command.strip())
            except Exception as e:
                print(f"Unexpected error executing the command: {e}")
                break

    def do_exit(self, args):
        """Exits from the console"""
        return True

    do_quit = do_exit

    def help_exit(self):
        print("Exits the console. You can also use the 'quit' command.")

    def help_quit(self):
        print("Exits the console. You can also use the 'exit' command.")

    def run_command(self, command):
        """Executes the given command securely."""
        args = shlex.split(command)

        try:
            result = subprocess.run(args, check=True, text=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            print(f"Command '{command}' failed with error: {e}")
            return
        except Exception as e:
            print(f"Unexpected error while executing command: {e}")
            return

        print(result.stdout)

        self.command_history.append(command)

    def do_history(self, args):
        """Shows command history"""
        for i, command in enumerate(self.command_history, 1):
            print(f"{i}: {command}")

    def help_history(self):
        print("Shows the command history.")

    def do_mkdir(self, args):
        """Creates a directory"""
        try:
            os.mkdir(args)
            print(f"Directory '{args}' created.")
        except Exception as e:
            print(f"Error creating directory: {e}")

    def help_mkdir(self):
        print("Creates a directory. Usage: mkdir directory_name")

    def do_rmdir(self, args):
        """Removes a directory"""
        try:
            os.rmdir(args)
            print(f"Directory '{args}' removed.")
        except Exception as e:
            print(f"Error removing directory: {e}")

    def help_rmdir(self):
        print("Removes a directory. Usage: rmdir directory_name")

    def do_touch(self, args):
        """Creates a file"""
        try:
            with open(args, 'a'):
                os.utime(args, None)
            print(f"File '{args}' created.")
        except Exception as e:
            print(f"Error creating file: {e}")

    def help_touch(self):
        print("Creates a file. Usage: touch file_name")

    def do_rm(self, args):
        """Removes a file"""
        try:
            os.remove(args)
            print(f"File '{args}' removed.")
        except Exception as e:
            print(f"Error removing file: {e}")

    def help_rm(self):
        print("Removes a file. Usage: rm file_name")

    def do_ls(self, args):
        """Lists files in a directory with their permissions"""
        try:
            path = args if args else '.'
            for file in os.listdir(path):
                permissions = os.stat(os.path.join(path, file)).st_mode
                permissions_str = stat.filemode(permissions)
                print(f"{permissions_str} {file}")
        except Exception as e:
            print(f"Error listing files: {e}")

    def help_ls(self):
        print("Lists files in a directory with their permissions. Usage: ls [directory_path]")

    def do_clear(self, args):
        """Clears the console."""
        subprocess.run(['clear'], shell=True)

    def help_clear(self):
        print("Clears the console. Usage: clear")

    def precmd(self, line):
        line = line.lower()
        if line == 'quit' or line == 'exit':
            return 'exit'
        return line

if __name__ == "__main__":
    print("Secure Advanced Shell. Type 'exit' or 'quit' to leave. Use 'history' to see command history.")
    shell = SecureAdvancedShell()
    shell.cmdloop()
