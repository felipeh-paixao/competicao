teste = int(input())

for i in range(teste):
    linha = input()
    if linha == 'abc':
        print('YES')
    else:
        if linha == 'bca' or linha == 'cab':
            print('NO')
        else:
            print('YES')