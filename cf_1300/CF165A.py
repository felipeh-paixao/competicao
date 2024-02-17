n = int(input())
pontos = []
contador = 0
i = 0
while(i < n):
    linha = input().split()
    vet = [int(linha[0]), int(linha[1])]
    pontos.append(vet)
    i += 1
pontos.sort()

for ponto in pontos:
  maior_y = 0
  menor_y = 0
  maior_x = 0
  menor_x = 0
  for j in range(n):     
    if ponto[0] == pontos[j][0]:      
      if ponto[1] > pontos[j][1]:
        maior_y = 1        
      if ponto[1] < pontos[j][1]:
        menor_y = 1
    if ponto[1] == pontos[j][1]:      
      if ponto[0] > pontos[j][0]:
        maior_x = 1
      if ponto[0] < pontos[j][0]:
        menor_x = 1
  if maior_x and maior_y and menor_x and menor_y:  
      contador += 1

print(contador)