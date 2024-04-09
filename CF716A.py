linha = input().split()
n = int(linha[0])
t = int(linha[1])
contador = 1

time = input().split()

for i in range(1, n, 1):
    if int(time[i]) - int(time[i - 1]) <= t:
        contador += 1
    else:
        contador = 1

print(contador)
