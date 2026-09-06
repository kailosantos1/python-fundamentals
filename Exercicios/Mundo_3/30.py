from datetime import date

def voto(nasc):
    idade = date.today().year - nasc
    if idade < 16:
        return "VOTO NEGADO!"
    elif 16 <= idade <= 17 or idade > 70:
        return "VOTO OPCIONAL!"
    else:
        return "VOTO OBRIGATORIO"


ano = int(input("Digite o ano de nascimento: "))
resultado = voto(ano)
print(resultado)