linha = input().split()
a = int(linha[0])
b = int(linha[1])
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
if primos.count(a) < 1:
  print('NO')
else:
  if primos.count(b) < 1:
    print('NO')
  else:
    if primos.index(a) + 1 == primos.index(b):
      print('YES')
    else:
      print('NO')
