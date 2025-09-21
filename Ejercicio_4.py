def leer_grilla():
    grilla = []
    while True:
        try:
            linea = input()
            if linea.strip() == "":
                break
            grilla.append(linea)
        except EOFError:
            break
    return grilla

def detectar_flor(grilla):
    # Extraer solo las filas que contienen '*'
    ocupadas = [fila for fila in grilla if '*' in fila]
    if not ocupadas:
        return "No hay flor"

    
    patron = ''.join(ocupadas)

    
    verticales = sum(fila.count('*') for fila in zip(*ocupadas))
    horizontales = sum(fila.count('*') for fila in ocupadas)


    if patron.count('*')>= 20 and verticales>= 5:
        return "Triple Corolla Flower"
    else:
        return "Double Petal Flower"

grilla = leer_grilla()
print(detectar_flor(grilla))
