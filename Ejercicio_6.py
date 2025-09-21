from collections import defaultdict

n = int(input())
puntos = [tuple(map(int, input().split())) for _ in range(n)]

# Diccionario: suma de coordenadas → lista de pares de índices
suma_medios = defaultdict(list)

for i in range(n):
    for j in range(i + 1, n):
        x_sum = puntos[i][0] + puntos[j][0]
        y_sum = puntos[i][1] + puntos[j][1]
        key = (x_sum, y_sum)
        suma_medios[key].append((i, j))

# Buscar dos pares con misma suma y sin puntos repetidos
for pares in suma_medios.values():
    if len(pares)>= 2:
        for a in range(len(pares)):
            for b in range(a + 1, len(pares)):
                i1, j1 = pares[a]
                i2, j2 = pares[b]
                # Verificar que los 4 puntos sean distintos
                if len({i1, j1, i2, j2}) == 4:
                    print("YES")
                    exit()

print("NO")