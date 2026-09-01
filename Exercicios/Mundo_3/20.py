# randint para gerar um numero aleatorio entre 1 e 6 para 4 jogadores
# montar um dicionario com 4 jogares e 4 jogadas
# mostrar o jogador e seus resultados mas deixando em ordem os resultados, para saber a posicao de cada um, sendo que o maior numero tirado e o vencedor

from random import randint
import time
jogadores= []
cadastro = dict()

for j in range(1,5):
    jogador = (f"Jogador_{j}")
    numero = randint(1,6)
    jogadores.append([jogador, numero])
    cadastro[jogador] = numero
    jogadores.clear()
ranking = sorted(cadastro.items(), key= lambda item: item[1], reverse=True)
for pos, (nome, numero) in enumerate(ranking):
    time.sleep(0.5)
    print(f"O jogador {nome} ficou em {pos+1} lugar, tirando: {numero} no dado")
