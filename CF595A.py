linha = input().split()
n = int(linha[0])
m = int(linha[1])
andares = []
 
contador = 0
x = 0
y = 2
for i in range(n):
    temp = input().split()
    andares.extend(temp)
 
while(y <= len(andares)):
        
    if andares[x:y].count('1'):
        contador += 1
    
    x += 2
    y += 2
 
print(contador)