linha = input().split()

n = int(linha[0])
s = int(linha[1])

number = []

linha_1 = input().split()

for lin in linha_1:
    number.append(int(lin))

number.sort()

if sum(number[0:-1]) <= s:
    print('YES')
else:
    print('NO')