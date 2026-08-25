num = int(input("Digite um numero: "))
conversao = str(input("Qual a base de conversao? (1-binario,2-octal,3-hexadecimal)"))

if conversao == "1":
    binario = format(num,'b')
    print(f"o numero em binario e: {binario}")
elif conversao == "2":
    octal = format(num,'o')
    print(f"o numero em octal e: {octal}")
else:
    hexa = format(num,'x')
    print(f"o numero em hexadecimal e: {hexa}")
