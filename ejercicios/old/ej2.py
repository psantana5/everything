def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def imprimir_primos_menores_o_iguales_a_n(n):
    for i in range(2, n + 1):
        if es_primo(i):
            print(i, end="")


def main():
    pedir = int(input("Entra un número: "))
    print("Los números primos menores o iguales a", pedir, "son:")
    imprimir_primos_menores_o_iguales_a_n(pedir)


if __name__ == "__main__":
    main()
