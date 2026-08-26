mais_18 = 0
homens = 0
mulheres = 0
idade = 0
pessoas = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo (F/M): ")).upper()[0]
    print("Pessoa Cadastrada!")
    escolha = str(input("Deseja continuar (S/N)? ")).upper()[0]

    if sexo == "F" and idade < 20:
        mulheres += 1
        
    if idade > 18:
        mais_18 += 1
        
    if sexo == "M":
        homens += 1

    pessoas += 1
    if escolha == "N":
        break
    
print(f"Foram cadastradas {pessoas} pessoas!")
print(f"Foram cadastrados {homens} homens!")
print(f"Foram cadastrada {mulheres} mulheres com menos de 20 anos")