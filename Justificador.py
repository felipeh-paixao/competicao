n = int(input())
while n != 0:
    nomes = []
    tamanho = 0   

    for i in range(n):        
        nomes.append(input())
        if len(nomes[i]) > tamanho:
            tamanho = len(nomes[i])
    
    for nome in nomes:
        nome = ' ' * (tamanho - len(nome)) + nome
        print(nome)        
    
    n = int(input())
    if(n != 0):
        print()  
        