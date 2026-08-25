num  = int(input("Digite um numero para saber seu fatorial: "))
num1 = num
fatorial = 1
print(f"Calculando {num}! = ", end=" ")
while num1 > 0:
    print(f"{num1}", end= " ")
    print(f"x" if num1 > 1 else "=", end=" ")
    fatorial *= num1
    num1 -= 1
print(fatorial , end= " ")
