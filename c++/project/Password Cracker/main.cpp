#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <openssl/sha.h>

std::string sha256(const std::string& str) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, str.c_str(), str.length());
    SHA256_Final(hash, &sha256);

    std::stringstream ss;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; ++i) {
        ss << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(hash[i]);
    }

    return ss.str();
}

bool checkPassword(const std::string& password, const std::string& targetHash) {
    std::string passwordHash = sha256(password);
    return passwordHash == targetHash;
}

bool crackPassword(const std::string& dictionaryFile, const std::string& targetHash) {
    std::ifstream file(dictionaryFile);
    if (!file) {
        std::cerr << "Error opening dictionary file." << std::endl;
        return false;
    }

    std::string password;
    while (file >> password) {
        if (checkPassword(password, targetHash)) {
            std::cout << "Password cracked! The password is: " << password << std::endl;
            return true;
        }
    }

    std::cout << "Password not found in the dictionary." << std::endl;
    return false;
}

void performBruteForceAttack(const std::string& targetHash) {
    std::string password = "a";
    std::string characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

    while (true) {
        if (checkPassword(password, targetHash)) {
            std::cout << "Password cracked! The password is: " << password << std::endl;
            return;
        }

        // Generate next password permutation
        auto it = std::find(characters.rbegin(), characters.rend(), password.back());
        if (it == characters.rend()) {
            if (password.length() == 8) {
                break;
            }
            password += characters[0];
        } else {
            ++it;
            password.back() = *it;
        }
    }

    std::cout << "Password not found." << std::endl;
}

int main() {
    int choice;
    std::string targetHash;
    std::string dictionaryFile;

    while (true) {
        std::cout << "Menu:" << std::endl;
        std::cout << "1. Dictionary-based attack" << std::endl;
        std::cout << "2. Brute-force attack" << std::endl;
        std::cout << "3. Exit" << std::endl;
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                std::cout << "Enter the dictionary file name: ";
                std::cin >> dictionaryFile;
                crackPassword(dictionaryFile, targetHash);
                break;

            case 2:
                std::cout << "Enter the hash to crack: ";
                std::cin >> targetHash;
                performBruteForceAttack(targetHash);
                break;

            case 3:
                return 0;

            default:
                std::cout << "Invalid choice. Try again." << std::endl;
                break;
        }
    }
}
