num = int(input("Digite um numero: "))

e_primo = True

for primo in range(2, num):
    if num %primo == 0:
        e_primo = False
if e_primo == True:
    print(f"o numero {num} e primo")
else:
    print(f"o numero {num} nao e primo")

