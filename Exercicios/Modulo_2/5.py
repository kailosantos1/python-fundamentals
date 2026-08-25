nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if media >= 7:
    print(f"Parabens voce foi aprovado sua nota e: {media}")
elif media >= 5:
    print(f"Esta de recuperacao sua nota foi: {media}")
else:
    print(f"Que azar tente de novo ano que vem sua nota foi: {media}")
