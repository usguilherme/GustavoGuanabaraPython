# Este programa exibe a tabuada de vários números, um por vez.
# Ele para de funcionar quando o número digitado é negativo.

while True:
    print('-' * 30)
    num = int(input('Quer ver a tabuada de qual valor? '))

    if num < 0:
        break

    print('-' * 30)

    for i in range(1, 11):
        print(f'{num} x {i:2} = {num * i}')

print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')