cases = int(input())

for i in range(cases):
    n = int(input())
    resultado = 1
    numeros = input().split()
    numeros.sort(reverse=True)    
    numeros[-1] = (int(numeros[-1]) + 1)
    for numero in numeros:
        resultado *= int(numero)
    
    print(resultado)