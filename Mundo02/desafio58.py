#O computador vai pensar em um número entre 0 e 10, o jogador vai tentar advinhar até acertar. mostrando no final
#quantos palpites foram necessários para vencer

from random import randint
computador = randint(0,10)
acertou = False
cont = 0
while not acertou:
    cont += 1
    resposta = int(input("Digite seu número entre 0 e 10 "))
    if resposta == computador:
        acertou = True

print(f"Foi necessário {cont} repetiçoes para encontrar a resposta igual!")
