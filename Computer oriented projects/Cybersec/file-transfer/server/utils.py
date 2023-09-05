# server/utils.py

import hashlib


def calculate_file_hash(filename):
    # Calculate the MD5 hash of a file to verify data integrity
    md5_hash = hashlib.md5()
    with open(filename, "rb") as file:
        while chunk := file.read(8192):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()


def validate_file_hash(filename, expected_hash):
    # Validate the MD5 hash of a file against the expected hash
    calculated_hash = calculate_file_hash(filename)
    return calculated_hash == expected_hash
