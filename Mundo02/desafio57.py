#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F" caso esteja errado, peça
#a digitação novamente até ter um valor correto

sexo = ''
while sexo not in ['M', 'F']:
    sexo = input('Digite o sexo (M/F): ').strip().upper()
    if sexo not in ['M', 'F']:
        print('Valor inválido! Por favor, digite M ou F.')
print(f'Sexo digitado: {sexo}')