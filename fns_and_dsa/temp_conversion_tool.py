FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
   
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
   
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User Interaction Function
def convert_temperature():
    try:
        # Prompt user for temperature
        temperature = float(input("Enter the temperature to convert: "))
        
        # Ask user if the temperature is in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit not in ['C', 'F']:
            print("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
        if unit == 'F':
            # Convert from Fahrenheit to Celsius
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        elif unit == 'C':
            # Convert from Celsius to Fahrenheit
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")

    except ValueError :
       print("Invalid temperature. Please enter a numeric value.")
# Run the conversion function
if __name__ == "__main__":
    convert_temperature()