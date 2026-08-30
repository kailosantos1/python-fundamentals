matriz = [[0,0,0], [0,0,0], [0,0,0]]
pares = 0
soma_c = 0
for l in range(0,3):
    for c in range(0,3):
        matriz [l] [c] = int(input(f"Digite um valor para [{l}], [{c}]:"))
for linha in matriz:
    for n in linha:
        if n %2 == 0:
            pares += n
for linha in matriz:
    soma_c += linha[2]

print(f"A soma de todos os valores pares e: {pares}")
print(f"A soma da terceira coluna e: {soma_c}")
print(f"O maior numero da segunda linha e: {max(matriz[1])}")
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz [l] [c]:^5}]", end='')
    print()