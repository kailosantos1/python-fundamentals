pilha = []
verificador = True
expresao = str(input("Digite a expressao: "))
for c in expresao:
    if c == '(':
        pilha.append(c)
    if c == ')':
        if pilha == []:
            verificador = False
        else:
            pilha.pop()
if pilha == [] and verificador == True:
    print("Expressao valida!")
else:
    print("Expressao invalida!")