cases = int(input())

for x in range(cases):
    pontuacao = 0
    rings = []
    for k in range(10):
        rings.append(input())
    
    for i in range(10):
        for j in range(10):          

            if(i == 0 or j == 0 or j == 9 or i == 9) and rings[i][j] != '.':
                pontuacao += 1
            elif(i == 1 or i == 8 or j == 1 or j == 8)  and  rings[i][j] != '.':
                pontuacao += 2
            elif(i == 2 or i == 7 or j == 2 or j == 7) and rings[i][j] != '.':
                pontuacao += 3
            elif (i == 3 or i == 6 or j == 3 or j == 6) and rings[i][j] != '.':
                pontuacao += 4
            elif rings[i][j] != '.':
                pontuacao += 5
            
    
    print(pontuacao)
    

