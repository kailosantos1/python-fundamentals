# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
gols_partidas = []

nome = str(input("Digite o nome do jogador: ")).capitalize()
partidas = int(input(f"Quantas partidas {nome} jogou? "))
jogador['nome'] = nome
jogador['partidas'] = partidas
total_gols = 0
for i in range(1,partidas+1):
    gols = int(input(f"Quantos gol o {nome} fez no jogo {i}? "))
    gols_partidas.append(gols)
    jogador['gols'] = gols_partidas[:]
    total_gols += gols
gols_partidas.clear()  
jogador['total_gols'] = total_gols

aproveitamento = jogador["gols"]
print("-="*30)
print(jogador)
print("-="*30)
for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("-="*30)
print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas")
for pos, i in enumerate(aproveitamento):
    print(f"  => Na partida {pos+1}, fez {i} gols")
print("-="*30)
print(f"Foi um total de {jogador['total_gols']} gols")


