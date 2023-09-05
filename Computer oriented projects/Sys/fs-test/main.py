import os


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}


class File:
    def __init__(self, name, contents, parent=None):
        self.name = name
        self.contents = contents
        self.parent = parent


class FileSystemItem:
    def __init__(self, name, parent, is_dir=False):
        self.name = name
        self.parent = parent
        self.is_dir = is_dir


class FileSystem:
    def __init__(self):
        self.root = Directory('')
        self.current_dir = self.root

    def split_path(self, path):
        return path.split('/')

    def get_node(self, path):
        if path[0] == '/':
            dir_ = self.root
            tokens = self.split_path(path[1:])
        else:
            dir_ = self.current_dir
            tokens = self.split_path(path)
        for token in tokens:
            if token == '..':
                if dir_.parent is not None:
                    dir_ = dir_.parent
            else:
                dir_ = dir_.children.get(token)
                if dir_ is None:
                    return None
        return dir_

    def create(self, path, contents=None):
        if path[0] == '/':
            dir_ = self.root
            tokens = self.split_path(path[1:])
        else:
            dir_ = self.current_dir
            tokens = self.split_path(path)
        for token in tokens[:-1]:
            if token not in dir_.children:
                return 'Directory does not exist'
            dir_ = dir_.children[token]
        if tokens[-1] in dir_.children:
            return 'File or Directory already exists'
        if contents is None:
            dir_.children[tokens[-1]] = Directory(tokens[-1], dir_)
        else:
            dir_.children[tokens[-1]] = File(tokens[-1], contents, dir_)
        return 'File or Directory created'

    def read(self, path):
        node = self.get_node(path)
        if node is None:
            return 'File or Directory does not exist'
        if isinstance(node, File):
            return node.contents
        else:
            return 'Cannot read a directory'

    def update(self, path, contents):
        node = self.get_node(path)
        if node is None:
            return 'File or Directory does not exist'
        if isinstance(node, File):
            node.contents = contents
            return 'File updated'
        else:
            return 'Cannot update a directory'

    def delete(self, path):
        node = self.get_node(path)
        if node is None:
            return 'File or Directory does not exist'
        if node.parent is not None:
            del node.parent.children[node.name]
            return 'File or Directory deleted'
        else:
            return 'Cannot delete root directory'

    def change_dir(self, path):
        dir_ = self.get_node(path)
        if dir_ is None:
            return 'Directory does not exist'
        if isinstance(dir_, Directory):
            self.current_dir = dir_
            return 'Changed directory'
        else:
            return 'Cannot cd into a file'

    def move(self, source_path, dest_path):
        node = self.get_node(source_path)
        if node is None:
            return 'File or Directory does not exist'
        if node.parent is None:
            return 'Cannot move root directory'
        del node.parent.children[node.name]
        tokens = self.split_path(dest_path)
        dir_ = self.get_node('/'.join(tokens[:-1]))
        if dir_ is None:
            return 'Destination directory does not exist'
        dir_.children[tokens[-1]] = node
        node.name = tokens[-1]
        node.parent = dir_
        return 'File or Directory moved'

    def list_dir(self, path='.'):
        dir_ = self.get_node(path)
        if dir_ is None:
            return 'Directory does not exist'
        if isinstance(dir_, Directory):
            return [child.name for child in dir_.children.values()]
        else:
            return 'Cannot list a file'

    def current_path(self):
        path = []
        dir_ = self.current_dir
        while dir_.parent is not None:
            path.append(dir_.name)
            dir_ = dir_.parent
        return '/' + '/'.join(reversed(path))


def clear_screen():
    # The command for clearing the screen will be different depending on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Mac and Linux
        os.system('clear')


def cli():
    fs = FileSystem()
    print("Welcome to the FileSystem Simulator. Type 'help' to list available commands.\n")

    while True:
        command = input("FS $ ").split()
        if len(command) == 0:
            continue
        operation = command[0]
        operands = command[1:]

        try:
            if operation == 'exit':
                print("Exiting... Thank you for using the FileSystem Simulator.")
                break
            elif operation == 'help':
                print("""
                      touch [file path] : Creates a new file.
                      nano [file path] : Edits the contents of a file. Use ':' to specify new contents.
                      mkdir [dir path] : Creates a new directory.
                      cat [file path] : Prints the contents of a file.
                      rm [path] : Deletes a file or directory.
                      cd [dir path] : Changes the current directory.
                      mv [source path] [destination path] : Moves a file or directory.
                      ls [dir path] : Lists the contents of a directory. If no path is specified, lists the current directory.
                      pwd : Prints the current directory path.
                      clear : Clears the screen.
                      exit : Exits the program.
                      help : Prints this help text.
                      """)

            elif operation == 'touch':
                print(fs.create(' '.join(operands)))
            elif operation == 'nano':
                path_contents = ' '.join(operands).split(':')
                path = path_contents[0]
                contents = None if len(
                    path_contents) == 1 else path_contents[1]
                print(fs.update(path.strip(), contents))
            elif operation == 'mkdir':
                print(fs.create(' '.join(operands)))
            elif operation == 'cat':
                print(fs.read(' '.join(operands)))
            elif operation == 'rm':
                print(fs.delete(' '.join(operands)))
            elif operation == 'cd':
                print(fs.change_dir(' '.join(operands)))
            elif operation == 'mv':
                source_dest = ' '.join(operands).split()
                if len(source_dest) < 2:
                    print("Please provide both source and destination paths.")
                else:
                    source = source_dest[0]
                    destination = source_dest[1]
                    print(fs.move(source, destination))
            elif operation == 'ls':
                path = ' '.join(operands)
                if path == '':
                    path = '.'  # Use '.' to represent the current directory
                print(fs.list_dir(path))
            elif operation == 'pwd':
                print(fs.current_path())
            elif operation == 'clear':
                clear_screen()
            else:
                print(
                    f"Unknown command: {operation}. Type 'help' for a list of commands.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


cli()
