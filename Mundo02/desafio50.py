# Este programa lê seis números inteiros, um de cada vez, e calcula a soma apenas dos que forem pares.
# Ele usa um laço de repetição para solicitar os valores e, para cada número digitado, verifica se é par.
# Se for, adiciona o valor a um total acumulado.
# Ao final, o programa exibe a quantidade de números pares digitados e a soma total deles.

soma = 0
contador = 0

for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        soma += num
        contador += 1

print(f'Você informou {contador} números pares e a soma foi {soma}.')