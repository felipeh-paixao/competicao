x = int(input())
while(x):  
    
    names = []
    maior = 0
    for i in range(x):
        name = input()
        names.append(name)
        if len(name) > maior:
            maior = len(name)
    
    for nome in names:
        espace = maior - len(nome)
        print(' '*espace + nome)

    x = int(input())
    if(x != 0):
        print()