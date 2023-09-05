# shared/common.py

import hashlib

# Define constants for action types
UPLOAD_ACTION = "UPLOAD"
DOWNLOAD_ACTION = "DOWNLOAD"
LIST_ACTION = "LIST"
DELETE_ACTION = "DELETE"
RENAME_ACTION = "RENAME"

# Define a constant for the buffer size used in file transfer
BUFFER_SIZE = 1024

# Define a constant for the server address and port
SERVER_ADDRESS = "localhost"
SERVER_PORT = 12345  # Replace with the actual server port

# Function to display a menu of available actions


def display_menu():
    print("Available Actions:")
    print("1. Upload a file")
    print("2. Download a file")
    print("3. List files on the server")
    print("4. Delete a file on the server")
    print("5. Rename a file on the server")
    print("0. Exit")

# Function to get user input for the action selection


def get_user_action():
    while True:
        try:
            choice = int(input("Enter action number: "))
            if 0 <= choice <= 5:
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid action number.")

# Function to get user input for the filename


def get_filename():
    filename = input("Enter the name of the file: ")
    return filename

# Function to calculate the MD5 hash of a file


def calculate_file_hash(filename):
    md5_hash = hashlib.md5()
    with open(filename, "rb") as file:
        while chunk := file.read(BUFFER_SIZE):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

# Function to validate the MD5 hash of a file


def validate_file_hash(filename, expected_hash):
    calculated_hash = calculate_file_hash(filename)
    return calculated_hash == expected_hash

# ... (other shared functions or constants as needed)
