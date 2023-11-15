def main():
    al_sand = ["Cereales que contienen gluten", "Crústaceos", "Huevos", "Pescado", "Soja", "Leche y derivados",
               "Frutos de cáscara", "Apio", "Mostaza", "Granos de sésamo", "Anhidrido sulfuroso y sulfitos", "Moluscos", "Altramuces"]
    categoria = str(input("¿Qué categoría quieres ver?: "))

    if categoria == "sandwiches".lower():
        print(al_sand)


main()
