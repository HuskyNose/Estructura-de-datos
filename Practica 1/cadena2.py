cadena2 = "Parangaricutirimicuaro"
letras = {}
 
for i in cadena2:
     if i in letras:
         letras[i] = letras[i] + 1 
     else:
         letras[i] = 1
for l in letras:
    print (l, "=", letras[l])     
        