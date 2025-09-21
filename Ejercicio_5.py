A, B, C, D = map(int, input().split())

semanas = 0
ardillas = C

while ardillas <= D:
    semanas += 1
    ardillas = A * ardillas + B

print(semanas)