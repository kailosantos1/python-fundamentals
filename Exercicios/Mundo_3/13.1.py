temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp = []
    escolha = str(input("Deseja continuar (S/N)? ")).upper()[0]
    if escolha == "N":
        print("Ate mais!") 
        break

print(f"A quantidade de pessoas cadastradas foi de: {len(princ)}")
print(f"O maior pesso foi de {mai}Kg. Peso de ", end='')
for p in princ:
    if p[1] == mai:
        print(f"{p[0]}", end= ' ')

print(f"\nO menor pesso foi de {men}Kg. Peso de ", end='')
for p in princ:
    if p[1] == men:
        print(f"{p[0]}", end= ' ')
