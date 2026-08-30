# variaveis = temp, valores
# for para repetir 7 vezes e verificar os numeros dentro da lista temp, ja que nao posso usar matematica na lista
# if para ver se e par ou impar se for par joga dentro de valores no indece 0, se for impar jogar dentro de valores indice 1
valores = [[],[]]
temp = []
for n in range(0,7):
    temp.append(int(input("Digite um numero: ")))
    for c in temp:
        if c %2 == 0:
            valores[0].append(c)
        else:
            valores[1].append(c)
temp = []

print(f"Numeros pares dentro da lista: {sorted(valores[0])}")
print(f"Numeros impares dentro da lista: {sorted(valores[1])}")