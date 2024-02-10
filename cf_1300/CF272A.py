n = int(input())
n += 1
linha = input().split()
soma = 0
contador = 0
for num in linha:
    soma += int(num)

resto = soma % n
x = (n+1) - resto
for i in range(resto,6,x):
    contador += 1

print(contador)