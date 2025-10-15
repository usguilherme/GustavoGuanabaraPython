# Este programa analisa dados de várias pessoas (idade e sexo)
# e mostra um resumo no final, perguntando ao usuario se quer continuar.

total_maior_18 = 0
total_homens = 0
total_mulheres_jovens = 0

print('-' * 20)
print('CADASTRO DE PESSOAS')
print('-' * 20)

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0] #to pegando só a primeira letra
    if idade >= 18:
        total_maior_18 += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        total_mulheres_jovens += 1

    print('-' * 20)

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print('=' * 6, ' FIM DO PROGRAMA ', '=' * 6)
print(f'Total de pessoas com mais de 18 anos: {total_maior_18}')
print(f'Ao todo temos {total_homens} homens cadastrados.')
print(f'E temos {total_mulheres_jovens} mulheres com menos de 20 anos.')