linha = input().split()
n = int(linha[0]) # numeros de amigos
k = int(linha[1]) # numeros de refrigerantes
l = int(linha[2]) # ml por garrafas
c = int(linha[3]) # numeros de limoes
d = int(linha[4]) # numeros de fatias por limao
p = int(linha[5]) # gramas de sal
nl = int(linha[6])
np = int(linha[7])

menor = 0

ml_disp = k * l
fatias_disp = c * d

nl = ml_disp // nl
np = p // np

if nl < np:
    menor = nl
else:
    menor = np

if menor > fatias_disp:
    menor = fatias_disp

menor = menor // n

print(menor)
