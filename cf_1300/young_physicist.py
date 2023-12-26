n = int(input())
body = []
soma = 0
for i in range(n):
    body.append(input().split())

for i in range(n):
    for j in range(n):
        soma += int(body[i][j])

if soma == 0:
    print('YES')
else:
    print('NO')