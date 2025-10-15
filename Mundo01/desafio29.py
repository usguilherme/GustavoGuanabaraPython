#Crie um programa que leia a velocidade de um carro, se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi
#multado, A multa vai custar sete reais por cada Km acima do limite
velocidade = float(input("Qual é a velocidade atual do carro: "))
if velocidade > 80:
    preco = (velocidade - 80) * 7
    print(f"Voce irá pagar uma multa no valor de {preco:.0f} R$")
    print("Tenha um bom dia, Cuidado no transito!")
else:
    print("Tenha um bom dia, Cuidado no transito!")
