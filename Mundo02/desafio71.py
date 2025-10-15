# Este programa simula um caixa eletrônico, informando a quantidade de cédulas
# de R$50, R$20, R$10 e R$1 para um valor de saque.

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))

total = valor
cedula = 50
total_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        total_cedulas = 0

        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO CEV!')