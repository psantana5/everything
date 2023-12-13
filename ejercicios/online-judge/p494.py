while True:
    uno = input("Introduce la primera frase: ")
    dos = input("Introduce la segunda frase: ")

    palabras1 = uno.split()
    palabras2 = dos.split()
    cuenta = 0
    cuenta1 = 0

    for i in uno:
        if i == uno:
            cuenta = + 1
            print(cuenta)
    print(len(palabras1))

    for i in dos:
        if i == dos:
            cuenta1 += 1
            print(cuenta1)
    print(len(palabras2))
