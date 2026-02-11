calificaciones = [8,6,7,5,10,9,9,5,6,10]

suma = 0
for i in calificaciones:
    suma = suma + i
promedio = suma / len(calificaciones)

reprobatoria = 0
aprobatoria = 0
for i in calificaciones:
    if i > 5:
        aprobatoria = aprobatoria + 1
    else:
        reprobatoria = reprobatoria + 1
        
porcentaje_aprobados = (aprobatoria / 10) * 100
porcentaje_reprobatoria = (reprobatoria / 10) * 100
        

exentos = 0
for i in calificaciones:
    if i >= 8:
        exentos = exentos + 1
        
print ('Alumnos aprobados', aprobatoria,
       'Alumnos reprobados', reprobatoria)
print ('Alumnos exentos', exentos)
print ('Porcentaje reprobados:', porcentaje_reprobatoria)
print ('Porcentaje aprobados:', porcentaje_aprobados)

