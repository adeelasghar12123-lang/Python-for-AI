def temp_converter():
    while True:
        choice = int(input("1.Celsius to Farenheit.... | 2. Fahrenheit to Celsius...."))
        if choice < 1 or choice > 2:
            print("Enter a valid Choice !")
            continue
        else:
            break
    if choice == 1:
        celsius = float(input("Enter temperature in celsius : "))
        fahrenheit = (celsius * 9/5) + 32
        print(f'{celsius} C in Fahrenheit is {fahrenheit:.2f} F !')
    else:
        fahrenheit = float(input("Enter temperature in Fahrenheit : "))
        celsius = celsius = (fahrenheit - 32) * 5/9
        print(f'{fahrenheit} F in Celsius is {celsius:.2f} C !')

temp_converter()


