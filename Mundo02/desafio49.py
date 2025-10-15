# Pede ao usuário para digitar o número da tabuada.
num = int(input('Digite um número para ver sua tabuada: '))

print('-' * 10)
for c in range(1, 11):
    print(f'{num} x {c:2} = {num * c}')

print('-' * 10)