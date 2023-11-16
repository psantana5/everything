import os


def abrir():
    try:
        archivo = str(
            input("¿Cual es la ruta del archivo que quieres abrir? "))
        with open(archivo, 'r') as file:
            contenido = file.read()
            print(contenido)
    except ValueError:
        print("Oops, ha habido un error. ")


def escribir():
    try:
        escribir = str(input("¿Qué nuevo archivo quieres escribir?"))
        contenido = str(input("¿Qué contenido quieres escribir? "))
        with open(escribir, 'w') as file:
            file.write(contenido + "\n")
            print(escribir)
    except FileNotFoundError:
        print("Vaya, no he podido encontrar el archivo")


def añadir():
    try:
        anadir = str(input("¿Qué archivo quieres añadir contenido?"))
        contenido = str(input("¿Qué contenido quieres añadir?"))
        with open(anadir, 'a') as file:
            file.write(contenido)
            print(anadir)
    except ValueError:
        print("Ha habido un error, lo siento.")


def menu():
    print("Menu de opciones\n"
          "\n"
          "1. Abrir un archivo\n"
          "2. Escribir un archivo nuevo\n"
          "3. Añadir contenido a un archivo\n"
          "4. Salir\n"
          )
    eleccion = int(input("Escoge una opción: "))
    if eleccion == 1:
        abrir()
    elif eleccion == 2:
        escribir()
    elif eleccion == 3:
        añadir()
    elif eleccion == 4:
        exit
    else:
        try:
            print("Opción no reconocida")
            menu()
        except ValueError:
            print("Valor no aceptado, introduce sólo un número")
            menu()


menu()
