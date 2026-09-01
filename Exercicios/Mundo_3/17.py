# pergunta quantos jogos vao ser gerados, a quantidade de jogos gerados sera a quantidade de listas dentro da lista sorteador, dentro da lista sorteador vai ter o metodo random.sample que vai gerar os numeros aleatorios para cada jogo (cada lista dentro de lista), depois exibir as listas com o print(sorteador), entao, cadastra a quantidade de jogos, guarda dentro de lista e exibe
import time
import random
contador = 0
sorteador = []
jogos = int(input("Quantos jogos? "))

for i in range(0,jogos):
    sorteador.append(random.sample(range(1,61),6))

print(f"A quantidade de jogos gerados foi: {jogos}")
print("Gerando por favor aguarde...")
time.sleep(1)
for lista in sorteador:
    contador += 1
    time.sleep(0.5)
    print(f"Jogo {contador}: {sorted(lista)}")