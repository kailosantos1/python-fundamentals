def maior(*valores):
    if valores == ():
        print("Nenhum valor foi informado")
    else:
        print(f"foram informados {len(valores)} valores: {valores}, o maior valor foi: {max(valores)}")

maior(3,7,10)
maior(2,10)
maior()
