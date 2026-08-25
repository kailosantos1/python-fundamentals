valor = float(input("Qual o valor da casa? "))
salario = float(input("Qual o salario? "))
parcelas = int(input("Qual a quantidade de parcelas? "))

prestacao = salario * 0.30
parcela = valor / parcelas

if parcela <= prestacao:
    print("Pode seguir com o emprestimo")
else:
    print("Emprestimo negado")