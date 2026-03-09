from collections import deque

max_val = 3
tiempo_Limite = 10
bicola = deque()
peticiones = [
    (1, 0),
    (2, 2),
    (3, 4),
    (4, 6),
    (5, 12)
]

inicio = peticiones[0][1]

for i, tiempo in peticiones:
    if tiempo - inicio < tiempo_Limite:
        if len(bicola) < max_val:
            bicola.append(i)
            print(list(bicola))
        else:
            bicola.popleft()
            bicola.append(i)
            print(list(bicola))
            
    else:
        while bicola:
            bicola.popleft()
            if bicola:
                print(list(bicola))
        
        inicio = tiempo
        bicola.appendleft(i)
        print(list(bicola))