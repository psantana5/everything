def coeficiente_binomial(n, k):
    """
    Calcula el coeficiente binomial de n y k de forma recursiva.

    Parámetros:
      n (int): El número de elementos del conjunto.
      k (int): El número de elementos de cada subconjunto.

    Retorno:
      int: El coeficiente binomial de n y k.
    """
    if k == 0 or k == n:
        return 1
    else:
        return coeficiente_binomial(n - 1, k - 1) + coeficiente_binomial(n - 1, k)


n = int(input("Introduzca el número de elementos del conjunto: "))
k = int(input("Introduzca el número de elementos de cada subconjunto: "))

coeficiente = coeficiente_binomial(n, k)

print(f"El coeficiente binomial de {n} y {k} es: {coeficiente}")
