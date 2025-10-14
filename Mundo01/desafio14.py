# Programa que lê uma temperatura em Celsius e converte para Fahrenheit
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F")
