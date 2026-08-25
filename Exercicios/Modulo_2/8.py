valor_produto = float(input("Qual o valor do produto? "))
pagamento = str(input("Qual a forma de pagamento? (avista, cheque, cartao) "))

if pagamento == 'avista' or pagamento == 'cheque':
    desconto = valor_produto * 0.10
    valor_final = valor_produto - desconto
    print(f'forma de pagamento escolhida foi {pagamento}, o valor total a ser pago com desconto e de: {valor_final}')

elif pagamento == 'cartao':
    parcelas = int(input(f"Em quantas vezes ira fazer?"))
    if parcelas <= 1:
        desconto = valor_produto * 0.05
        valor_final = valor_produto - desconto
        print(f'forma de pagamento escolhida foi {pagamento}, em {parcelas} o valor total a ser pago com desconto e de: {valor_final}')
    elif parcelas == 2:
        print(f'forma de pagamento escolhida foi {pagamento}, em {parcelas} o valor total a ser pago e de: {valor_produto}')
    else:
        juros = valor_produto * 0.20
        valor_final = valor_produto + juros
        print(f'forma de pagamento escolhida foi {pagamento}, em {parcelas} o valor total a ser pago com juros e de: {valor_final}')
else:
    print("Digite um valor valido")
    