n = int(input())
linha = input().split()
while(n):
    for i in range(7):
        if n - int(linha[i]) <= 0:
            n = 0
            print(i + 1)
            break
        else:
            n -= int(linha[i])
    