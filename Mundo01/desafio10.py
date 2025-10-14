# Programa que lê quanto dinheiro uma pessoa tem na carteira e mostra quantos dólares ela pode comprar
real = float(input("Digite quanto você tem na carteira (R$): "))
dolar = real / 3.27
print(f"Você pode comprar ${dolar:.2f} dólares")
