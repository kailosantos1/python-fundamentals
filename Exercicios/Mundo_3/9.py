

numeros = []
for n in range(0,5):
    valores = int(input("Digite um valor: "))
    if not numeros:
        numeros.insert(5,valores)
        print(f"{valores} inserido ao final da lista...")
    else:
        for pos, v in enumerate(numeros):
            if v  > valores:
                numeros.insert(pos, valores)
                print(f"{valores} inserido na posicao: {pos}")
                break
        else:
            numeros.append(valores)
            print(f"{valores} inserido na posicao: {len(numeros)- 1}")

print(numeros)