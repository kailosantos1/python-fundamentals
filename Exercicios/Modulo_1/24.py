velocidade = float(input("Digite a velocidade do carro: "))

multa = (velocidade - 80) * 7

print(multa)
if velocidade > 80:
    print(f"Voce foi multado em R$ {multa:.2f}")

else:
    print("voce esta dentro do limite de velocidade")