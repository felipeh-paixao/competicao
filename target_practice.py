cases = int(input())

for x in range(cases):
    pontuacao = 0
    rings = []
    
    for k in range(10):
        rings.append(input())
    cont = 1
    for i in range(10):
        for j in range(10):
            print(rings[i][j])
            if i <= 4:
                z = i
            else:
                z = i - cont
                cont += 1

            if(z == 0 or j == 0) and rings[i][j] != '.':
                pontuacao += 1
            elif z == 1  and 0 < j < 9 and  rings[i][j] != '.':
                pontuacao += 2
            elif z == 2 and 1 < j < 8 and rings[i][j] != '.':
                pontuacao += 3
            elif z == 3 and 2 < j < 7 and rings[i][j] != '.':
                pontuacao += 4
            else:
                pontuacao += 5
            
    
    print(pontuacao)
    

