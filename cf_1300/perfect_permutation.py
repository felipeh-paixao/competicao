n = int(input())
aux = 0
permutation = []
if n % 2 == 1:
    print(-1)
else:
    for i in range(1, n + 1, 1):
        permutation.append(i)
    
    for i in range(0, n, 2):
        aux = permutation[i + 1]
        permutation[i + 1] = permutation[i]
        permutation [i] = aux

    for i in range(n):
        if(i < n - 1):
            print(permutation[i], end = ' ') 
        else:
            print(permutation[i], end = '')
