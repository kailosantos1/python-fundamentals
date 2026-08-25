from datetime import date

ano = int(input("Que ano voce nasceu? "))

idade = date.today().year - ano

if idade < 18:
    print("Voce ainda vai se alistar")
    falta = 18 - idade
    print(f"Falta {falta} anos para vc se alistar")
elif idade == 18:
    print("Esta na hora de se alistar")
else:
    passou = idade- 18
    print("Ja passou da hora de se alistar!")
    print(f"Passou {passou} anos da hora de se alistar")

