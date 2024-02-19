import math
t = int(input())
while(t):
    ultimo = -1
    primeiro = 0
    linha_1 = input().split()
    n = int(linha_1[0])
    m = int(linha_1[1])
    num = input().split()
    for i in range(n):
        num[i] = int(num[i])
    instrucoes = input()
    produto = math.prod(num)
    
    for i in range(n):
        if i < n - 1:
            print(produto%m,end=' ')
        else:
            print(produto%m)
        if instrucoes[i] == 'L':
            produto //= num[primeiro]
            primeiro += 1            
        else:
            produto //= num[ultimo]
            ultimo -= 1
    t -= 1