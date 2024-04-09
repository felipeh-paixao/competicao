t = int(input())

while(t):

    z = 0
    teste = 0
    square = []
    linha = input().split()

    n = int(linha[0])
    c = int(linha[1])
    d = int(linha[2])

    linha_1 = input().split()
    x = 0
    y = n
    while(y <= n * n):
        square.append(linha_1[x:y])

        x += 3
        y += 3
    
    for i in range(n - 1):
        for j in range(n - 1):            
            if int(square[i + 1][j]) == int(square[i][j]) + c and int(square[i][j + 1]) == int(square[i][j]) + d:
                teste += 1 

        if teste == 3:
            z += 1
            teste = 0
    
    if z == n * n:
        print('YES')
    else:
        print('NO')

    t -= 1