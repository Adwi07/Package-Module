def temp_converter(operation, temperature):

    def convert_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def convert_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    operations = {
        "celsius": convert_to_celsius,
        "fahrenheit": convert_to_fahrenheit
    }

    if operation not in operations:
        raise ValueError("Unsupported temperature conversion")

    return operations[operation](temperature)

