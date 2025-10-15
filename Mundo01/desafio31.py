#Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0.50 para
#viagens de até 200km e R$0.45 para viagens mais longas
km = float(input("Digite a distância em km da sua viagem: "))
if km > 200: preco = km * 0.45
else: preco = km * 0.50
print(f"O preço da viagem de {km:.0f} é de: {preco:.2f} R$")
