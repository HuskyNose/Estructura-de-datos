x = [1,2,4,4,4,5,7,9,11,13,14,15,16,16]
sin_repetir = []

for i in x:
    if i not in sin_repetir:
        sin_repetir.append(i)

print(sin_repetir)