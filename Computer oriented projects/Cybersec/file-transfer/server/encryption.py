# server/encryption.py

from cryptography.fernet import Fernet


def generate_key():
    # Generate a new encryption key
    return Fernet.generate_key()


def encrypt_message(key, message):
    # Encrypt the message using the provided key
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message


def decrypt_message(key, encrypted_message):
    # Decrypt the encrypted message using the provided key
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message
