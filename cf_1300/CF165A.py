n = int(input())
parada = n * 2
pontos = []
contador = 0
while(n):
    linha = input().split()
    for lin in linha:
        pontos.append(int(lin))
    
    n -= 1

maior_x = pontos[0]
menor_x = pontos[0]

for i in range(0, parada, 2):
    if maior_x < pontos[i]:
        maior_x = pontos[i]
    if menor_x > pontos[i]:
        menor_x = pontos[i]

maior_y = pontos[1]
menor_y = pontos[1]

for i in range(1, parada, 2):
    if maior_y < pontos[i]:
        maior_y = pontos[i]
    if menor_y > pontos[i]:
        menor_y = pontos[i]
for i in range(0, parada, 2):
    if pontos[i] > menor_x and pontos[i] < maior_x:
        if pontos[i + 1] > menor_y and pontos[i + 1] < maior_y:
            contador += 1
            print(f'{pontos[i]} {pontos[i + 1]}')

print(contador)