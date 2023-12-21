t = int(input())

for x in range(t):
    
    linha_1 = input().split()
    k = int(linha_1[0])
    n = int(linha_1[1])
    sequencia = input()
    contador = 0
    i = 0
    while(i < len(sequencia)):
        if sequencia[i] == 'B':
            contador += 1
            i += n
        else:
            i += 1
    
    print(contador)  
 