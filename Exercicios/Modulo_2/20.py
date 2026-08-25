verificador = False
while verificador == False:
    sexo = str(input("Digite um sexo (M/F): ")).upper()
    if sexo == "M" or sexo == "F":
        print("Cadastrado com sucesso!")
        escolha = str(input("Deseja continuar (S/N)? ")).upper()
        if escolha == "N":
            verificador = True
    else:
        print("Valor invalido digite novamente!")    

    
    
    

