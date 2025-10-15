#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
#do comprador e em quantos anos ele vai pagar. A prestação mensal, não pode exceder 30% do salário ou então o empréstimo
#será negado

casa = float(input("Qual é o valor da casa em R$? "))
salario = float(input("Qual é o salário do comprador? "))
anos = int(input("Quantos anos voce vai pagar "))

mensal = casa / (anos * 12)
if mensal > salario * 0.30:
    print(f"Prestação negada, no valor de {mensal:.2f}")
else:
    print(f"Prestação aprovada, no valor de {mensal:.2f}")


