# nome, nota1, nota2, vai ser uma lista que vai ficar dentro da lista cadastro, mostrar de forma tabular o print da lista, buscar as notas de cada aluno[elemento dentro da lista cadastro] pelo indice do aluno[0], e os indeces das notas (n1[1], n2[2])


cadastro = []

while True:
    nome = str(input("Nome: ")).capitalize()
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) /2
    cadastro.append([nome, n1, n2, media])
    print("Cadastro realizado com sucesso!")
    escolha = str(input("Deseja cadastrar outro aluno (S/N)? ")).upper()[0]
    if escolha == "N":
        break
print("-=" *30)
print(f"{'No.':<10}", end="")
print(f"{'NOME':>6}", end="")
print(f"{'MEDIA':>14}", end="" "\n")
print("-"*30)
for i in cadastro:
    print(f"{cadastro.index(i):<10} {i[0]:^5} {i[3]:>11}")
print("-"*30)

while True:
    aluno = int(input("Mostrar as notas de qual aluno? (999 interrompe): "))
    if aluno == 999:
        print("Ate mais!!!")
        break
    t = len(cadastro) - 1
    print("-"*30)
    if aluno <= t:
        print(f"As Notas de {cadastro[aluno][0]} sao: {cadastro[aluno][1]}, {cadastro[aluno][2]}")    
    else:
       print("Codigo de aluno nao existe!")

    print("-"*30)