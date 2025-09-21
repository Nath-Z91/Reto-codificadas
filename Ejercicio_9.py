from collections import deque
import sys
import copy

def bfs(grilla, hongo_pos, n, m):
    visitado = [[False]*m for _ in range(n)]
    q = deque()
    q.append(hongo_pos)
    visitado[hongo_pos[0]][hongo_pos[1]] = True

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visitado[nx][ny] and grilla[nx][ny] == 'Q':
                    visitado[nx][ny] = True
                    q.append((nx, ny))
    return visitado

def resolver(grilla):
    n = len(grilla)
    m = len(grilla[0])
    queso_total = [(i,j) for i in range(n) for j in range(m) if grilla[i][j] == 'Q']
    hongo_pos = next((i,j) for i in range(n) for j in range(m) if grilla[i][j] == 'H')

    # Caso base: sin eliminar nada
    alcanzables = bfs(grilla, hongo_pos, n, m)
    if any(not alcanzables[i][j] for i,j in queso_total):
        return 0

    # Probar eliminar 1, 2,..., hasta que al menos un queso quede aislado
    for k in range(1, len(queso_total)+1):
        from itertools import combinations
        for eliminar in combinations(queso_total, k):
            nueva = copy.deepcopy(grilla)
            for x, y in eliminar:
                nueva[x][y] = '.'
            alcanzables = bfs(nueva, hongo_pos, n, m)
            if any(nueva[i][j] == 'Q' and not alcanzables[i][j] for i,j in queso_total):
                return k
    return len(queso_total)

# Ejemplo de uso
grilla = [
    list("..Q.."),
    list(".HQ.Q"),
    list("QQQQQ"),
    list("..Q..")
]

print(resolver(grilla))  # Devuelve el mínimo número de celdas a eliminar


