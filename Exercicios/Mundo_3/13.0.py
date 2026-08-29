pessoas = []
dados = []
pessoas_leves = []
pessoas_pesadas = []
contador = 0
while True:
    nome = str(input("Digite o nome: "))
    peso = float(input("Digite o peso: "))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    print("Pessoa cadastrada!")
    contador += 1
    if peso >= 100:
        pessoas_pesadas.append(nome)
    elif peso <= 70:
        pessoas_leves.append(nome)
    dados = []
    escolha = str(input("Deseja cadastrar mais pessoas (S/N)? ")).upper()[0]
    if escolha == 'N':
        break
print(f"As pessoas e seus pesos cadastrados foram: {pessoas}")
print(f"Quantidade de pessoas cadastradas: {contador}")
print(f"Pessoas com o peso maior ou igual a 100kg: {pessoas_pesadas}")
print(f"Pessoas com o peso abaixo ou igual a 70kg: {pessoas_leves}")

