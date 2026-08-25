tot_mais_velho = 0
tot_nova = 0
soma_idade = 0
nome_mais_velho = str()

for pessoas in range(1,5):
    nome = str(input("Qual o seu nome? "))
    idade = int(input("Qual a sua idade? "))
    sexo = str(input("Qual seu sexo? (F/M)")).upper()

    soma_idade += idade
    if sexo == "M" and idade > tot_mais_velho:
        tot_mais_velho = idade
        nome_mais_velho = nome

    if sexo == "F" and idade < 20:
        tot_nova += 1


media_idades = soma_idade /pessoas
print(f"a media de todas as idades e: {media_idades}")
print(f"o nome da pessoa mais velha entre os homens e: {nome_mais_velho}, idade: {tot_mais_velho}")
print(f"quantidade de mulheres a baixo de 20 anos: {tot_nova}")
