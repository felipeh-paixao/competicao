n = int(input())
parada = n * 2
pontos = []
contador = 0
i = 0
while(i < n):
    linha = input().split()
    vet = [linha[0], linha[1]]
    pontos.append(vet)
    i += 1
pontos.sort()
print(pontos)
