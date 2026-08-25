distancia = float(input("Digite a distancia da viagem em km: "))


if distancia <= 200:
    preco = distancia * 0.50
    print(f"o preco da passagem e: {preco}")
else:
    preco = distancia * 0.45
    print(f"o preco da passagem e: {preco}")
