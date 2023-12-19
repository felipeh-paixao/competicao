cases = int(input())
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for x in range(cases):
    acertos = 0
    num_letras = int(input())
    letras = input()
    for i in range(26):
        comparativo = letras.count(alfabeto[i])
        if comparativo >= i + 1:
            acertos += 1
    
    print(acertos)
