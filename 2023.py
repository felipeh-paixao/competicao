t = int(input())
while(t):
    maior = 0
    menor = 0
    linha = input().split()
    a = int(linha[0])
    b = int(linha[1])

    if a > b:
        maior = a
        menor = b
    else:
        menor = a
        maior = b
    
    if menor == 1:
        print(maior * 2)
    elif maior % menor == 0:
        aux = maior / menor
        print(int(maior * aux))
    elif maior % 2 == 0 and menor % 2 == 0:
        print(int((maior / 2) * menor))
    else:
        print(maior * menor)






    t -= 1
