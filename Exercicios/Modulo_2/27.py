c = s = 0

while True:
    num = int(input("Digite um numero para ver a tabuada: "))

    if num < 0:
        print("Numero negativo detectado, encerrando programa!")
        break
    
    for tabuada in range(1,11):
        resultado = num * tabuada
        print(f"{num} X {tabuada} = {resultado}")