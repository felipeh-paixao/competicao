t = int(input())

for z in range(t):
    linha_1 = input().split()
    n = int(linha_1[0])
    x = int(linha_1[1])
    h = 1

    alturas = input().split()
    alturas.sort()
    linhas = int(alturas[-1])

    for i in range(linhas):
        for j in range(n):
            if int(alturas[i][j]) < h:
                x -= 1
            else:
                h += 1
                
