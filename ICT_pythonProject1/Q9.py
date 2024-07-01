# Write a Python program to convert temperatures to and from Celsius
# Fahrenheit. [Formula: c/5=f-32/9 where c=temperature in Celsius and f=
# temperature in Fahrenheit.] Sample input: Temperature in Fahrenheit
# =41 Sample output: Temperature in Celsius =5

farenheit = float(input('enter the temperature: '))
celsius = (farenheit-32)*(5/9)
print('Temperature in celsius =',celsius)