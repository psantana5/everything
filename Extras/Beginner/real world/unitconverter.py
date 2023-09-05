unit_conversions = {
    "intocm": {"name": "Inches to Centimeters", "conversion_factor": 2.54},
    "fttom": {"name": "Feet to Meters", "conversion_factor": 0.3048},
    "lbstokg": {"name": "Pounds to Kilograms", "conversion_factor": 0.453592},
    "ftoc": {"name": "Fahrenheit to Celsius", "conversion_factor": 5 / 9, "subtract_first": 32},
    "galtol": {"name": "Gallons to Liters", "conversion_factor": 3.78541}
}

print("Available conversions:")
for key, conversion in unit_conversions.items():
    print(f"{key}: {conversion['name']}")

# User input for the type of conversion they want to perform
conversion_key = input("Which conversion would you like to perform? (Use short name like 'intocm', 'fttom', etc.) ")

# User input for the value they want to convert
value_to_convert = float(input("Enter the value you want to convert: "))

# Initialize converted_value to None to signify that we haven't found a matching conversion yet
converted_value = None

# Find and perform the conversion
if conversion_key in unit_conversions:
    conversion = unit_conversions[conversion_key]
    if 'subtract_first' in conversion:  # Special case for Fahrenheit to Celsius
        converted_value = (value_to_convert - conversion['subtract_first']) * conversion['conversion_factor']
    else:
        converted_value = value_to_convert * conversion['conversion_factor']

# Check if a valid conversion was found and performed
if converted_value is not None:
    print(f"The converted value is: {converted_value}")
else:
    print("Sorry, that conversion is not available.")
