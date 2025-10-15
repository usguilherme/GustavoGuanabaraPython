# O laço itera de 1 a 500, pulando de 2 em 2 para pegar apenas os números ímpares.
soma = 0
contador = 0

for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
        contador += 1
print(f'A soma dos {contador} números ímpares múltiplos de 3 é {soma}.')