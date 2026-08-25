import random

c = 0

while True:
    
    num1 = random.randint(0,10)
    num2 = int(input("Digite um valor: "))

    escolha = str(input("Escolha PAR ou IMPAR (P/I): ")).upper()[0]

    if escolha == "P":
        soma = (num1 + num2)
        if soma %2 == 0:
            print(f"Parabens, voce venceu!, vamos jogar novamente")
            c += 1
        else:
            print(f"Voce perdeu! Voce venceu: {c} vez")
            break
    if escolha == "I":
        soma = (num1 + num2)
        if soma %2 != 0:
            print(f"Parabens, voce venceu!, vamos jogar novamente")
            c += 1
        else:
            print(f"Voce perdeu! Voce venceu: {c} vez")
            break
