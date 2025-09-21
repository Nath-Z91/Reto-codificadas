def expand(figura, base, n):
    nueva = []
    for fila in figura:
        bloques = []
        for c in fila:
            if c == '#':
                bloques.append(base)
            else:
                bloques.append(['.' * n] * n)
        # Combinar horizontalmente los bloques
        for i in range(n):
            nueva.append(''.join(b[i] for b in bloques))
    return nueva

def papel_tapiz(base, k):
    n = len(base)
    figura = base
    for _ in range(k - 1):
        figura = expand(figura, base, n)
    return figura