frase = str(input("Digite uma frase: "))
nova_frase = frase.replace(" ", "")
polindromo = True

for verificador in range(len(nova_frase)//2):
    if nova_frase[verificador] != nova_frase[-1 - verificador]:
        polindromo = False
if polindromo == True:
    print("e um polindromo")
else:
    print("nao e um polindromo")
        
    
    

   
   
   




