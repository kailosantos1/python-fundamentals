import random

jogador1 = int(input("Voce sera o JOGADOR 1, Qual voce escolhe? 1 - tesoura, 2 - pedra, 3 - papel "))
jogador2 = random.randint(1,3)

if jogador1 == jogador2:
    print("Empate!")

elif (jogador1 ==  1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (jogador1 == 3 and jogador2 == 2):
    print("Parabéns, o JOGADOR 1 ganhou! 🏆")
else:
    print("O JOGADOR 2 (Computador) ganhou! 🤖")