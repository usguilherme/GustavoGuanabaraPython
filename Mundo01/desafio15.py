# Programa que calcula o preço a pagar por um carro alugado, considerando 60 R$/dia e 0,15 R$/km
km = float(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias alugados: "))
preco = (dias * 60) + (km * 0.15)
print(f"O preço a pagar é: R$ {preco:.2f}")
