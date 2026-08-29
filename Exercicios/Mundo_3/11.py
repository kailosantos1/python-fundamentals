lista = []
pares = []
impares = []
while True:
    numeros = int(input("Digite um numero: "))
    escolha = str(input("Deseja continuar (S/N)? ")).upper()[0]
    lista.append(numeros)
    if numeros %2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)

    if escolha == "N":
        print("Ate mais!")
        break

print(f"A lista e: {lista}")
print(f"Os numeros pares sao: {pares}")
print(f"Os numeros impares sao: {impares}")