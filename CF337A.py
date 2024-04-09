linha = input().split()

n = int(linha[0])
m = int(linha[1])
quebra_cabeca = []

linha_1 = input().split()

for lin in linha_1:
    quebra_cabeca.append(int(lin))

quebra_cabeca.sort()

dif = abs(quebra_cabeca[0] - quebra_cabeca[n - 1])
i = 0
j = n - 1
while(j < m):
    if dif > abs(quebra_cabeca[i] - quebra_cabeca[j]):
        dif = abs(quebra_cabeca[i] - quebra_cabeca[j])

    i += 1
    j += 1

print(dif)