def main():
    if True:
        dni = str(input("Introduce tu DNI completo: "))
        if len(dni) > 9:
            print("El DNI no debe tener más de 9 caracteres")
        elif len(dni) < 9:
            print("Por favor, introduce tu DNI completo, incluyendo la letra")
        else:
            dni_numero = dni[:-1]
            dni_letra = dni[-1].upper()

            def calcular_letra_dni(numero_dni):
                letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
                indice_letra = int(numero_dni) % 23
                return letras_dni[indice_letra]

            letra_calculada = calcular_letra_dni(dni_numero)

            if dni_letra == letra_calculada:
                print("La letra del DNI es correcta.")
            else:
                print("La letra del DNI es incorrecta.")


main()
