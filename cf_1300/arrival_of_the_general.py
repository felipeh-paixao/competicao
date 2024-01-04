n = int(input())
linha = input().split()
a = []
for valor in linha:
    a.append(int(valor))

maior = a.index(max(a))
menor = a.index(min(a))
menor = a[menor]

aux = 0
for i in range(n):
    if a[i] == menor:
        aux = i

menor = aux
resultado = 0
if maior > menor:
    resultado = maior + ((n - 1) - menor) - 1
    print(resultado)
else:
    resultado = maior + ((n - 1) - menor)
print(resultado)