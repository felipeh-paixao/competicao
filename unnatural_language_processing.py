casos = int(input())
while(casos):
    y = int(input())
    palavra = input()
    nova_palavra = ''
    consoante = 0
    vogal = 0
    for i in range(y):
        if 'a' < palavra[i] < 'e':
            consoante += 1
        else:
            vogal += 1

        if vogal == 2:
            nova_palavra += '.' + palavra[i]
            vogal = 0
            consoante = 0 
        elif consoante == 2:
            if palavra[i + 1] == 'a' or palavra[i + 1] == 'e':
                nova_palavra += '.' + palavra[i]
            else:
                nova_palavra += palavra[i] + '.'
            
            vogal = 0
            consoante = 0        
        else:
            nova_palavra += palavra[i]
    
    print(nova_palavra)    
   
    casos -= 1