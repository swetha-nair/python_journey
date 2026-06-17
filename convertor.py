print("UNIT CONVERTER")
print("1. Temperature")
print("2. Length")
print("3. Weight")
print("4. Speed")

user_choice = int(input("Enter your choice (1-4): "))

if user_choice == 1:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    option = int(input("Choose conversion: "))
    input_value = float(input("Enter temperature: "))

    if option == 1:
        result = (input_value * 9/5) + 32
        print(f"{input_value}C = {result:.2f}F")

    elif option == 2:
        result = (input_value - 32) * 5/9
        print(f"{input_value}F = {result:.2f}C")

    else:
        print("Please choose a valid option!")

elif user_choice == 2:
    print("\nLength Converter")
    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")

    option = int(input("Choose conversion: "))
    input_value = float(input("Enter length: "))

    if option == 1:
        result = input_value / 1000
        print(f"{input_value} m = {result} km")

    elif option == 2:
        result = input_value * 1000
        print(f"{input_value} km = {result} m")

    else:
        print("Please choose a valid option!")

elif user_choice == 3:
    print("\nWeight Converter")
    print("1. Kilogram to Pound")
    print("2. Pound to Kilogram")

    option = int(input("Choose conversion: "))
    input_value = float(input("Enter weight: "))

    if option == 1:
        result = input_value * 2.20462
        print(f"{input_value} kg = {result:.2f} lb")

    elif option == 2:
        result = input_value / 2.20462
        print(f"{input_value} lb = {result:.2f} kg")

    else:
        print("Please choose a valid option!")

elif user_choice == 4:
    print("\nSpeed Converter")
    print("1. km/h to m/s")
    print("2. m/s to km/h")

    option = int(input("Choose conversion: "))
    input_value = float(input("Enter speed: "))

    if option == 1:
        result = input_value / 3.6
        print(f"{input_value} km/h = {result:.2f} m/s")

    elif option == 2:
        result = input_value * 3.6
        print(f"{input_value} m/s = {result:.2f} km/h")

    else:
        print("Please choose a valid option!")

else:
    print("Invalid choice.")
