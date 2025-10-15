numero = int(input("Digite seu número, que iremos calcular o seu fatorial "))
print("Calculando o fatorial.....")
soma = 1
if numero >= 0:
    for i in range(numero, 0, -1):
        soma *= i
        if i > 1:
            print(i, end=" x ")
        else:
            print(i, end=" = ")

    print(soma)
else:
    print("Não é possível calcular fatorial de números negativos")