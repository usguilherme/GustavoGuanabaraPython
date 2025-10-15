# Solicita um número inteiro ao usuário.
num = int(input('Digite um número: '))
total_divisores = 0

for c in range(1, num + 1):
    if num % c == 0:
        print(f'{c}', end=' ')
        total_divisores += 1
    else:
        print(f'{c}', end=' ')

print(f'\nO número {num} foi divisível {total_divisores} vezes.')

if total_divisores == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')