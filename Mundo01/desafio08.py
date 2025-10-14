#Escreva um programa que leia um valor em metros e o exiba convertido em centrimetros e milimetros.
metros = int(input("Digite o valor em Metros "))
print(f"O valor {metros}m, em centrimetros é {metros * 100:.0f}cm, e em milimetros é {metros * 1000:.0f}mm")