cadena = "Parangaricutirimicuaro"

minusculas = list("abcdefghijklmnopqrstuvwxyz")
mayusculas = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for l in minusculas:
    contador = 0
    for letra in cadena:
        if letra == l:
            contador += 1
    
    if contador > 0:
        print(f"{l} = {contador}")   
        
for L in mayusculas:
    contador = 0
    for letra in cadena:
        if letra == L:
            contador += 1
    if contador > 0:
        print(f"{L} = {contador}")
