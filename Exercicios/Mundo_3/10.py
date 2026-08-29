lista = []

while True:
    lista.append(int(input("Digite um numero para adicionar na lista: ")))
    escolha = str(input("Deseja continuar a incluir numeros (S/N)? ")).upper()[0]
    if escolha == "N":
        break

print(f"A lista e: {lista}")
print(f"Foram digitados: {len(lista)} numeros")
print(f"A lista ordenada de forma descrescente fica: {sorted(lista, reverse= True)}")
if 5 in lista:
    print(f"O numero 5 esta na lista e foi digitado: {lista.count(5)} vez")
else:
    print("O numero 5 nao foi digitado!")
