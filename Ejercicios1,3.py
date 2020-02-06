a = [1, 7, 22, 90, 32, 2, 92, 85, 12]
b = [1, 5, 77, 22, 90, 25, 83, 100, 2, 21, 90]
c = []

for numeroA in a:
    if numeroA not in b:
        c.append(numeroA)

for numeroB in b:
    if numeroB not in a:
        c.append(numeroB)

print(c)