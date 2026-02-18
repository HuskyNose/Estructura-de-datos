import pandas as pd

df = pd.read_csv('housing.csv')

price = list(df['price'])
bedrooms = list(df['bedrooms'])
bathrooms = list(df['bathrooms'])
sqft_living = list(df['sqft_living'])
sqft_lot = list(df['sqft_lot'])
floors = list(df['floors'])
sqft_above = list(df['sqft_above'])
sqft_basement = list(df['sqft_basement'])
yr_built = list(df['yr_built'])

def calcularParametros(lista, nombre_columna):
    n = len(lista)
    
    suma = 0
    for x in lista:
        suma += x
    media = suma / n
    
    conteo = {}
    for x in lista:
        conteo[x] = conteo.get(x, 0) + 1
        
    moda = lista[0]
    max_reps = 0
    for valor, reps in conteo.items():
        if reps > max_reps:
            max_reps = reps
            moda = valor
    
    suma_cuadrados = 0
    for x in lista:
        suma_cuadrados += (x - media) ** 2
    varianza = suma_cuadrados / (n - 1)
    desviacion = varianza ** 0.5
    
    
            
    print("--Estadísticas de" ,nombre_columna)
    print("--Media:" ,media)
    print("--Moda:" ,moda)
    print("--Varianza:" ,varianza)
    print("--Desviación Estándar:" ,desviacion)
    print('------------------------------------')



calcularParametros(price, "Precio")
calcularParametros(bedrooms, "Habitaciones")
calcularParametros(bathrooms, "Baños")
calcularParametros(sqft_living, "Pies Cuadrados Habitables")
calcularParametros(sqft_lot, "Pies Cuadrados del Lote")
calcularParametros(floors, "Pisos")
calcularParametros(sqft_above, "Pies Cuadrados por Encima del Suelo")
calcularParametros(sqft_basement, "Pies Cuadrados del Sótano")
calcularParametros(yr_built, "Año de Construcción")