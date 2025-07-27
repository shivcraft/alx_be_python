# temp_conversion_tool.py
# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    # 1. Prompt and validate numeric input
    temp_str = input("Enter the temperature to convert: ")
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # 2. Prompt for unit and validate
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    unit = unit.strip().upper()
    if unit not in ('C', 'F'):
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

    # 3. Perform conversion
    if unit == 'F':
        c = convert_to_celsius(temp)
        print(f"{temp}°F is {c}°C")
    else:  # unit == 'C'
        f = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {f}°F")

if __name__ == "__main__":
    main()
