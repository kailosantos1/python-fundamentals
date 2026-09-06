def ficha(nome='desconhecido', gols=0):

    return(print(f"O jogador {nome} fez {gols} gol(s) no campeonato!"))


nome = input("Digite o nome do jogador: ").capitalize()
gols_texto = str(input(f"Digite a quantidade de gols feitos pelo {nome}: "))
if ficha():
    ficha(nome,gols=int(gols_texto))
elif ficha(nome) == ficha(nome):
    ficha(nome)
elif ficha() == ficha(gols=gols_texto):
    ficha()(gols=int(gols_texto))
elif ficha() == ficha(nome, gols_texto):
    ficha(nome, gols=int(gols_texto))


