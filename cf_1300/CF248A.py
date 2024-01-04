#Cupboards
n = int(input())
direita = []
esquerda = []
segundos = 0
for i in range(n):
    linha = input().split()
    direita.append(linha[0])
    esquerda.append(linha[1])

if direita.count('0') > direita.count('1'):
    segundos += (n - direita.count('0'))
else:
    segundos += (n - direita.count('1'))

if esquerda.count('0') > esquerda.count('1'):
    segundos += (n - esquerda.count('0'))
else:
    segundos += (n - esquerda.count('1'))

print(segundos)