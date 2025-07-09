def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def main():
    print("Temperature Conversion Tool")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    choice = int(input("Select conversion (1-6): "))
    
    if choice == 1:
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
    elif choice == 2:
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
    elif choice == 3:
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {celsius_to_kelvin(c):.2f}K")
    elif choice == 4:
        k = float(input("Enter temperature in Kelvin: "))
        print(f"{k}K = {kelvin_to_celsius(k):.2f}°C")
    elif choice == 5:
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_to_kelvin(f):.2f}K")
    elif choice == 6:
        k = float(input("Enter temperature in Kelvin: "))
        print(f"{k}K = {kelvin_to_fahrenheit(k):.2f}°F")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()