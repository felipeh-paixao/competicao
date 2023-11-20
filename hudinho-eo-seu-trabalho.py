N = int(input())
nomes = []
for nome in range(N):
    auxiliar = input()
    nomes.append(auxiliar)

for i in range(N):
    for j in range(N - 1 - i):
        if nomes[j][0] > nomes [j + 1][0]:
            auxiliar = nomes [j + 1]
            nomes[j + 1] = nomes [j]
            nomes [j] = auxiliar
            
for nome in nomes:
    print(nome)
