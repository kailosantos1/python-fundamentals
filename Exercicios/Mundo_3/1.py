numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

escolha = int(input("digite um numero: "))
while True:
    
    if escolha >= 0 and escolha < 11:
        escolha = numero[escolha]
        print(escolha)
        break
    else:
        escolha = int(input("tente novamente! digite um numero: "))

