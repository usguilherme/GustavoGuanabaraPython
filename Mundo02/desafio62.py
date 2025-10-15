# Este programa calcula os termos de uma PA (Progressão Aritmética) e pergunta
# ao usuário se ele quer ver mais termos, encerrando apenas quando ele digitar 0.

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro
cont_termos = 1
total_termos = 0
mais_termos = 10

while mais_termos != 0:
    total_termos += mais_termos
    while cont_termos <= total_termos:
        print(f'{termo} -> ', end='')
        termo += razao
        cont_termos += 1
    print('PAUSA')

    mais_termos = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {total_termos} termos mostrados.')