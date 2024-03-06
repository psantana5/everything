numeros = []

while True:
    eleccion = input("Entra un numero o 'basta' si quieres parar: ")
    if eleccion.lower() == "basta":
        break
    else:
        try:
            number = int(eleccion)
            numeros.append(number)
        except ValueError:
            print("Entra un número válido o 'basta'.")

print("Lista de numeros entrados:", numeros)

unicos = list(set(numeros))

print("Lista de numeros únicos:", unicos)
