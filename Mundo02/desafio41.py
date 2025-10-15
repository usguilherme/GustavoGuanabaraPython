from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Ano de Nascimento: '))
idade = ano_atual - ano_nascimento

if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print(f'O atleta tem {idade} anos.')
print(f'Sua categoria é: {categoria}')