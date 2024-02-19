t = int(input())
for i in range(t):
    contador = 0
    n = int(input())
    linha = input()
    for j in range(n):        
        if linha[j] == '@':
            contador += 1
        elif linha[j] == '*':
            if j < n - 2:
                if linha[j+1] == '*':
                    break
    print(contador)
    