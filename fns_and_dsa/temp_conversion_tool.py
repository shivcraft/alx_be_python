# temp_conversion_tool.py

# 1. Define global conversion factors exactly once at the module level
#CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
#FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

def convert_to_celsius(fahrenheit):
    # 2. Reference the global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    # 3. Reference the global CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    temp_str = input("Enter the temperature to convert: ")
    try:
        temp = float(temp_str)
    except ValueError:
        # Must raise exactly this message
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit not in ('C', 'F'):
        # Likewise raise for bad unit
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

    if unit == 'F':
        result = convert_to_celsius(temp)
        print(f"{temp}°F is {result}°C")
    else:
        result = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {result}°F")

if __name__ == "__main__":
    main()
