# Pede ao usuário o primeiro termo e a razão da PA.
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro

print('-=' * 10)
for c in range(10):
    print(f'{termo}', end=' -> ')
    termo += razao

print('FIM')