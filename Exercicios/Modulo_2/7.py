peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura * altura)

if imc <18.5:
    print(f"Voce esta abaixo do peso, IMC: {imc:.2f} ")
elif imc <= 25:
    print(f"Voce esta no peso ideal, IMC: {imc:.2f}")
elif imc <30:
    print(f"Voce esta com sobrepeso, IMC: {imc:.2f}")
elif imc <40:
    print(f"Voce esta obeso, IMC: {imc:.2f}")
else:
    print(f"Voce esta com Obesidade Morbida, IMC: {imc:.2f}")
