# client/client.py

import os
import socket

# Function to establish a connection with the server


def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Replace with the actual server address and port
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)
    return client_socket

# Function to send an action to the server


def send_action(client_socket, action):
    try:
        client_socket.send(action.encode())
    except Exception as e:
        print(f"Error while sending action: {str(e)}")

# Function to receive a response from the server


def receive_response(client_socket):
    try:
        response = client_socket.recv(1024).decode()
        return response
    except Exception as e:
        print(f"Error while receiving response: {str(e)}")

# Function to upload a file to the server


def upload_file(client_socket, filename):
    try:
        if not os.path.isfile(filename):
            print(f"The file '{filename}' does not exist.")
            return

        send_action(client_socket, "UPLOAD")
        client_socket.send(filename.encode())
        with open(filename, "rb") as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                client_socket.send(data)
        print(f"File '{filename}' uploaded successfully.")

    except Exception as e:
        print(f"Error while uploading file: {str(e)}")

# Function to download a file from the server


def download_file(client_socket, filename):
    try:
        send_action(client_socket, "DOWNLOAD")
        client_socket.send(filename.encode())
        response = receive_response(client_socket)

        if response == "ERROR":
            print(f"File '{filename}' not found on the server.")
            return

        with open(filename, "wb") as file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)
        print(f"File '{filename}' downloaded successfully.")

    except Exception as e:
        print(f"Error while downloading file: {str(e)}")

# ... (other client-side functions)


if __name__ == "__main__":
    client_socket = connect_to_server()

    while True:
        print("Available Actions:")
        print("1. Upload a file")
        print("2. Download a file")
        print("3. List files on the server")
        print("4. Delete a file on the server")
        print("5. Rename a file on the server")
        print("0. Exit")

        choice = input("Enter action number: ")

        if choice == "1":
            filename = input("Enter the name of the file to upload: ")
            upload_file(client_socket, filename)
        elif choice == "2":
            filename = input("Enter the name of the file to download: ")
            download_file(client_socket, filename)
        elif choice == "3":
            # Implement the function to list files on the server (if available)
            pass
        elif choice == "4":
            # Implement the function to delete a file on the server (if available)
            pass
        elif choice == "5":
            # Implement the function to rename a file on the server (if available)
            pass
        elif choice == "0":
            client_socket.close()
            break
        else:
            print("Invalid choice. Please try again.")
