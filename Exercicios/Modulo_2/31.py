cedula_50 = 0
cedula_20 = 0
cedula_10 = 0
cedula_1 = 0

valor = int(input("Que valor voce quer sacar? R$"))

while valor >= 50:
    cedula_50 += 1
    valor -= 50
while valor >= 20:
    cedula_20 += 1
    valor -= 20
while valor >= 10:
    cedula_10 += 1
    valor -= 10
while valor >= 1:
    cedula_1 += 1
    valor -= 1

if cedula_50 > 0:
    print(f"Total de {cedula_50} cedulas de R$50")
if cedula_20 > 0:
        print(f"Total de {cedula_20} cedulas de R$20")
if cedula_10 > 0:
    print(f"Total de {cedula_10} cedulas de R$10")
if cedula_1 > 0:
    print(f"Total de {cedula_1} cedulas de R$1")

