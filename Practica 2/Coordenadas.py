matriz = [[4,7,2,9,5,7],
          [1,3,7,6,8,0],
          [9,2,5,7,4,6],
          [8,7,1,3,7,2],
          [5,0,6,4,2,9],
          [7,8,9,2,1,7]]

def buscar(m, objetivo):
    encontrados = []
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == objetivo:
                encontrados.append((i + 1, j + 1))
    
    if encontrados:
        return encontrados
    return "No Encontrado"

valores_a_buscar = [7, 2, 9, 0, 4, 1, 6, 8, 3, 10]

for v in valores_a_buscar:
    print(f"Buscando {v}...")
    print(f"Resultado: {buscar(matriz, v)}")
    print("-" * 30)