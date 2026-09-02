#  Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

soma_idade = 0
lista_pessoas = []
while True:
    nome = str(input("Digite o nome: ")).capitalize()
    while True:
        sexo = str(input("Digite o sexo (M/F): ")).upper()[0]
        if sexo in "MF":
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    idade = int(input("Digite a idade: "))
    soma_idade += idade
    pessoas = dict()
    pessoas['nome'] = nome
    pessoas['sexo'] = sexo
    pessoas['idade'] = idade
    lista_pessoas.append(pessoas)
    print("Cadastro realizado!")
    while True:
        escolha = str(input("Deseja realizar outro cadastro(S/N)? ")).upper()[0]
        if escolha in "SN":
            break
        print("ERRO! Por favor, digite apenas S ou N.")
    if escolha == 'N':
        break
cadastro = len(lista_pessoas)
media = soma_idade/cadastro
print("-="*30)
print(f"Ao todo temos {cadastro} pessoas cadastradas!")
print(f"A media de idade e de {media:.2f} anos")
print("As mulheres cadastradas foram:", end="")
for i in lista_pessoas:
    if i['sexo'] == 'F':
        print(i['nome'], end=" ")
print("")
print("Lista das pessoas que estao acima da media:")
for i in lista_pessoas:
    if i['idade'] > media:
        print(f"   nome = {i['nome']}; sexo = {i['sexo']}; idade = {i['idade']};")
print("<<ENCERRADO>>")
    

    