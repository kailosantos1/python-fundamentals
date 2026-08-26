preco_total = 0
mais_1k = 0
nome_1k = []
mais_caro = 0
mais_barato = 0
nome_barato = str()
nome_caro = str()
while True:
    nome_produto = str(input("Digite o nome do produto: "))
    preco_produto = float(input("Digite o preco do produto: "))

    if preco_total == 0:
        mais_caro = preco_produto
        nome_caro = nome_produto
        mais_barato = preco_produto
        nome_barato = nome_produto
    else:
        if preco_produto > mais_caro:
            mais_caro = preco_produto
            nome_caro = nome_produto
        if preco_produto < mais_barato:
            mais_barato = preco_produto
            nome_barato = nome_produto

    if preco_produto > 1000:
        mais_1k += 1
        nome_1k.append(nome_produto)

    preco_total += preco_produto
    print(f"Produto inserido no carrinho! seu carrinho esta no total de {preco_total:.2f}")
    escolha = str(input("Deseja continuar (S/N): ")).upper()[0]

    if escolha == "N":
        break

print(f"O valor total gasto na compra foi de {preco_total:.2f}")
print(f"O produto {nome_1k} custaram mais de R$ 1.000,00")
print(f"O produto {nome_barato} foi o mais barato, custando {mais_barato}")
print(f"O produto {nome_caro} foi o mais caro, custando {mais_caro}")