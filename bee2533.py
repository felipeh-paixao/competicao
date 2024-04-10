try:
    m = int(input())
    ira = 0
    x = m
    m *= 100
    while(x):
        linha = input().split()
        ira += (int(linha[0]) * int(linha[1])) / int(linha[1])

        x -= 1
    
    print('{:.4f}'.format(ira / m))

except EOFError:
    pass