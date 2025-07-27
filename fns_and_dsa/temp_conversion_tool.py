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
    temp_str = input("Enter the temperature to convert: ")
    try:
        temp = float(temp_str)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        c = convert_to_celsius(temp)
        print(f"{temp}°F is {c}°C")
    elif unit == 'C':
        f = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {f}°F")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
