guardador = tuple()
pares = tuple()
for c in range(0,4):
    numeros = int(input("Digite um valor: "))
    guardador += (numeros,)

print(f"O numero 9 apareceu: {guardador.count(9)}")
print(f"o numero 3 esta na posicao: {guardador.index(3)}")

for par in guardador:
    if par %2 ==0:
        pares += (par, )
    

print(f"os numeros pares sao: {pares}")
    
