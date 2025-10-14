#Um professor quer sortear um dos seus quatros alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random
n1 = input("Nome do primeiro aluno: ")
n2 = input("Nome do segundo aluno: ")
n3 = input("Nome do terceiro aluno: ")
n4 = input("Nome do quatro aluno:: ")
array = [n1,n2,n3,n4]
escolhido = random.choice(array)
print(f"O aluno escolhido foi {escolhido}")


