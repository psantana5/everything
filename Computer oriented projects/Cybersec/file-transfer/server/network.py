# server/network.py

import os
import socket


def send_file(client_socket, filename):
    try:
        # Check if the file exists
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"The file '{filename}' does not exist.")

        # Send the file size to the client
        file_size = os.path.getsize(filename)
        client_socket.send(str(file_size).encode())

        # Open the file and send its contents in chunks
        with open(filename, "rb") as file:
            chunk_size = 1024
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                client_socket.send(chunk)

    except Exception as e:
        # Handle any exceptions that occur during file transfer
        client_socket.send("ERROR".encode())
        print(f"Error while sending file: {str(e)}")


def receive_file(client_socket, filename):
    try:
        # Receive the file size from the client
        file_size = int(client_socket.recv(1024).decode())

        # Open the file and receive its contents in chunks
        with open(filename, "wb") as file:
            bytes_received = 0
            while bytes_received < file_size:
                chunk = client_socket.recv(1024)
                file.write(chunk)
                bytes_received += len(chunk)

    except Exception as e:
        # Handle any exceptions that occur during file transfer
        print(f"Error while receiving file: {str(e)}")


def receive_action(client_socket):
    try:
        # Receive the action type from the client
        action = client_socket.recv(1024).decode()
        return action
    except Exception as e:
        # Handle any exceptions that occur during action reception
        print(f"Error while receiving action: {str(e)}")


def send_action(client_socket, action):
    try:
        # Send the action type to the client
        client_socket.send(action.encode())
    except Exception as e:
        # Handle any exceptions that occur during action sending
        print(f"Error while sending action: {str(e)}")
