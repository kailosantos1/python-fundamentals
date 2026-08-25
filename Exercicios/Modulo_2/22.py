num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))
menu = True

while menu == True:

    print("[1] - Somar")
    print("[2] - Multiplicar")
    print("[3] - Maior")
    print("[4] - Novos Numeros")
    print("[5] - Sair do programa")

    escolha = int(input("Escolha uma opcao: "))

    if escolha == 1:
        soma = num1 + num2
        print(f"A soma entre {num1} e {num2} e: {soma}")
    elif escolha == 2:
        mult = num1 * num2
        print(f"A multiplicacao entre {num1} e {num2} e: {mult}")
    elif escolha == 3:
        if num1 > num2:
            print(f"O maior numero entre {num1} e {num2} e: {num1}")
        elif num2 > num1:
            print(f"O maior numero entre {num1} e {num2} e: {num2}")
        elif num2 == num1:
             print(f"Os numeros {num1} e {num2} sao iguais!")
    elif escolha == 4:
            num1 = float(input("Digite o novo numero: "))
            num2 = float(input("Digite outro numero: "))
    elif escolha == 5:
        print("Ate mais!")
        menu = False
    else:
         print("Opcao invalida digite um numero que existe no menu!")