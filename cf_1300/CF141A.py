#Amusing Joke
x = input()
a = []
b = []
c = []
aux = 1

for i in x:
    a.append(i)

x = input()

for i in x:
    b.append(i)

x = input()

for i in x:
    c.append(i)



for i in a:
    if c.count(i) > 0:
        c.remove(i)
    else:
        aux = 0
        break

for j in b:    
    if c.count(j) > 0:
        c.remove(j)
    else:
        aux = 0
        break

if aux and len(c) == 0:
    print('YES')
else:
    print('NO')
