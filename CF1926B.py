t = int(input())
while(t):
    n = int(input())
    matrix = []
    contador = 0
    teste = 0
    for i in range(n):
        linha = input()
        if linha.count('1'):
            matrix.append(linha.count('1'))

    contador = matrix[0]

    for mat in matrix:
        if mat != contador:
            teste = 1
    
    if(teste):
        print('TRIANGLE')  
    else:
        print('SQUARE')  

    t -= 1