from random import randint

numeros= []
pares = []
impares = []
def sorteia():
    for n in range(0,5):
        numero = randint(0,1000)
        numeros.append(numero)
    print(f"Os numeros sorteados foram: {numeros}")
def somaPar():
    somapares = 0
    contpares = 0
    contimpares = 0
    for n in numeros:
        if n %2 == 0:
            pares.append(n)
            somapares += n
            contpares += 1
        if n %2 != 0:
            impares.append(n)
            contimpares += 1
    if contpares >= 1:
        print(f"Os numeros pares sao: {pares}, ao total sao: {contpares} numeros e a soma deles da: {somapares}")
    else:
        print("Nao tem numeros pares!")
    if contimpares >= 1:
        print(f"Os numeros impares sao: {impares}, ao total sao: {contimpares} numeros")
    else:
        print("Nao tem numeros impares!")
        
sorteia()
somaPar()





