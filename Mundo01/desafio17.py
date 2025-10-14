# Programa que lê os catetos de um triângulo retângulo e calcula a hipotenusa
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adj = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = (cateto_oposto**2 + cateto_adj**2)**(1/2)
print(f"O comprimento da hipotenusa é {hipotenusa:.2f}")
