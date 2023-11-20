linha_de_entrada = input()

n1 = int(linha_de_entrada.split()[0])
n2 = int(linha_de_entrada.split()[1])
soma = n1 + n2

while soma > 0:
    soma = str(soma)
    for i in soma:
        if i != '0':
            print(i,end='')
    
    print()

    linha_de_entrada = input()
    n1 = int(linha_de_entrada.split()[0])
    n2 = int(linha_de_entrada.split()[1])
    soma = n1 + n2