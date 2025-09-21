n = int(input())
frecuenci_total = {}
personas_con_palabras = {}

for_in = range(n);m = int(input()); palabra_persona = set()
for_in = range(m); palabra = input()

frecuenci_total = [palabra] = frecuenci_total.get(palabra,0) + 1


# Buscar palabras que aparesca en todas las personas

comunes = [p for p in frecuenci_total if personas_con_palabras.get(p,0) == n]

#Ordenar

comunes.sort(key=lambda p:(frecuenci_total[p],p),reverse= True)

for  palabra in comunes:
    print('palabra')







 