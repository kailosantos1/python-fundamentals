try:
    salario = float(input("digite o salario: "))

    if salario > 1250:
        aumento = salario * 0.10

    else:
        aumento = salario * 0.15

    novo_salario = salario + aumento
    print(f"o aumento foi de {aumento:.2f}")
    print(f"O novo salário é: R$ {novo_salario:.2f}")
except ValueError:
    print("digite um numero valido")