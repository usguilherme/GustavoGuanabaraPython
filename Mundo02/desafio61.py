# Este programa calcula os 10 primeiros termos de uma PA (Progressão Aritmética)
# usando o primeiro termo e a razão fornecidos pelo usuário.

print('Gerador de PA')
print('-=' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro
cont = 1

while cont <= 10:
    print(f"{termo} -> ", end='')
    termo += razao
    cont += 1

print('FIM')