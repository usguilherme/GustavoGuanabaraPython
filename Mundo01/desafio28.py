#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador, O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
selecao = randint(0,5)
print("Irei selecionar um número entre 0 a 5, diga qual eu irei escolher, e vejo se voce acertou! ")
num = int(input("Diga o seu número: "))
if num == selecao:
    print("Você acertou!")
else:
    print("Errou!")
