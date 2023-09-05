#include <iostream>
#include <conio.h>
#include <fstream>
#include <regex>

// Función para gestionar teclas presionadas
void handleKeyPress(char key)
{
    // Print the pressed key
    std::cout << "Tecla presionada: " << key << std::endl;

    // lógica para manejar la tecla presionada
}

// Function to handle key releases
void handleKeyRelease(char key)
{
    // Imprimir la tecla liberada
    std::cout << "Tecla liberada: " << key << std::endl;

    // lógica aquí para manejar la tecla liberada
}

// Función que escucha el input del teclado
void listenForKeyboardInput()
{
    char key;
    while (true)
    {
        if (_kbhit())
        {
            key = _getch();
            if (key == '\r')
            {
                // Salir del bucle si se presiona la tecla Enter
                break;
            }
            else if (key & 0x80)
            {
                // Manejar la liberación de tecla
                handleKeyRelease(key & 0x7F);
            }
            else
            {
                // Manejar la presión de tecla
                handleKeyPress(key);
            }
        }
    }
}

// Hacer un clear de la pantalla
void clearScreen()
{
    system("cls");
}

// Enseñar texto en la pantalla (consola)
void displayText(const std::string &text)
{
    std::cout << text << std::endl;
}

int main()
{
    std::cout << "Controlador de Teclado y Pantalla" << std::endl;

    // Comenzar a escuchar la entrada del teclado
    listenForKeyboardInput();

    // Limpiar la pantalla
    clearScreen();

    // Mostrar texto en la pantalla
    displayText("¡Hola, Mundo!");

    return 0;
}

#include <iostream>
#include <fstream>
#include <regex>

void handleNVMeSSD(const std::string &deviceName)
{
    // Lógica para manejar los SSD NVMe
    std::cout << "Manejando SSD NVMe: " << deviceName << std::endl;
    // Realizar operaciones como leer/escribir datos, gestionar espacios de nombres, etc.
}

void NVMeSSD()
{
    std::ifstream devices("/proc/devices");
    std::regex nvmeRegex("nvme[0-9]+");

    std::string line;
    while (std::getline(devices, line))
    {
        std::smatch match;
        if (std::regex_search(line, match, nvmeRegex))
        {
            std::string deviceName = match.str();
            std::cout << "Encontrado SSD NVMe: " << deviceName << std::endl;
            handleNVMeSSD(deviceName);
        }
    }
}

void runStorageDeviceSetup()
{
    // Identificar SSDs NVMe
    NVMeSSD();

    // Lógica para manejar SSDs SATA y HDDs

    // Lógica para manejar otros dispositivos de almacenamiento
}

int main()
{
    runStorageDeviceSetup();

    return 0;
}