import math
n = int(input())
hamster = input()
tempo = 0
cont = hamster.count('X') - len(hamster) // 2
if hamster.count('X') != len(hamster)//2:
    tempo = math.ceil(abs(((len(hamster) // 2) - hamster.count('X'))) / n)    

print(abs(cont))
for i in range(len(hamster)):
    if cont != 0:
        if cont > 0:
            if hamster[i] == 'X':
                print(hamster[i].lower(),end='')
                cont -= 1
            else:
                print(hamster[i],end='')
        else:
            if hamster[i] == 'x': 
                print(hamster[i].upper(),end='')
                cont += 1
            else:
                print(hamster[i],end='')
    else:
        print(hamster[i],end='')
