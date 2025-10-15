# Este programa coleta o nome, a idade e o sexo de quatro pessoas.
# Ele calcula a média de idade do grupo, encontra o nome do homem mais velho e conta quantas mulheres têm menos de 20 anos.
# A lógica usa um laço de repetição para coletar os dados e, dentro dele, usa condicionais para fazer as verificações e atualizações necessárias.

soma_idades = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
total_mulheres_jovens = 0

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M ou F: ')).strip().upper()

    soma_idades += idade

    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        total_mulheres_jovens += 1

media_idade = soma_idades / 4

print('=' * 20)
print(f'A média de idade do grupo é de {media_idade:.1f} anos.')
print(f'O homem mais velho do grupo tem {maior_idade_homem} anos e se chama {nome_homem_mais_velho}.')
print(f'Ao todo são {total_mulheres_jovens} mulheres com menos de 20 anos.')