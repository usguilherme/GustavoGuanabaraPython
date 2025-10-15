# Este programa lê um número inteiro 'n' e mostra os 'n' primeiros elementos da Sequência de Fibonacci.

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)

n = int(input('Quantos termos você quer ver? '))
termo_1 = 0
termo_2 = 1

print('~' * 30)
print(f'{termo_1} -> {termo_2}', end='')
cont = 3

while cont <= n:
    proximo_termo = termo_1 + termo_2
    print(f' -> {proximo_termo}', end='')
    termo_1 = termo_2
    termo_2 = proximo_termo
    cont += 1

print(' -> FIM')
