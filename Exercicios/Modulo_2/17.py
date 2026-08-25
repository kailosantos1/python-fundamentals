lista_idade = []
idade = 0
lista_idade_maiores = []
lista_idade_menores = []
verificador_idade = True

for receber_idade in range(1,8):
    idade = int(input("Qual a sua idade? "))
    lista_idade.append(idade)

for i in lista_idade:
    if i >= 18:
        verificador_idade = True
        lista_idade_maiores.append(i)    
    else:
        lista_idade_menores.append(i)

if verificador_idade == True:
    print(f"maiores que 18: {lista_idade_maiores}")
print(f"menores de 18: {lista_idade_menores}")