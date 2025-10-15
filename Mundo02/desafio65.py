# Este programa lê vários números, calcula a média, encontra o maior e o menor
# valor e pergunta ao usuário se ele quer continuar.

soma = 0
cont = 0
maior = 0
menor = 0
resposta = 'S'

while resposta in 'Ss':
    num = int(input('Digite um número inteiro: '))
    soma += num
    cont += 1

    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()

media = soma / cont

print(f'Você digitou {cont} números e a média foi {media:.2f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')