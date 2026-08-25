verificador = True
c = 0
a = 0
comparador = 0
media = 0
maior = 0
menor = 0

while verificador == True:
    num = float(input("Digite um numero: "))

    if comparador != num:
        if comparador < num and maior < num:
                maior = num
        if comparador > num and menor > num:
           menor = num

    comparador = num   
    c += num
    a += 1

    print(comparador)    
    print(maior)
    print(menor)   
#     escolha = str(input("Deseja continuar (S/N)? ")).upper()
#     if escolha == "N":
#         verificador = False



# media = c / a
# print(f"A media e: {media}")
