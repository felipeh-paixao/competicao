t = int(input())

while(t):
    linha = input().split()
    
    n = int(linha[0])
    a = int(linha[1])
    b = int(linha[2])
    
    if a * 2 < b:
        print(n * a)
    else:
        if n % 2:
            print(f'{a + ((n // 2) * b)}')
        else:
            print((n // 2) * b)

    t -= 1