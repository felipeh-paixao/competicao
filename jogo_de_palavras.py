cont = 1
while True:
    palavra = input()    
    if palavra == '*':
        break

    maior = palavra
    menor = palavra    

    n = len(palavra)
    for i in range(n):
        
        if palavra > maior:
            maior = palavra
        
        if palavra < menor:
            menor = palavra
        
        palavra = list(palavra)
        palavra_removida = palavra.pop()
        palavra.insert(0, palavra_removida)
        palavra = ''.join(palavra)
    
    print(f'Caso {cont}: {menor} {maior}')
    
    cont += 1

