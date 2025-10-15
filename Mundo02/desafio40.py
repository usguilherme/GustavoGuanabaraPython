#Receba tres notas do aluno, faça a media aritmética, e verifique: >= 7 Aprovado, 5.0 <= nota <= 6.9 RECUPERACAO
#se não, Reprovado

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Média {media:.1f} - Aprovado")
elif 5.0 <= media <= 6.9:
    print(f"Média {media:.1f} - Recuperação")
else:
    print(f"Média {media:.1f} - Reprovado")