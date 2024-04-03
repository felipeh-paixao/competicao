linha = input().split()
s = int(linha[0])
n = int(linha[1])
x = n
dragons =[]
z = 1
while(x):
    linha = input().split()
    y = []
    y.append(int(linha[0]))
    y.append(int(linha[1]))
    dragons.append(y)

    x -= 1

dragons.sort()

x = n

for i in range(x):    
    if s > dragons[i][0]:
        s += dragons[i][1]
    else:
        z = 0
        break

if z:
    print('YES')
else:
    print('NO')