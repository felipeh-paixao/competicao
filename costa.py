entrada = input()
entrada = entrada.split(' ')
M = int(entrada[0])
N = int(entrada[1])
mapa = []
contador = 0

for x in range(M):    
    mapa.append(input())

for i in range(M):
    for j in range(N):
        if (i == 0 or j == 0 or i == M - 1 or j == N - 1) and mapa[i][j] == '#':
            contador += 1
        elif mapa[i][j] == '#' and (mapa[i-1][j] == '.' or mapa[i + 1][j] == '.' or mapa[i][j - 1] == '.' or mapa[i][j + 1] == '.'):
            contador +=1

print(contador)
