# Este programa lê dois valores e apresenta um menu de opções para o usuário,
# permitindo que ele realize operações como somar, multiplicar, encontrar o maior
# número, inserir novos valores ou sair do programa.

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
''')
    opcao = int(input('>>>>> Qual é a sua opção? '))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}.')
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {multiplicacao}.')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior valor entre {n1} e {n2} é {maior}.')
    elif opcao == 4:
        print('Informe os novos valores:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')

    sleep(2)

print('Fim do programa! Volte sempre!')