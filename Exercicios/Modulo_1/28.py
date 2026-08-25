try:
    num1 = float(input("digite um numero: "))
    num2 = float(input("digite outro numero: "))
    num3 = float(input("digite outro numero: "))

    if num1 > num2 and num1 > num3:
        maior = num1
    elif num2 > num3:
        maior = num2
    else:
        maior = num3

    if num1 < num2 and num1 < num3:
        menor = num1
    elif num2 < num3:
        menor = num2
    else:
        menor = num3

    print(f"maior numero e {maior}")
    print(f"menor numero e {menor}")

except ValueError:
    print("Erro: Digite apenas números válidos! Letras e caracteres especiais não são aceitos.")
