import random
num = random.randint(0,5)

tentativa = int(input("tente adivinhar o numero: "))


if num == (tentativa):
    print("Parabens, voce acertou")
else:
    print(f"Voce errou, o numero era {num}")