cadastro = dict()

cadastro ['nome'] = str(input("Nome: ")).capitalize()
cadastro ['media'] = float(input("Media: "))

if cadastro['media'] >= 7:
    cadastro['situacao'] = 'aprovado'
    print(f"O aluno {cadastro['nome']} foi {cadastro['situacao']} com media: {cadastro['media']}")
else:
    cadastro['situacao'] = 'reprovado'
    print(f"O aluno {cadastro['nome']} foi {cadastro['situacao']} com media: {cadastro['media']}")