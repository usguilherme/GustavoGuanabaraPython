# Programa que lê largura e altura de uma parede, calcula sua área e a quantidade de tinta necessária (1 litro pinta 2m²)
largura = float(input("Digite a largura da parede (m): "))
altura = float(input("Digite a altura da parede (m): "))
area = largura * altura
tinta = area / 2
print(f"Área da parede: {area} m²")
print(f"Tinta necessária: {tinta:.2f} litros")
