# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

pessoa = dict()

nome = str(input("Digite o nome: ")).capitalize()
nascimento = int(input("Digite o ano de nascimento: "))
qts_carteira = str(input("Essa pessoa tem carteira de trabalho (S/N)? ")).upper()[0]

idade = date.today().year - nascimento

pessoa['nome'] = nome
pessoa['idade'] = idade


if qts_carteira == "S":
    carteira_trabalho = int(input("Digite o numero da carteira de trabalho: "))
    contratacao = int(input("Qual o ano de contratacao? "))
    salario = int(input("Qual o salario? "))
    pessoa['carteira'] = carteira_trabalho

    aposentadoria = pessoa["idade"] + ((contratacao + 35) - date.today().year)

    pessoa['contratacao'] = contratacao
    pessoa['salario'] = salario
    pessoa['aposentadoria'] = aposentadoria

    print("-="*30)
    print(f"O nome da pessoa e: {pessoa["nome"]}")
    print(f"A pessoa tem: {pessoa["idade"]} anos de idade")
    print(f"A pessoa tem a carteira de trabalho numero: {pessoa["carteira"]}") 
    print(f"A pessoa foi contratada no ano de: {pessoa["contratacao"]}")
    print(f"A pessoa tem o salario igual a: {pessoa["salario"]}")
    print(f"A pessoa vai se aposentar com a idade igual a: {pessoa["aposentadoria"]}")

else:
    print("-="*30)
    print(f"O nome da pessoa e: {pessoa["nome"]}")
    print(f"A pessoa tem: {pessoa["idade"]} anos de idade")
    print("Ela nao tem carteira de trabalho!")




