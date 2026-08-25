
lista_pesos = []
pesos = 0


for i in range (1,6):
    peso = float(input("Digite seu peso: "))
    lista_pesos.append(peso)

maior_peso = lista_pesos[0]
menor_peso = lista_pesos[0]

for peso in lista_pesos:
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
print(maior_peso)
print(menor_peso)
