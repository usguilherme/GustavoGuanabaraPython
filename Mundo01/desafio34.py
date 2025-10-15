#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento, para salários superiores
#a R$1.250.00. calcule um aumento de 10%. para salários inferiores ou iguais, o aumenta é de 15%
salario = int(input("Digite o seu salário"))
if salario > 1250:
    novoSalario = salario + (salario * 0.10)
else:
    novoSalario = salario + (salario * 0.15)

print(f"O seu salário foi de {salario:.2f} R$, para {novoSalario:.2f} R$")
