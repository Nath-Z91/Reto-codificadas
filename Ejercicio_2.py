n = int(input())
cadena = input()

if all(c in {'T','C','S'} 
       for c in cadena):print('YES')
else:
    print('NO')