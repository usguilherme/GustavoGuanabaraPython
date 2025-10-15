#Faça um programa que leia três números e mostre qual é o maior e qual é o menor
n1 = int(input("Digite seu primeiro número: "))
n2 = int(input("Digite seu segundo número: "))
n3 = int(input("Digite seu terceiro número: "))
menor = n1
maior = n1

if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

print(f"O maior número é {maior}, já o menor é {menor}")



