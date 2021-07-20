# Задание №2 - сделано
u_input = float(input('Enter a numer: '))
temperature_type = input('Choose C, F or K: ')


def task_7_2(u_input, temperature_type):
    if temperature_type == 'C':
        celsius = u_input
        kelvin = u_input + 273.15
        fahrenheit = u_input * 1.8 + 32
        return celsius, kelvin, fahrenheit
    elif temperature_type == 'F':
        celsius = (u_input - 32) / 1.8
        kelvin = (u_input + 459.67) * 5 / 9
        fahrenheit = u_input
        return celsius, kelvin, fahrenheit
    elif temperature_type == 'K':
        celsius = u_input - 273.15
        kelvin = u_input
        fahrenheit = u_input * 1.8 - 459.67
        return celsius, kelvin, fahrenheit
    else:
        return False


print(task_7_2(u_input, temperature_type))
