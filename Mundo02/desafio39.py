#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar
#ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento, seu programa tmabém deverá mostrar
#o tempo que falta ou que passou do prazo.

from datetime import date
anoN = int(input("Digite seu ano de nascimento: "))
anoA = date.today().year
idade = anoA - anoN
if idade > 18:
    print(f"Voce passou do tempo de se alistar, já se fazem {idade - 18} anos")
elif idade == 18:
    print(f"Voce deve se alistar, está na hora e na idade certa")
else:
    print(f"Voce ainda irá se alistar, falta {18 - idade} anos!")
