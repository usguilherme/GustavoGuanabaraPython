# O laço de repetição vai de 1 a 50 (o número 51 é usado para incluir o 50 no intervalo).
for n in range(1, 51):
    if n % 2 == 0:
        print(n, end= ' ')
print('FIM')