#Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem:
#O primeiro valor é maior, o segundo valor é maior, Não existe valor maior, os dois são iguais
n1 = int(input("Digite seu número: "))
n2 = int(input("Digite seu número: "))
if n1 > n2:
    print(f"O primeiro número {n1} é maior que o segundo número {n2}")
elif n2 > n1:
    print(f"O segundo número {n2} é maior que o primeiro número {n1}")
else:
    print("Não existe valor maior, os dois sõa iguais")
