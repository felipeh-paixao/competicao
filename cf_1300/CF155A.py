#I_love_%username%
n = int(input())
pontos = []
linha = input().split()
maior = 0
menor = 0
contador = 0
for i in range(n):
    pontos.append(int(linha[i]))
    if i > 0:
        if pontos[i] > maior:
            maior = pontos[i]
            contador += 1
        if pontos[i] < menor:
            menor = pontos[i]
            contador += 1
    else:
        maior = pontos[i]
        menor = pontos[i]

print(contador)