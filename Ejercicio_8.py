def es_valido(d, personas, bodegas, capacidades):
    i = 0  # índice de persona
    n = len(personas)
    for b, cap in zip(bodegas, capacidades):
        atendidos = 0
        while i < n and abs(personas[i] - b) <= d and atendidos < cap:
            i += 1
            atendidos += 1
        if i == n:
            return True
    return i == n

def menor_distancia(personas, bodegas, capacidades):
    personas.sort()
    bodegas_cap = sorted(zip(bodegas, capacidades))
    bodegas = [b for b, _ in bodegas_cap]
    capacidades = [c for _, c in bodegas_cap]

    low, high = 0, 10**9
    res = high
    while low <= high:
        mid = (low + high) // 2
        if es_valido(mid, personas, bodegas, capacidades):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res

# Entrada
n, k = map(int, input().split())
personas = list(map(int, input().split()))
bodegas = list(map(int, input().split()))
capacidades = list(map(int, input().split()))

# Salida
print(menor_distancia(personas, bodegas, capacidades))

