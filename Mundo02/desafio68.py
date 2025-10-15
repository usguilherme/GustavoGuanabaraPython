# Este programa joga par ou ímpar com o usuario e só para quando ele perde.
# No final, mostra o total de vitórias consecutivas.

from random import randint

vitorias = 0
print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)

while True:
    jogador = int(input('Diga um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    computador = randint(0, 10)

    total = jogador + computador
    resultado = ' '
    if total % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'

    print('-' * 30)
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total é {total}, que é {resultado}.')
    print('-' * 30)

    if escolha == 'P':
        if resultado == 'PAR':
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if resultado == 'ÍMPAR':
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break

print(f'GAME OVER! Você venceu {vitorias} vezes consecutivas.')