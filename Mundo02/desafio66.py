# Este programa lê vários números, soma-os e conta quantos foram digitados,
# parando apenas quando o usuario digita 999.

soma = 0
cont = 0
num = 0

print('Digite vários números inteiros. O programa irá parar quando você digitar 999.')

while num != 999:
    num = int(input('Digite um número (999 para parar): '))

    if num != 999:
        soma += num
        cont += 1

print('~' * 30)
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')