toneladas_cereal = [12,24,16,15,20,18,6,10,12,11,15,12]

suma = 0
for i in toneladas_cereal:
    suma = suma + i
promedio = suma / len(toneladas_cereal)

valmayor = []
mayores = 0
for i in toneladas_cereal:
    if i > promedio:
        mayores = mayores + 1
        valmayor.append(i)
    
valinferior = []    
menores = 0
for t in toneladas_cereal:
    if t < promedio:
        menores = menores + 1
        valinferior.append(t)
    
    

print ('Promedio anual:', promedio)
print ('Valores superiores al promedio',mayores)
print ('Valores menores al promedio',menores)
print (valmayor)
print (valinferior)
