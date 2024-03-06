def main():
    favoritos = ["python", "c", "perl", "bash", "c++"]
    eleccion = int(input("¿Qué posición de la lista quieres imprimir? "))
    try:
        print(favoritos[eleccion])
    except IndexError:
        if eleccion < 0:
            print("Introduce un número mayor a 0")
        elif eleccion > len(favoritos):
            print("Introduce una posición que esté dentro de la lista")
        main()


while __name__ == "__main__":
    main()
