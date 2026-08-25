verificador = True
c = 0
a = 0
media = 0

while verificador == True:
    num = float(input("Digite um numero: "))

    if a == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
 
    c += num
    a += 1     

    escolha = str(input("Deseja continuar (S/N)? ")).upper()
    if escolha == "N":
        verificador = False



media = c / a
print(f"A media e: {media}")
print(f"O maior numero digitado foi: {maior}")
print(f"O menor numero digitado foi: {menor}")