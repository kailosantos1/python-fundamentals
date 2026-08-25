import random
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")
lista = [aluno1, aluno2, aluno3, aluno4]
ordemdeescolha = random.sample(lista, k=4)

print(f"A ordem de apresentacao sera: {ordemdeescolha}.")


