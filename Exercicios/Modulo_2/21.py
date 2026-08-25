import random

numero = random.randint(0,10)
ganhou = False


while ganhou == False:
    numero_escolhido = int(input("Adivinhe um numero: "))
    if numero_escolhido == numero:
        print(f"Voce ganhou!!! O numero sorteado era: {numero}")
        ganhou = True
    else:
        print(f"Voce errou! Tente novamente.")




