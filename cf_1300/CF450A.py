import math
linha_1 = input().split()
n = int(linha_1[0])
m = int(linha_1[1])
linha_2 = input().split()
amigos = []
for linha in linha_2:
    amigos.append(math.ceil(int(linha)/m))

maior =  max(amigos)
posicao = amigos.index(maior)

for i in range(posicao, n, 1):
    if amigos[i] == maior:
        posicao = i + 1

print(posicao)