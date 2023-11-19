maior = int(input())
posicao = 1

for i in range(1,100):
    auxiliar = int(input())
    if maior < auxiliar:
        maior = auxiliar
        posicao = i + 1
print(maior)
print(posicao)