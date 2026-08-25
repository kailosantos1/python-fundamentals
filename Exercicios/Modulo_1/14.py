dias = int(input("Digite o numero de dias alugados: "))
km = float(input("Digite o numero de km rodados: "))

preco = (dias * 60) + (km * 0.15)
print(f"O preco a pagar e R${preco:.2f}.") 