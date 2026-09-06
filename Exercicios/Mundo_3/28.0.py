lista = []

def maior():
    while True:
        num = int(input("Digite um valor: "))
        lista.append(num)
        escolha = input("Deseja digitar outro valor? (S/N) ").upper() [0]
        if escolha == "N":
            break
    print(max(lista))

maior()
