#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
ano = int(input("Digite o ano especifico, e diremos se ele é ou não BISSEXTO "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 : print(f"O ano {ano} é BISSEXTO")
else: print(f"O ano {ano} não é bissexto!")
