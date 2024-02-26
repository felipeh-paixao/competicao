t = int(input())
while(t):
    linha = input()

    if linha.count('A') > linha.count('B'):
        print('A')
    else:
        print('B')
    t -= 1