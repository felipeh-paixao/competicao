n = int(input())
body = []
x = 0
y = 0
z = 0
for i in range(n):
    body.append(input().split())

for i in range(n):
    for j in range(3):
        if j == 0:
            x += int(body[i][j])
        elif j == 1:
            y += int(body[i][j])
        else:
            z += int(body[i][j])


if x  == 0 and  y == 0 and z == 0:
    print('YES')
else:
    print('NO')