mensagem = input()
i = 0
saida = ''
while(i < len(mensagem)):
    if mensagem[i] == '.':
        saida += '0'
        i += 1
    elif mensagem[i + 1] == '.':
        saida += '1'
        i += 2
    else:
        saida += '2'
        i += 2

print(saida)