# Jeff and Digits

n =  int(input())
linha = input().split()
linha.sort(reverse=True)
linha_1 = linha[:]
num = ''.join(linha)
teste = 1
x = -1
aux = 0
while(teste):    
    for i in range(1, len(num), 1):
        num = ''.join(linha_1)
        print(num)
        if i < len(num) - 1:
            aux = linha_1[i]
            linha_1[i] = linha_1[i + 1]
            linha_1[i + 1] = aux 
        
    
    teste = int(input())

    linha = linha[:x]
    linha_1 = linha[:]
    num = ''.join(linha_1)

    

    