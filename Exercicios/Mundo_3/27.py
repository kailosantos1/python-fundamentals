import time


def contador(inicio, fim, passo):

    for c in range (inicio,fim,passo):
        time.sleep(0.5)
        print(c)

contador (1, 11, 1)
contador (10, -1, -2)

inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))
if inicio > fim:
    final = fim - 1
else:
    final = fim + 1
passo = int(input("Digite o passo: "))
contador (inicio, final, passo)


