#Effective Approach


n = int(input())
numeros = input().split()
m = int(input())
queries = input().split()
vasya = 0
petya = 0
aux = 0
valores = {}
for i in queries:        
    if i in valores:
        aux = valores[i]
    else:
        aux = numeros.index(i)
        valores[i] = aux        
    
    vasya += aux + 1 
    petya += n - aux

print(f'{vasya} {petya}')