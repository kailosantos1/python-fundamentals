from datetime import date

ano = int(input("Digite o ano que o atleta nasceu: "))

idade = date.today().year - ano

if idade <= 9:
    print(f"O atleta ainda esta na categoria mirim, idade: {idade}")
elif idade <= 14:
    print(f"O atleta ainda esta na categoria infantil, idade: {idade}")
elif idade <= 19:
    print(f"O atleta se encontra na categoria junior, idade: {idade}")
elif idade <= 20:
    print(f"O atleta se econtra na categoria senior, idade: {idade}")
else:
    print(f"O atleta esta na categoria master, idade: {idade}")