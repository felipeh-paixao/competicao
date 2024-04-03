n = int(input())
max_linha = 4 * n + 1

for i in range(n):
    espaco = max_linha - i + 1 - 1
    print(' ' + str(i))
