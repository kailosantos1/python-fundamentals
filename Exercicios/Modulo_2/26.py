c = s = 0

while True:
    num = int(input("Digite um numero (escreva 999 para parar): "))

    if num == 999:
        print("Encerrando programa!")
        break   
    s += num
    c += 1
print(f"A soma dos {c} numero foi: {s}")