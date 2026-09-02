# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.


time = []


while True:
    gols_partidas = []
    jogador = dict()


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
        jogador['total_gols'] = total_gols
    time.append(jogador)
    gols_partidas.clear()
    print(f"Cadastro do jogador {nome}, realizado com sucesso!")
    while True:
        escolha = str(input("Deseja cadastrar outro jogador (S/N)?")).upper()[0]
        if escolha in "SN":
            break
        print("ERRO! Por favor escolha S ou N")
    if escolha == "N":
        break
print("-="*30)
print(f"{"cod":<10}", end="")
print(f"{"Nome":>5}", end="")
print(f"{"Gols":>10}", end="")
print(f"{"Total de gols feitos":>25}")
print("-"*30)
for pos, i in enumerate(time):
    print(f"{pos+1:<10} {i['nome']:^5} {str(i['gols']):>10}", end="")
    print(f"{i['total_gols']:>10}")
print("-"*30)

while True:
            qts_levantamento = int(input("Mostrar o levantamento de qual jogador? (999 para sair) "))
            if qts_levantamento == 999:
                print("Ate mais!")
                print("-"*30)
                break 
            indice = qts_levantamento - 1
            if 0<= indice < len(time):
                    print(f" -- LEVANTAMENTO DO JOGADOR {time[indice]['nome']}:")
                    for pos, i in enumerate(time[indice]['gols']):
                        print(f"   No jogo {pos + 1} fez {i} gols")
                    print("-"*30)
            else:
                print(f"ERRO! Nao existe jogador com o codigo {qts_levantamento}")
                print("-"*30)





