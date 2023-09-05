#include <iostream>
#include <string>
#include <vector>
#include <bcrypt.h>
#include <sqlite3.h>
#include <bcrypt_helper.h>

// Simulated database storing user credentials
struct User {
    std::string username;
    std::string passwordHash;
};

// Simulated database of registered users
std::vector<User> registeredUsers;

// SQLite database connection
sqlite3* db;

// SQLite callback function to retrieve registered users from the database
int RetrieveUsersCallback(void* data, int argc, char** argv, char** colNames)
{
    std::vector<User>& users = *reinterpret_cast<std::vector<User>*>(data);
    users.push_back({ argv[0], argv[1] });
    return 0;
}

// Initialize the SQLite database and create the user table
bool InitializeDatabase()
{
    int rc = sqlite3_open("users.db", &db);
    if (rc != SQLITE_OK) {
        std::cerr << "Failed to open database: " << sqlite3_errmsg(db) << std::endl;
        return false;
    }

    std::string createTableQuery = "CREATE TABLE IF NOT EXISTS users ("
                                   "username TEXT PRIMARY KEY,"
                                   "passwordHash TEXT NOT NULL);";

    char* errMsg;
    rc = sqlite3_exec(db, createTableQuery.c_str(), nullptr, nullptr, &errMsg);
    if (rc != SQLITE_OK) {
        std::cerr << "Failed to create table: " << errMsg << std::endl;
        sqlite3_free(errMsg);
        return false;
    }

    return true;
}

// Simulates user registration and stores the username and hashed password in the database
bool RegisterUser(const std::string& username, const std::string& password)
{
    // Check if the user is already registered
    std::string selectQuery = "SELECT username FROM users WHERE username = '" + username + "';";
    sqlite3_stmt* stmt;
    if (sqlite3_prepare_v2(db, selectQuery.c_str(), -1, &stmt, nullptr) != SQLITE_OK) {
        std::cerr << "Failed to execute select query." << std::endl;
        return false;
    }

    int rc = sqlite3_step(stmt);
    if (rc == SQLITE_ROW) {
        std::cout << "User already exists." << std::endl;
        sqlite3_finalize(stmt);
        return false;
    }
    sqlite3_finalize(stmt);

    // Hash the password using bcrypt
    std::string passwordHash;
    bcrypt_ctx_manager bcryptContextManager;
    bcrypt_ctx* bcryptContext = bcryptContextManager.Create();
    if (bcryptContext == nullptr) {
        std::cerr << "Failed to create bcrypt context." << std::endl;
        return false;
    }

    if (bcrypt_hashpw(password.c_str(), password.length(), bcryptContext, &passwordHash) != 0) {
        std::cerr << "Failed to hash password." << std::endl;
        return false;
    }

    // Store the username and password hash in the database
    std::string insertQuery = "INSERT INTO users (username, passwordHash) VALUES ('" + username + "', '" + passwordHash + "');";
    if (sqlite3_exec(db, insertQuery.c_str(), nullptr, nullptr, nullptr) != SQLITE_OK) {
        std::cerr << "Failed to execute insert query." << std::endl;
        return false;
    }

    std::cout << "User registered successfully." << std::endl;
    return true;
}


bool AuthenticateUser(const std::string& username, const std::string& password)
{
    // Find the user in the database
    std::string selectQuery = "SELECT username, passwordHash FROM users WHERE username = '" + username + "';";
    sqlite3_stmt* stmt;
    if (sqlite3_prepare_v2(db, selectQuery.c_str(), -1, &stmt, nullptr) != SQLITE_OK) {
        std::cerr << "Failed to execute select query." << std::endl;
        return false;
    }

    int rc = sqlite3_step(stmt);
    if (rc != SQLITE_ROW) {
        std::cout << "User not found." << std::endl;
        sqlite3_finalize(stmt);
        return false;
    }

    std::string storedUsername = reinterpret_cast<const char*>(sqlite3_column_text(stmt, 0));
    std::string passwordHash = reinterpret_cast<const char*>(sqlite3_column_text(stmt, 1));
    sqlite3_finalize(stmt);

    // Verify the password using bcrypt
    bcrypt_ctx_manager bcryptContextManager;
    bcrypt_ctx* bcryptContext = bcryptContextManager.Create();
    if (bcryptContext == nullptr) {
        std::cerr << "Failed to create bcrypt context." << std::endl;
        return false;
    }

    if (bcrypt_checkpw(password.c_str(), password.length(), passwordHash.c_str(), bcryptContext) == 0) {
        std::cout << "User authenticated successfully." << std::endl;
        return true;
    }
    else {
        std::cout << "Authentication failed. Invalid password." << std::endl;
        return false;
    }
}

// Cleanup and close the SQLite database connection
void Cleanup()
{
    sqlite3_close(db);
}

int main()
{
    // Initialize the database
    if (!InitializeDatabase()) {
        std::cerr << "Failed to initialize the database." << std::endl;
        return 1;
    }

    // Interactive menu
    int option;
    std::string username, password;
    std::cout << "Secure Chat Application" << std::endl;
    std::cout << "1. Register" << std::endl;
    std::cout << "2. Login" << std::endl;
    std::cout << "Select an option: ";
    std::cin >> option;

    switch (option) {
        case 1:
            std::cout << "Enter username: ";
            std::cin >> username;
            std::cout << "Enter password: ";
            std::cin >> password;
            RegisterUser(username, password);
            break;
        case 2:
            std::cout << "Enter username: ";
            std::cin >> username;
            std::cout << "Enter password: ";
            std::cin >> password;
            AuthenticateUser(username, password);
            break;
        default:
            std::cout << "Invalid option." << std::endl;
            break;
    }

    // Cleanup and close the database connection
    Cleanup();

    return 0;
}
