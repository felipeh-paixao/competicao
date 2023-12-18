#Enigma

linha =  input().split()
n = int(linha[1])
d = linha[0]
comparativo = d
contador = 0

if d[0] == '?':
    d = '1' + d[1:]

d = int(d.replace('?', '0'))
multiplo_anterior = d - (d % n)

if multiplo_anterior != d:
    multiplo_anterior += n

while len(str(multiplo_anterior)) <= len(comparativo):
    for i in range(len(comparativo)):
        if comparativo[i] != '?':
            if comparativo[i] != str(multiplo_anterior)[i]:
                contador += 1
    
    if contador == 0:
        break
    else:
        multiplo_anterior += n
        contador = 0

if contador == 0:
    print(multiplo_anterior)
else:
    print('*')        
