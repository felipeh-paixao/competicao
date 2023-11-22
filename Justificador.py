n = int(input())
while n != 0:
    nomes = []
    tamanho = 0
    for i in range(n):        
        nomes.append(input().strip())
        if len(nomes[i]) > tamanho:
            tamanho = len(nomes[i])
    
    for nome in nomes:
        print(' ' * (tamanho - len(nome)) + nome)
        
    print()

    n = int(input())    
    


           