print("What is the temperature in fahrenheit?")
value = input()

if value.isnumeric() == False:
    print("Not a value number")

farenheit = int(value)

celcius = (farenheit - 32) * 5/9
print(celcius)