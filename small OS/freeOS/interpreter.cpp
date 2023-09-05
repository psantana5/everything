#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <netinet/ip.h>
#include <netinet/ip_icmp.h>

// ICMP header structure
struct ICMPHeader
{
    uint8_t type;
    uint8_t code;
    uint16_t checksum;
    uint16_t identifier;
    uint16_t sequenceNumber;
};

// Function to calculate the ICMP checksum
uint16_t calculateChecksum(const uint16_t *data, size_t length)
{
    uint32_t sum = 0;
    while (length > 1)
    {
        sum += *data++;
        length -= 2;
    }
    if (length == 1)
    {
        sum += *reinterpret_cast<const uint8_t *>(data);
    }
    sum = (sum >> 16) + (sum & 0xFFFF);
    sum += (sum >> 16);
    return static_cast<uint16_t>(~sum);
}

// Function to send an ICMP echo request
void sendICMPEchoRequest(const std::string &ipAddress)
{
    // Create a raw socket for sending ICMP packets
    int rawSocket = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
    if (rawSocket < 0)
    {
        std::cerr << "Failed to create raw socket" << std::endl;
        return;
    }

    // Set the destination IP address
    sockaddr_in destination;
    std::memset(&destination, 0, sizeof(destination));
    destination.sin_family = AF_INET;
    if (inet_pton(AF_INET, ipAddress.c_str(), &(destination.sin_addr)) <= 0)
    {
        std::cerr << "Invalid IP address: " << ipAddress << std::endl;
        close(rawSocket);
        return;
    }

    // Create an ICMP echo request packet
    ICMPHeader icmpHeader;
    std::memset(&icmpHeader, 0, sizeof(icmpHeader));
    icmpHeader.type = 8; // ICMP echo request
    icmpHeader.code = 0;
    icmpHeader.identifier = htons(getpid());
    icmpHeader.sequenceNumber = htons(1);
    icmpHeader.checksum = calculateChecksum(reinterpret_cast<uint16_t *>(&icmpHeader), sizeof(icmpHeader));

    // Send the ICMP packet
    ssize_t bytesSent = sendto(rawSocket, &icmpHeader, sizeof(icmpHeader), 0, reinterpret_cast<sockaddr *>(&destination), sizeof(destination));
    if (bytesSent < 0)
    {
        std::cerr << "Failed to send ICMP packet" << std::endl;
    }

    // Close the raw socket
    close(rawSocket);
}

// Function to execute the ping command
void executePingCommand(const std::string &ipAddress)
{
    std::cout << "Pinging " << ipAddress << "..." << std::endl;

    // Send ICMP echo requests
    for (int i = 0; i < 4; ++i)
    {
        sendICMPEchoRequest(ipAddress);
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
}

// Function to execute the command
void executeCommand(const std::string &command)
{
    // Split the command into tokens
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(command);
    while (std::getline(tokenStream, token, ' '))
    {
        tokens.push_back(token);
    }

    // Check the command and execute corresponding actions
    if (tokens.empty())
    {
        // Empty command, do nothing
        return;
    }
    else if (tokens[0] == "ping")
    {
        // Handle the ping command
        if (tokens.size() >= 2)
        {
            std::string ipAddress = tokens[1];
            executePingCommand(ipAddress);
        }
        else
        {
            std::cout << "Invalid usage of ping command. Usage: ping <ip_address>" << std::endl;
        }
    }
    else if (tokens[0] == "help")
    {
        // Handle the help command
        std::cout << "Available commands:" << std::endl;
        std::cout << "ping <ip_address> - Send ICMP echo requests to the specified IP address" << std::endl;
        std::cout << "help - Display available commands" << std::endl;
        // Add more commands and their descriptions as needed
    }
    else
    {
        // Unknown command
        std::cout << "Unknown command: " << tokens[0] << std::endl;
    }
}