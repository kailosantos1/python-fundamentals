numero = list()

while True:
    valores = int(input("Digite um valor:"))
    if valores in numero:
        print("Esse valor ja foi adicionado!", end=" ")
    else:
        numero.append(valores)
        print("Valor adicionador com sucesso!")
    escolha = str(input("Deseja continuar (S/N)?")).upper()[0]
    
    if escolha == 'N':
        print("Ate mais!")
        break

print(f"Os valores digitador sao: {sorted(numero)}")