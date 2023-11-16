conversiones = {
    'longitudes': {
        'kilómetros': {'millas': 0.621371, 'metros': 1000, 'yardas': 1094},
        'millas': {'kilómetros': 1.60934, 'metros': 1609.34, 'yardas': 1760},
        'metros': {'kilómetros': 0.001, 'millas': 0.000621371, 'yardas': 1.09361},
        'yardas': {'kilómetros': 0.0009144, 'millas': 0.000568182, 'metros': 0.9144}
    },
    'volúmenes': {
        'litros': {'galones': 0.264172, 'mililitros': 1000, 'centímetros cúbicos': 1000},
        'galones': {'litros': 3.78541, 'mililitros': 3785.41, 'centímetros cúbicos': 3785.41},
        'mililitros': {'litros': 0.001, 'galones': 0.000264172, 'centímetros cúbicos': 1},
        'centímetros cúbicos': {'litros': 0.001, 'galones': 0.000264172, 'mililitros': 1}
    },
    'masas': {
        'kilogramos': {'libras': 2.20462, 'gramos': 1000},
        'libras': {'kilogramos': 0.453592, 'gramos': 453.592},
        'gramos': {'kilogramos': 0.001, 'libras': 0.00220462}
    }
}

tipo_unidad = input(
    "Entra el tipo de unidad (longitudes, volúmenes, masas): ").lower()
unidad_origen = input(f"Entra la unidad de origen ({
                      ', '.join(conversiones[tipo_unidad].keys())}): ").lower()
unidad_destino = input(f"Entra la unidad de destino ({', '.join(
    conversiones[tipo_unidad][unidad_origen].keys())}): ").lower()

if tipo_unidad in conversiones and unidad_origen in conversiones[tipo_unidad] and unidad_destino in conversiones[tipo_unidad][unidad_origen]:
    factor_conversion = conversiones[tipo_unidad][unidad_origen][unidad_destino]
    print(f"El factor de conversión de {unidad_origen} a {
          unidad_destino} es: {factor_conversion}")
else:
    print("Las unidades entradas no son válidas.")
