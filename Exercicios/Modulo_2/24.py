verificador = True
c = 0
soma = 0
while verificador == True:
    num = int(input("Digite um numero: "))

    if num != 999:
        c += 1
        soma += num
    else:
        verificador = False

print(f"Quantidade de numeros digitados: {c} e a soma e: {soma} ")