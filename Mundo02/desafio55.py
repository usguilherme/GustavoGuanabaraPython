# Este programa lê o peso de cinco pessoas, armazena o maior e o menor valor e exibe o resultado final.
# Ele usa um laço de repetição para solicitar o peso de cada pessoa, e uma lógica condicional para comparar e atualizar o maior e o menor peso conforme os valores são lidos.

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))

    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi de {maior}Kg.')
print(f'O menor peso lido foi de {menor}Kg.')