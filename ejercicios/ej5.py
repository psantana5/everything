alergenos_sand = {
    "Hamburguesa": ["Gluten", "Leche y derivadas", "Mostaza", "Granos de sésamo"],
    "McPollo": ["Gluten", "Leche y derivadas", "Huevo", "Mostaza"],
    "Cuarto de libra con queso": ["Gluten", "Leche y derivadas", "Mostaza", "Sulfitos"],
    "McRib": ["Gluten", "Mostaza", "Apio", "Sulfitos"],
    "Big Mac": ["Gluten", "Leche y derivadas", "Mostaza", "Sulfitos"],
    "McFish": ["Gluten", "Pescado", "Leche y derivadas", "Mostaza", "Sulfitos"],
    "McVeggie": ["Gluten", "Leche y derivadas", "Mostaza", "Sulfitos"]
}

# Ask the user for input
user_choice = input(
    "¿De qué sandwich quieres comprobar los alérgenos? ")

if user_choice in alergenos_sand:
    print(f"Los alérgenos para {user_choice} son: {
          ', '.join(alergenos_sand[user_choice])}.")
else:
    print("Sandwich no disponible")
